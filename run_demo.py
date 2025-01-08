# coding : utf-8
# Author : yuxiang Zeng
import time
import subprocess
import numpy as np
from datetime import datetime

######################################################################################################
# 在这里写执行实验逻辑
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
    command = f"python train_model.py --exp_name TestConfig " \
              f"--retrain 1 --rounds 1 --dataset huawei --eval_set 1"
    commands.append(command)

    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]
    return commands


def only_once_experiment(commands, exper_name, hyper=None):
    # command = f"python ./data_preprocess/data_generator.py"
    # commands.append(command)
    for time_interval in [10, 50, 100, 500, 1000, 2000]:
        command = f"python train_model.py --exp_name {exper_name} --time_interval {time_interval} " \
                  f"--retrain 1 --dataset malware"
        commands.append(command)

    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]
    return commands

######################################################################################################
# 在这里写执行顺序
def experiment_command():
    commands = []
    hyper_dict = {
        'rank': [20, 50, 100]
    }
    best_hyper = hyper_search('MLPConfig', hyper_dict)
    commands = only_once_experiment(commands, 'MLPConfig', best_hyper)

    # commands = only_once_experiment(commands, 'TestConfig', None)
    return commands


def hyper_search(exp_name, hyper_dict):
    """
    多超参数逐步优化
    :param hyper_dict: 字典形式的超参数和其对应搜索范围，例如：
                       {'Rank': [10, 50, 100], 'Order': [0.1, 0.5, 1.0]}
    :return: 最优超参数字典
    """
    from train_model import run
    from utils.config import get_config

    config = get_config(exp_name)
    best_hyper = {}
    with open(log_file, 'a') as f:
        for hyper_name, hyper_values in hyper_dict.items():
            current_best_value = None
            best_metric = 0 if config.classification else 1e9
            for value in hyper_values:
                # 设置当前超参数值，同时保留之前优化的最佳值
                config.__dict__.update(best_hyper)
                config.__dict__[hyper_name] = value
                # 运行实验
                metrics = run(config)
                # 根据任务选择优化目标
                if config.classification:
                    metric = 'Acc'
                    current_metric = np.mean(metrics[metric])
                    if current_metric > best_metric:
                        best_metric = current_metric
                        current_best_value = value
                else:
                    metric = 'MAE'
                    current_metric = np.mean(metrics[metric])
                    if current_metric < best_metric:
                        best_metric = current_metric
                        current_best_value = value
                f.write(f"Hyperparameter: {hyper_name}, Value: {value}, Metrics: {current_metric}\n")
            # 更新最优超参数
            print(hyper_name, current_best_value)
            best_hyper[hyper_name] = current_best_value
            f.write(f"Best {hyper_name}: {current_best_value}\n")
        f.write(f"The Best Hyperparameters: {best_hyper}\n")
    print(best_hyper)
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

    # 清空日志文件的内容
    with open(log_file, 'a') as f:
        f.write(f"Experiment Start!!!\n")

    commands = experiment_command()

    # 执行所有命令
    for command in commands:
        run_command(command, log_file)

    with open(log_file, 'a') as f:
        f.write(f"All commands executed successfully.\n\n")


if __name__ == "__main__":
    log_file = "run.log"
    main()
