# coding : utf-8
# Author : yuxiang Zeng

import os
import time
import random
import nbformat
import platform
import torch as t
import numpy as np

def set_settings(config):
    if config.debug:
        config.rounds = 2
        config.epochs = 1
        config.lr = 1e-3
        config.decay = 1e-3

    if config.classification:
        config.loss_func = 'CrossEntropyLoss'
    else:
        config.num_classes = 1

    # 检查操作系统
    if platform.system() == "Darwin":  # "Darwin" 是 macOS 的系统标识
        config.device = 'cpu' if config.device != 'mps' else 'mps'

    else:
        # 如果不是 macOS，你可以选择默认设置为 CPU 或 GPU
        config.device = "cuda" if t.cuda.is_available() else "cpu"

    return config


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


