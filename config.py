import torch

# device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")