import sys

sys.path.append("../src")
from langtorch import _TextTensor, TextModule
from langtorch import Session
import unittest
import numpy as np
import torch


class TestMul(unittest.TestCase):
    def test_mul1(self):
        tensor1 = _TextTensor("1")
        tensor1.requires_grad = True
        tensor2 = _TextTensor("2")
        tensor2.requires_grad = True
        tensor3 = tensor2*tensor1
        tensor3.backward()
        self.assertTrue((tensor2.grad == tensor1) and (tensor1.grad == tensor2))


    def test_mul2(self):
        tensor1 = _TextTensor([str(m) for m in range(9)])
        tensor1.requires_grad = True
        tensor2 =  _TextTensor([str(m) for m in range(9)][::-1])
        tensor2.requires_grad = True
        tensor3 = tensor2*tensor1
        tensor3.backward()

        self.assertTrue(np.all(tensor2.grad == tensor1) and np.all(tensor1.grad == tensor2))


    def test_add(self):
        tensor1 = _TextTensor("1")
        tensor1.requires_grad = True
        tensor2 = _TextTensor("2")
        tensor2.requires_grad = True
        tensor3 = tensor2*tensor1
        tensor4 = (tensor3+tensor2)
        tensor4.backward()
        self.assertTrue((tensor2.grad == tensor1) and (tensor1.grad == tensor2) and tensor3.grad is None )



if __name__ == "__main__":
    unittest.main()
