import torch

def get_cuda():
    
    use_cuda = torch.cuda.is_available()

    if use_cuda:
        device = "cuda"
        print('__CUDNN VERSION:', torch.backends.cudnn.version())
        print('__Number CUDA Devices:', torch.cuda.device_count())
        print('__CUDA Device Name:',torch.cuda.get_device_name(0))
        print('__CUDA Device Total Memory [GB]:',torch.cuda.get_device_properties(0).total_memory/1e9)

        memory_information = {
            "Total memory" : torch.cuda.get_device_properties(0).total_memory,
            "Memory reserved" : torch.cuda.memory_reserved(0),
            "Memory allocated" : torch.cuda.memory_allocated(0),
            "Free reserved": torch.cuda.memory_reserved(0) - torch.cuda.memory_allocated(0)  # free inside reserved
        }

        for key in memory_information:
            print(key, '->', memory_information[key] / (1024 ** 3), "GB")

    else:
        device = "cpu"
        print("no cuda")
        
    return device
