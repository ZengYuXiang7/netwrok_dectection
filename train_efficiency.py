# coding : utf-8
# Author : yuxiang Zeng


# def estimate_gpu_memory(model, sample_input, config):
#     # Assuming input_size is a tuple, e.g., (batch_size, channels, height, width)
#     model = model.to(config.device)
#     dummy_input = tuple(item.to(config.device) for item in sample_input)
#     with torch.cuda.profiler.profile():
#         model(dummy_input)
#     memory_allocated = torch.cuda.memory_allocated()
#     memory_reserved = torch.cuda.memory_reserved()
#     print(f"Memory Allocated: {memory_allocated / (1024 ** 2):.2f} MB")
#     print(f"Memory Reserved: {memory_reserved / (1024 ** 2):.2f} MB")
#     torch.cuda.empty_cache()

def calculate_flops_params(model, sample_input, args):
    from thop import profile
    sample_input = tuple([item.to(args.device) for item in sample_input][:-1])
    flops, params = profile(model.to(args.device), inputs=sample_input, verbose=False)
    # config.log.only_print(f"Flops: {flops} Params: {params}")
    return flops, params


def calculate_inference_time(model, sample_input, args):
    from time import time
    import numpy as np
    step = 100
    all_time = []
    for i in range(step):
        a = sample_input
        t1 = time()
        model(a)
        t2 = time()
        all_time.append(t2 - t1)
    inference_time = np.mean(all_time)
    # config.log.only_print(f"Average Inference Time: {inference_time * 1000:.2f} ms")
    return inference_time * 1000


def only_run():
    # Experiment Settings, logger, plotter
    from utils.config import get_config
    from utils.logger import Logger
    from utils.plotter import MetricsPlotter
    from utils.utils import set_settings, set_seed
    from train_model import Model

    args = get_config()
    set_settings(args)
    log_filename = f'Model_{args.model}_{args.dataset}_S{args.train_size}_R{args.rank}_Ablation{args.Ablation}'
    plotter = MetricsPlotter(log_filename, args)
    log = Logger(log_filename, plotter, args)

    from data import experiment, DataModule

    exper = experiment(args)
    datamodule = DataModule(exper, args)
    model = Model(datamodule, args).to(args.device)

    sample_inputs = next(iter(datamodule.train_loader))
    flops, params = calculate_flops_params(model, sample_inputs, args)
    inference_time = calculate_inference_time(model, sample_inputs, args)
    # estimate_gpu_memory(model, sample_inputs, config)
    return flops, params, inference_time


def get_efficiency(args):
    from train_model import Model
    from data import experiment, DataModule
    exper = experiment(args)
    datamodule = DataModule(exper, args)
    model = Model(datamodule, args)
    sample_inputs = next(iter(datamodule.train_loader))
    flops, params = calculate_flops_params(model, sample_inputs, args)
    inference_time = calculate_inference_time(model, sample_inputs, args)
    # estimate_gpu_memory(model, sample_inputs, config)
    return flops, params, inference_time


if __name__ == '__main__':
    only_run()
