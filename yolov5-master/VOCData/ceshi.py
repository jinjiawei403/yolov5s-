import torch

# 检查CUDA是否可用
cuda_available = torch.cuda.is_available()

if cuda_available:
    # 获取GPU设备数量
    num_gpu = torch.cuda.device_count()

    # 获取当前使用的GPU索引
    current_gpu_index = torch.cuda.current_device()

    # 获取当前GPU的名称
    current_gpu_name = torch.cuda.get_device_name(current_gpu_index)

    # 获取GPU显存的总量和已使用量
    total_memory = torch.cuda.get_device_properties(current_gpu_index).total_memory / (1024 ** 3)  # 显存总量(GB)
    used_memory = torch.cuda.memory_allocated(current_gpu_index) / (1024 ** 3)  # 已使用显存(GB)
    free_memory = total_memory - used_memory  # 剩余显存(GB)

    print(f"CUDA可用，共有 {num_gpu} 个GPU设备可用。")
    print(f"当前使用的GPU设备索引：{current_gpu_index}")
    print(f"当前使用的GPU设备名称：{current_gpu_name}")
    print(f"GPU显存总量：{total_memory:.2f} GB")
    print(f"已使用的GPU显存：{used_memory:.2f} GB")
    print(f"剩余GPU显存：{free_memory:.2f} GB")
else:
    print("CUDA不可用。")

# 检查PyTorch版本
print(f"PyTorch版本：{torch.__version__}")

