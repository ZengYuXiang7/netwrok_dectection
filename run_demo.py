# coding : utf-8
# Author : yuxiang Zeng
import time
import subprocess
import numpy as np
from datetime import datetime

from anaconda_project.internal.cli.command_commands import add_command

from train_model import get_experiment_name


######################################################################################################
# 在这里写执行实验逻辑
def debug():
    return True

def Baselines(hyper_dict):
    hyper_dict = {
        'rank': [40, 50, 60],
        'dataset': ['IoT']
    }
    # best_hyper = hyper_search('MLPConfig', hyper_dict, retrain=1)
    # only_once_experiment('MLPConfig', best_hyper)
    #
    # best_hyper = hyper_search('LSTMConfig', hyper_dict, retrain=1)
    # only_once_experiment('LSTMConfig', best_hyper)
    #
    # best_hyper = hyper_search('CNNConfig', hyper_dict, retrain=1)
    # only_once_experiment('CNNConfig', best_hyper)

    best_hyper = hyper_search('GCNConfig', hyper_dict, grid_search=0, retrain=1)
    only_once_experiment('GCNConfig', best_hyper)  # {'continue_train': 1}

    best_hyper = hyper_search('GATConfig', hyper_dict, grid_search=0, retrain=1)
    only_once_experiment('GATConfig', best_hyper)  # {'continue_train': 1}

    best_hyper = hyper_search('GINConfig', hyper_dict, grid_search=0, retrain=1)
    only_once_experiment('GINConfig', best_hyper)  # {'continue_train': 1}

    # only_once_experiment('DAPPConfig')  # {'continue_train': 1}
    # only_once_experiment('GraphIoTConfig')  # {'continue_train': 1}


    return True


def Ablation(hyper=None):
    return True


def Our_model(hyper=None):
    return True


######################################################################################################
# 在这里写执行顺序
def experiment_run():

    hyper_dict = {
        'rank': [64],
        # 'num_layers': [2],
        # 'n_heads': [4],
        # 'try_exp': [i + 1 for i in range(4)],
    }
    best_hyper = hyper_search('TestConfig', hyper_dict, grid_search=0, retrain=1, debug=0)
    # only_once_experiment('TestConfig', best_hyper)
    return True


# 采用最佳的参数做最后一次复现实验
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


def hyper_search(exp_name, hyper_dict, grid_search=0, retrain=1, debug=0):
    """
    多超参数搜索，可以在逐个超参数搜索和网格搜索之间切换。

    :param exp_name: 实验名称
    :param hyper_dict: 字典形式的超参数和其对应搜索范围，例如：
                       {
                         'Rank': [10, 50, 100],
                         'Order': [0.1, 0.5, 1.0]
                       }
    :param retrain: 是否重复训练标志
    :param grid_search: 若为 True，则做网格搜索，否则做逐个超参数的“逐步优化”。
    :return: 最优超参数字典
    """
    import subprocess
    import numpy as np
    import pickle
    from itertools import product

    # 根据你的项目结构，导入 get_config
    from utils.config import get_config

    config = get_config(exp_name)
    # 准备一个日志文件
    log_file = f'./run.log'

    # 用于保存当前已确定的最佳超参数
    best_hyper = {}
    # 判断分类 or 回归，用于后续选择评价指标
    classification_task = getattr(config, 'classification', False)

    # 定义一个辅助函数，用于执行命令并读取结果
    def run_and_get_metric(cmd_str, config, chosen_hyper, debug=False):
        # 更新 config 中的超参数
        print(cmd_str)
        config.__dict__.update(chosen_hyper)
        log_filename = f"Model_{config.model}_Dataset_{config.dataset}_W{config.flow_length_limit:d}_R{config.rank}"
        # 运行命令
        if debug:
            print(log_filename, chosen_hyper)
        else:
            subprocess.run(cmd_str, shell=True)
        # 读取 metrics
        metric_file_address = f'./results/metrics/' + get_experiment_name(config)
        this_expr_metrics = pickle.load(open(metric_file_address+ '.pkl', 'rb'))

        # 根据任务类型选取关键指标
        if classification_task:
            metric_name = 'Acc'
        else:
            metric_name = 'MAE'
        best_value = np.mean(this_expr_metrics[metric_name])
        return best_value

    # =======================
    # 如果要做网格搜索
    # =======================
    if grid_search:
        """
        对 hyper_dict 做笛卡尔积，将所有超参数组合都尝试一遍
        例如:
          hyper_dict = {
            'Rank': [10, 50, 100],
            'Order': [0.1, 0.5, 1.0]
          }
          会产生 3x3=9 种组合
        """
        hyper_keys = list(hyper_dict.keys())
        hyper_values_list = [hyper_dict[k] for k in hyper_keys]

        best_metric = 0 if classification_task else 1e9
        best_combo = None
        with open(log_file, 'a') as f:
            f.write("\n=== Grid Search ===\n")
            for combo in product(*hyper_values_list):
                # combo 是一个元组，如 (10, 0.1) -> 对应 (Rank=10, Order=0.1)
                combo_dict = dict(zip(hyper_keys, combo))

                # 构建命令
                command = f"python train_model.py --exp_name {exp_name} --hyper_search 1 --retrain {retrain} "
                # 在命令里添加所有超参数
                for param_key, param_val in combo_dict.items():
                    command += f"--{param_key} {param_val} "

                # 先给其他未出现在 combo_dict 的超参数，指定其默认值
                for other_key, other_values in hyper_dict.items():
                    if other_key not in combo_dict:
                        command += f"--{other_key} {other_values[0]} "

                f.write(f"COMMAND: {command}\n")
                # 运行并获取结果
                current_metric = run_and_get_metric(command, config, combo_dict, debug)

                if classification_task:
                    # 分类，metric 越大越好
                    if current_metric > best_metric:
                        best_metric = current_metric
                        best_combo = combo_dict
                else:
                    # 回归/预测，metric (MAE) 越小越好
                    if current_metric < best_metric:
                        best_metric = current_metric
                        best_combo = combo_dict
                print(f"Combo: {combo_dict}, Metric= {current_metric}\n")
                f.write(f"Combo: {combo_dict}, Metric= {current_metric}\n")

            # 记录最优组合
            print(f"Best combo: {best_combo}, Best metric: {best_metric}\n")
            f.write(f"Best combo: {best_combo}, Best metric: {best_metric}\n")
        return best_combo

    # =======================
    # 否则，逐个超参数搜索
    # =======================
    else:
        """
        保持原有的“逐个超参数”逻辑
        """

        with open(log_file, 'a') as f:
            f.write("\n=== Sequential Hyper Search ===\n")
            # 逐个超参数搜索
            for hyper_name, hyper_values in hyper_dict.items():
                # 如果只有一个值，直接写入
                if len(hyper_values) == 1:
                    best_hyper[hyper_name] = hyper_values[0]
                    continue

                current_best_value = None
                # 分类任务选最大，回归任务选最小
                local_best_metric = 0 if classification_task else 1e9

                f.write(f"\nHyper: {hyper_name}, Values: {hyper_values}\n")
                print(f"{hyper_name} => {hyper_values}")

                for value in hyper_values:
                    # 根据目前已有最优超参数 + 当前超参数构建命令
                    command = f"python train_model.py --exp_name {exp_name} --hyper_search 1 --retrain {retrain} "

                    # 先写入之前已经确定的 best_hyper
                    for best_param_key, best_param_value in best_hyper.items():
                        config.best_param_key = best_param_value
                        command += f"--{best_param_key} {best_param_value} "

                    # 再加当前要测试的
                    command += f"--{hyper_name} {value} "

                    # 对其他 hyper 未探索过的，使用它们的第一个值
                    for other_hyper_name, other_hyper_values in hyper_dict.items():
                        if other_hyper_name not in best_hyper and other_hyper_name != hyper_name:
                            config.other_hyper_name = other_hyper_values[0]
                            best_hyper[other_hyper_name] = other_hyper_values[0]
                            command += f"--{other_hyper_name} {other_hyper_values[0]} "

                    # 运行命令、获取 metric
                    chosen_dict = best_hyper.copy()
                    chosen_dict[hyper_name] = value

                    f.write(f"COMMAND: {command}\n")
                    current_metric = run_and_get_metric(command, config, chosen_dict, debug)

                    # 比较更新最优
                    if classification_task:
                        if current_metric > local_best_metric:
                            local_best_metric = current_metric
                            current_best_value = value
                    else:
                        if current_metric < local_best_metric:
                            local_best_metric = current_metric
                            current_best_value = value

                    f.write(f"Value: {value}, Metric: {current_metric}\n")

                # 结束后，更新最优
                best_hyper[hyper_name] = current_best_value
                print(f"==> Best {hyper_name}: {current_best_value}, local_best_metric: {local_best_metric}\n")
                f.write(f"==> Best {hyper_name}: {current_best_value}, local_best_metric: {local_best_metric}\n")

            # 全部结束后，打印并写日志
            f.write(f"The Best Hyperparameters: {best_hyper}\n")
        print("The Best Hyperparameters:", best_hyper)
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
