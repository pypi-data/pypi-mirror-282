import sys
import re

sys.path.append("../src")
from langtorch import TextModule, _TextTensor
from langtorch.tt import ActivationGPT
from langtorch import Text
from langtorch.api.call import chat, auth
import torch
import numpy as np

import logging


# You can change this to logging.INFO to disable printing logs about api cal
logging.basicConfig(level=logging.CRITICAL)
from pyparsing import *

# auth(key_path="path/to/api_keys.json")
auth("D:/Techne/api_keys.json")