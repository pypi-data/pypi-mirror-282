# Work in progress, not fully functional
import torch
from torch.nn.modules.loss import _Reduction

from langtorch import ctx
from .activation import Activation
from .textmodule import TextModule
from langtorch.tensors import TextTensor

session = ctx


class _TextLoss(TextModule):
    reduction: str = 'sum'

    def __init__(self, prompt: TextTensor, activation=None, backward_prompt=None, key="loss", reduction: str = 'sum', **kwargs) -> None:
        super(_TextLoss, self).__init__(prompt=prompt, activation=activation, key=key, backward_prompt=backward_prompt, is_param=False, **kwargs)
        self.reduction = reduction
        self.register_forward_hook(self.reduction_hook)

    @staticmethod
    def reduction_hook(module, input, loss):
        if module.reduction == 'none':
            return loss
        elif module.reduction == 'sum':
            return loss.sum()
        else:
            raise ValueError(f"Unknown reduction: {loss.reduction}")


class CompareAnswersLoss(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: TextTensor, target: TextTensor, prompt: TextTensor):
        ctx.save_for_backward(input, target)
        assert input.shape == target.shape, f"Input and target must have the same shape. Got {input.shape} and {target.shape} instead."
        loss_query = prompt * input.add_key_("input") * target.add_key_('target')
        loss = Activation(session.default_model_for_functions)(loss_query)
        return loss

    @staticmethod
    def backward(ctx, grad_output):
        input, target = ctx.saved_tensors
        grad_input = grad_target = None

        if ctx.needs_input_grad[0]:
            # Compute gradient for input
            grad_input = grad_output

        if ctx.needs_input_grad[1]:
            # Compute gradient for target
            grad_target = -grad_input

        # The gradients for non-tensors arguments must be None.
        return grad_input, grad_target, None


class TextLoss(_TextLoss):
    key: str = "loss"

# class DropoutCorrectAnswer(TextModule):
#     def forward(self):
#         super().forward

class BinaryTextLoss(_TextLoss):
    def __init__(self, prompt: TextTensor, backward_prompt = "{input}\nProvide an informative description of the differences between the answers.", activation=None, key="loss", reduction: str = 'none', **kwargs):
        super(BinaryTextLoss, self).__init__(prompt=prompt, activation=activation, key=key, reduction=reduction, backward_prompt=backward_prompt)
        self.activation.max_tokens = 2
        self.register_forward_hook(self.to_01_hook)
        self.activation.gradient_mask = None

    def forward(self, input: TextTensor, target: TextTensor):
        loss = super().forward(TextTensor(input).add_key("input") + TextTensor(target).add_key("target"))
        return loss

    @staticmethod
    def to_01_hook(module, input, output):
        answers = [str(m).lower()[:3] for m in output.flat]
        yes_no_dict = {
            'yes': 1, 'y': 1, 'tru': 1, 't': 1, '1': 1,
            'no': 0, 'n': 0, 'fal': 0, 'f': 0, '0': 0
        }
        if any(ans not in yes_no_dict for ans in answers):
            print(f"Error! Invalid answer in Binary Loss: {answers} \nExpected: Yes or No")

        module.activation.gradient_mask = torch.Tensor([not bool(yes_no_dict.get(ans, 0)) for ans in answers]).reshape(
            output.shape) != True


