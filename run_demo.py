# coding : utf-8
# Author : yuxiang Zeng
import sys
import time
import subprocess
import numpy as np
from datetime import datetime

sys.dont_write_bytecode = True


def debug(commands):
    commands.append(f"python train_model.py --config_path ./exper_config.py --exp_name TestConfig "
                    f"--density 100 --retrain 1 --device cpu --rank 300 --rounds 2")
    return commands


def Baselines(commands):
    return commands


def Ablation(commands, hyper=None):
    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]
    return commands


def Our_model(commands, hyper=None):
    command = f"python train_model.py --config_path ./exper_config.py --exp_name TestConfig " \
              f"--retrain 1 --rounds 1  --dataset food --eval_set 1"
    commands.append(command)

    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]
    return commands


def experiment_command():
    commands = []
    # commands = Our_model(commands)
    # If we have hyper search, use this
    best_hyper = hyper_once('rank', [30, 50, 100])
    commands = Our_model(commands, best_hyper)
    return commands


# 一次性能的极致探索，采用这个实验
def final_experiment():
    commands = []
    best_hyper = hyper_once('rank', [10, 30, 50, 100])
    commands = Ablation(commands, best_hyper)
    commands = Our_model(commands, best_hyper)
    return commands


def hyper_once(hyper_name, different_hypers):
    from train_model import run
    from utils.config import get_config
    config = get_config()
    best_hyper, best_metric = None, 0 if config.classification else 1e9
    for hyper in different_hypers:
        config.__dict__[hyper_name] = hyper
        metrics = run(config)
        metric = 'Acc' if config.classification else 'MAE'
        if np.mean(metrics[metric]) > best_metric:
            best_metric = np.mean(metrics[metric])
            best_hyper = hyper
        print(metrics)
    print(f"The Best Hyper{hyper_name}, is {best_hyper}")
    best_hyper = {hyper_name: best_hyper}
    return best_hyper


def add_parameter(command: str, params: dict) -> str:
    for param_name, param_value in params.items():
        command += f" --{param_name} {param_value}"
    return command


def run_command(command, log_file, retry_count=0):
    success = False
    while not success:
        # 获取当前时间并格式化
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        # 如果是重试的命令，标记为 "Retrying"
        if retry_count > 0:
            retry_message = "Retrying"
        else:
            retry_message = "Running"

        # 将执行的命令和时间写入日志文件
        with open(log_file, 'a') as f:
            f.write(f"{retry_message} at {current_time}: {command}\n")

        # 直接执行命令，将输出和错误信息打印到终端
        process = subprocess.run(f'ulimit -s unlimited; ulimit -c unlimited&& ulimit -a && echo {command} &&' + command, shell=True)

        # 根据返回码判断命令是否成功执行
        if process.returncode == 0:
            success = True
        else:
            with open(log_file, 'a') as f:
                f.write(f"Command failed, retrying in 3 seconds: {command}\n")
            retry_count += 1
            time.sleep(3)  # 等待一段时间后重试


def main():
    log_file = "run.log"

    # 清空日志文件的内容
    with open(log_file, 'a') as f:
        f.write(f"Experiment Start!!!\n")

    commands = experiment_command()

    # 执行所有命令
    for command in commands:
        run_command(command, log_file)

    with open(log_file, 'a') as f:
        f.write(f"All commands executed successfully.\n")


if __name__ == "__main__":
    main()
