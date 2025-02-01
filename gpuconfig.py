import torch
print("CUDA Available:", torch.cuda.is_available())  # Should be True
print("CUDA Version:", torch.version.cuda)  # Should match nvidia-smi (12.7)
print("GPU Count:", torch.cuda.device_count())  # Should be 1 (or more)
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
