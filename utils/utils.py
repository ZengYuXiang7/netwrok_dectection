# coding : utf-8
# Author : yuxiang Zeng

import os
import time
import random
import nbformat
import platform
import torch as t
import numpy as np

def set_settings(args):
    if args.debug:
        args.rounds = 2
        args.epochs = 1
        args.lr = 1e-3
        args.decay = 1e-3

    if args.classification:
        args.loss_func = 'CrossEntropyLoss'

    def find_closest_power_of_2(train_size, percentage=0.10):
        # 计算目标 batch size
        target_bs = int(train_size * percentage)

        # 定义 2 的幂次序列
        powers_of_2 = [2 ** i for i in range(1, 15)]  # 2, 4, 8, ..., 256

        # 找到最接近的 2 的幂次
        closest_bs = min(powers_of_2, key=lambda x: abs(x - target_bs))

        return closest_bs

    # 找到最接近的 batch size
    # if config.train_size <= 10000:
    #     config.bs = find_closest_power_of_2(config.train_size)

    # 检查操作系统
    if platform.system() == "Darwin":  # "Darwin" 是 macOS 的系统标识
        args.device = 'cpu' if args.device != 'mps' else 'mps'

    else:
        # 如果不是 macOS，你可以选择默认设置为 CPU 或 GPU
        args.device = "cuda" if t.cuda.is_available() else "cpu"

    
    return args


# 时间种子
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    t.manual_seed(seed)
    t.cuda.manual_seed(seed)
    t.cuda.manual_seed_all(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    t.backends.cudnn.deterministic = True
    t.backends.cudnn.benchmark = False


def to_cuda(inputs, values):
    import dgl
    cuda_inputs = []
    for item in inputs:
        if isinstance(item, dgl.DGLGraph):
            # 如果元素是 DGL 图对象，转移到 CUDA
            cuda_inputs.append(item.to('cuda'))
        elif isinstance(item, list):
            # 如果元素是列表（假设包含图对象），处理每个图对象
            cuda_list = [tensor.to('cuda') if isinstance(tensor, dgl.DGLGraph) else tensor for tensor in item]
            cuda_inputs.append(cuda_list)
        else:
            # 否则，假设它是一个 PyTorch 张量
            cuda_inputs.append(item.to('cuda'))
    # 将 values 转移到 CUDA
    cuda_values = values.to('cuda')
    return cuda_inputs, cuda_values


def optimizer_zero_grad(*optimizers):
    for optimizer in optimizers:
        optimizer.zero_grad()


def optimizer_step(*optimizers):
    for optimizer in optimizers:
        optimizer.step()


def lr_scheduler_step(*lr_scheduler):
    for scheduler in lr_scheduler:
        scheduler.step()


def makedir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    return False


def computer_info():
    def showinfo(tip, info):
        print("{} : {}".format(tip, info))

    showinfo("操作系统及版本信息", platform.platform())
    showinfo('获取系统版本号', platform.version())
    showinfo('获取系统名称', platform.system())
    showinfo('系统位数', platform.architecture())
    showinfo('计算机类型', platform.machine())
    showinfo('计算机名称', platform.node())
    showinfo('处理器类型', platform.processor())
    showinfo('计算机相关信息', platform.uname())




#########################################################################
def create_ipynb_file(cells, file_name):
    # 创建一个空白的Notebook
    nb = nbformat.v4.new_notebook()
    # 添加单元格内容
    for cell in cells:
        cell_type = cell.get('cell_type', 'code')
        source = cell.get('source', '')
        metadata = cell.get('metadata', {})

        if cell_type == 'code':
            nb.cells.append(nbformat.v4.new_code_cell(source=source, metadata=metadata))
        elif cell_type == 'markdown':
            nb.cells.append(nbformat.v4.new_markdown_cell(source=source, metadata=metadata))
        else:
            raise ValueError("Invalid cell type: {}".format(cell_type))
    # 检查文件是否存在并添加编号
    file_path = f'{time.localtime(time.time()).tm_mon}.{time.localtime(time.time()).tm_mday} '
    file_path += f'{file_name}.ipynb'  # 指定文件路径和名称
    i = 2
    while os.path.exists(file_path):
        file_path = f'{time.localtime(time.time()).tm_mon}.{time.localtime(time.time()).tm_mday} '
        file_path += f'{file_name}{i}.ipynb'
        i += 1
    # 保存为.ipynb文件
    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + f'\"{file_path}\"' + ' 文件保存成功!')


def create_sh_file(cells, file_name):
    # 检查文件是否存在并添加编号
    file_path = f'{time.localtime(time.time()).tm_mon}.{time.localtime(time.time()).tm_mday} '
    file_path += f'{file_name}.sh'  # 指定文件路径和名称
    i = 2
    while os.path.exists(file_path):
        file_path = f'{time.localtime(time.time()).tm_mon}.{time.localtime(time.time()).tm_mday} '
        file_path += f'{file_name}{i}.sh'
        i += 1
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in range(len(cells)):
            f.write(cells[item])
            f.write('\n')
    print(time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + f'\"{file_path}\"' + ' 文件保存成功!')


def get_file_name():
    import sys
    py_name = sys.argv[0]
    # print("The script name is:", py_name)
    return py_name
