# coding : utf-8
# Author : yuxiang Zeng
import time
import subprocess
import numpy as np
from datetime import datetime

from anaconda_project.internal.cli.command_commands import add_command


######################################################################################################
# 在这里写执行实验逻辑
def debug(commands):
    commands = []
    # 执行所有命令
    for command in commands:
        run_command(command, log_file)
    return True

def Baselines(commands):
    commands = []
    # 执行所有命令
    for command in commands:
        run_command(command, log_file)
    return True


def Ablation(hyper=None):
    commands = []
    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]
    # 执行所有命令
    for command in commands:
        run_command(command, log_file)
    return True


def Our_model(hyper=None):
    commands = []

    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]

    # 执行所有命令
    for command in commands:
        run_command(command, log_file)
    return True


def only_once_experiment(exper_name, hyper=None):
    commands = []
    command = f"python train_model.py --exp_name {exper_name} --retrain 0"
    commands.append(command)

    if hyper:
        commands = [add_parameter(command, hyper) for command in commands]

    # 执行所有命令
    for command in commands:
        run_command(command, log_file)
    return True

######################################################################################################
# 在这里写执行顺序
def experiment_run():
    hyper_dict = {
        'flow_length_limit': [20, 30, 40],
        'rank': [50, 80, 100],
    }
    best_hyper = hyper_search('MLPConfig', hyper_dict, retrain=0)
    only_once_experiment('MLPConfig', best_hyper)

    best_hyper = hyper_search('LSTMConfig', hyper_dict, retrain=0)
    only_once_experiment('LSTMConfig', best_hyper)

    best_hyper = hyper_search('CNNConfig', hyper_dict, retrain=0)
    only_once_experiment('CNNConfig', best_hyper)

    best_hyper = hyper_search('TestConfig', hyper_dict, retrain=0)
    only_once_experiment('TestConfig', best_hyper)
    return True


def hyper_search(exp_name, hyper_dict, retrain=1):
    """
    多超参数逐步优化
    :param hyper_dict: 字典形式的超参数和其对应搜索范围，例如：
                       {'Rank': [10, 50, 100], 'Order': [0.1, 0.5, 1.0]}
    :return: 最优超参数字典
    """
    from utils.config import get_config
    import pickle
    config = get_config(exp_name)
    best_hyper = {}
    # Run the all hyper
    with open(log_file, 'a') as f:
        for hyper_name, hyper_values in hyper_dict.items():
            current_best_value = None
            best_metric = 0 if config.classification else 1e9
            print(hyper_name, hyper_values)
            for value in hyper_values:
                # 设置最基础的实验
                command = f"python train_model.py --exp_name {exp_name} --hyper_search 1 --retrain {retrain} "
                # 将搜好的超参数配置上
                # print(command)
                if len(best_hyper) != 0:
                    for best_param_key, best_param_values in best_hyper.items():
                        command += f"--{best_param_key} {best_param_values} "
                # print(command)
                # 搜索正在的参数
                command += f"--{hyper_name} {value} "
                # 将其他参数还未探索的先默认使用第一个
                # print(command)
                for other_hyper_name, other_hyper_values in hyper_dict.items():
                    if other_hyper_name not in command:
                        command += f"--{other_hyper_name} {other_hyper_values[0]} "
                        config.__dict__[other_hyper_name] = other_hyper_values[0]

                print(command)
                subprocess.run(command, shell=True)
                config.__dict__.update(best_hyper)
                config.__dict__[hyper_name] = value
                log_filename = f'Model_{config.model}_Dataset_{config.dataset}_W{config.flow_length_limit:d}_R{config.rank}'
                this_expr_metrics = pickle.load(open(f'./results/metrics/' + log_filename + '.pkl', 'rb'))
                # 根据任务选择优化目标
                if config.classification:
                    metric = 'Acc'
                    current_metric = np.mean(this_expr_metrics[metric])
                    if current_metric > best_metric:
                        best_metric = current_metric
                        current_best_value = value
                else:
                    metric = 'MAE'
                    current_metric = np.mean(this_expr_metrics[metric])
                    if current_metric < best_metric:
                        best_metric = current_metric
                        current_best_value = value
                f.write(f"Hyperparameter: {hyper_name}, Value: {value}, Metrics: {current_metric}\n")
            # 更新最优超参数
            print(f"Best {hyper_name}: {current_best_value}\n")
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

    experiment_run()


    with open(log_file, 'a') as f:
        f.write(f"All commands executed successfully.\n\n")


if __name__ == "__main__":
    log_file = "run.log"
    main()
