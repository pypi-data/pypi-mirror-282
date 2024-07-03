from typing import Optional

import torch


def set_device(dev: Optional[str] = None):
    if dev is not None:
        return torch.device(dev)
    return torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")