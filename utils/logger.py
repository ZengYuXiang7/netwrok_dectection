# coding : utf-8
# Author : yuxiang Zeng
# 日志
import os
import glob
import time
import logging
import numpy as np

from train_efficiency import get_efficiency
from utils.utils import makedir

class Logger:
    def __init__(
        self,
        filename,
        plotter,
        config,
        show_params=True
    ):
        self.clear_the_useless_logs()
        self.plotter = plotter
        self.exper_detail = f"Dataset : {config.dataset.upper()}, Model : {config.model}, Density : {config.density:.3f}, Bs : {config.bs}, Rank : {config.rank}, "
        self.fileroot = f'./results/{config.model}/' + time.strftime('%Y%m%d', time.localtime(time.time())) + '/log/'
        self.filename = filename
        makedir(self.fileroot)
        self.exper_time = time.strftime('%H_%M_%S', time.localtime(time.time())) + '_'
        self.exper_filename = self.fileroot + self.exper_time + self.filename
        if config.hyper_search:
            self.exper_filename += '_hyper_search'
        logging.basicConfig(level=logging.INFO, filename=f"{self.exper_filename}.md", filemode='w', format='%(message)s')
        # logging.basicConfig(level=logging.INFO, filename=f"{self.exper_filename}.md", filemode='w')
        self.logger = logging.getLogger(config.model)
        config.log = self
        self.config = config
        self.prepare_the_experiment(show_params)


    def prepare_the_experiment(self, show_params):
        self.logger.info('```python')
        if show_params:
            self.log(self.format_and_sort_config_dict(self.config.__dict__))

    def save_result(self, metrics):
        import pickle
        makedir('./results/metrics/')
        config_copy = self.config.__dict__.copy()
        if 'log' in config_copy:
            del config_copy['log']  # 移除无法序列化的 log 对象
        all_info = {'config': config_copy, 'dataset': self.config.model, 'model': self.config.model, 'train_size': self.config.train_size}
        for key in metrics:
            all_info[key] = metrics[key]
            all_info[key + '_mean'] = np.mean(metrics[key])
            all_info[key + '_std'] = np.std(metrics[key])
        # 保存序列化结果
        address = f'./results/metrics/' + self.filename
        with open(address + '.pkl', 'wb') as f:
            pickle.dump(all_info, f)

    # 日志记录
    def log(self, string):
        import time
        if string[0] == '\n':
            print('\n', end='')
            string = string[1:]
        final_string = time.strftime('|%Y-%m-%d %H:%M:%S| ', time.localtime(time.time())) + string
        self.only_print(string)
        self.logger.info(final_string)

    def __call__(self, string):
        self.log(string)

    def only_print(self, string):
        import time
        if string[0] == '\n':
            print('\n', end='')
            string = string[1:]
        green_string = f"\033[1;38;2;151;200;129m{time.strftime('|%Y-%m-%d %H:%M:%S| ', time.localtime(time.time()))}\033[0m" + f"\033[1m{string}\033[0m"
        print(green_string)

    def show_epoch_error(self, runId, epoch, monitor, epoch_loss, result_error, train_time):
        if self.config.verbose and epoch % self.config.verbose == 0:
            self.only_print(f"\033[1;38;2;151;200;129m{self.exper_detail}\033[0m")
            self.only_print(f'Best Epoch {monitor.best_epoch} = {monitor.best_score * -1:.4f}  now = {(epoch - monitor.best_epoch):d}')
            if self.config.classification:
                self.only_print(f"Round={runId + 1} Epoch={epoch + 1:03d} Loss={epoch_loss:.4f} vAc={result_error['AC']:.4f} vPr={result_error['PR']:.4f} vRc={result_error['RC']:.4f} vF1={result_error['F1']:.4f}  time={sum(train_time):.1f} s ")
            else:
                self.only_print(f"Round={runId + 1} Epoch={epoch + 1:03d} Loss={epoch_loss:.4f} vMAE={result_error['MAE']:.4f} vRMSE={result_error['RMSE']:.4f} vNMAE={result_error['NMAE']:.4f} vNRMSE={result_error['NRMSE']:.4f} time={sum(train_time):.1f} s ")

    def show_test_error(self, runId, monitor, results, sum_time):
        if self.config.classification:
            self(f'Round={runId + 1} BestEpoch={monitor.best_epoch:3d} Ac={results["AC"]:.4f} Pr={results["PR"]:.4f} Rc={results["RC"]:.4f} F1={results["F1"]:.4f} Training_time={sum_time:.1f} s \n')
        else:
            self(f'Round={runId + 1} BestEpoch={monitor.best_epoch:3d} MAE={results["MAE"]:.4f} RMSE={results["RMSE"]:.4f} NMAE={results["NMAE"]:.4f} NRMSE={results["NRMSE"]:.4f} Training_time={sum_time:.1f} s ')
        print()

    def format_and_sort_config_dict(self, config_dict, items_per_line=4):
        # Sort the dictionary by keys
        sorted_items = sorted(config_dict.items())
        formatted_str = ''
        for i in range(0, len(sorted_items), items_per_line):
            line_items = sorted_items[i:i + items_per_line]
            line_str = ', '.join([f"'{key}': {value}" for key, value in line_items])
            formatted_str += f"     {line_str},\n"
        return f"{{\n{formatted_str}}}".strip(',\n')


    def clear_the_useless_logs(self):
        def delete_small_log_files(directory):
            # 获取所有.log文件
            log_files = glob.glob(os.path.join(directory, '*.md'))
            number_lines = 15

            # 遍历所有的.log文件
            for file_path in log_files:
                try:
                    # 检查文件是否存在且可读
                    if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
                        print(f"Cannot access '{file_path}'. Skipping.")
                        continue

                    # 使用with语句安全地打开文件
                    with open(file_path, 'r') as file:
                        lines = file.readlines()

                    # 检查行数并删除文件
                    if len(lines) < number_lines:
                        os.remove(file_path)  # 删除文件
                        print(f"Deleted '{file_path}' as it had less than {number_lines} lines.")

                except OSError as e:
                    print(f"OS error processing file {file_path}: {e}")
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

        root_directory = f'./results/'
        for dirpath, dirnames, filenames in os.walk(root_directory):
            if 'log' in dirpath:
                delete_small_log_files(dirpath)

    def delete_empty_directories(self, dir_path):
        import os
        # 检查目录是否存在
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            # 遍历目录中的所有文件和子目录，从最底层开始
            for root, dirs, files in os.walk(dir_path, topdown=False):
                # 先删除空的子目录
                for name in dirs:
                    dir_to_remove = os.path.join(root, name)
                    # 如果目录是空的，则删除它
                    try:
                        if not os.listdir(dir_to_remove):  # 判断目录是否为空
                            os.rmdir(dir_to_remove)
                            print(f"Directory {dir_to_remove} has been deleted.")
                    except FileNotFoundError:
                        # 如果目录已经不存在，忽略此错误
                        pass
                # 检查当前目录是否也是空的，如果是则删除它
                try:
                    if not os.listdir(root):  # 判断当前根目录是否为空
                        os.rmdir(root)
                        print(f"Directory {root} has been deleted.")
                except FileNotFoundError:
                    # 如果目录已经不存在，忽略此错误
                    pass
        else:
            print(f"Directory {dir_path} does not exist.")


    # 邮件发送日志
    def send_email(self, subject, body, receiver_email="zengyuxiang@hnu.edu.cn"):
        if self.config.debug:
            return
        import yagmail
        import os
        import pickle

        if isinstance(body, dict):
            metrics = body
            body = []
            # Add experiment results
            body.append('*' * 10 + 'Experiment Results:' + '*' * 10)
            for key in metrics:
                body.append(f'{key}: {np.mean(metrics[key]):.4f} ± {np.std(metrics[key]):.4f}')

            flops, params, inference_time = get_efficiency(self.config)
            body.append(f"Flops: {flops:.0f}")
            body.append(f"Params: {params:.0f}")
            body.append(f"Inference time: {inference_time:.2f} ms")

            # Add experiment success message
            body.append('*' * 10 + 'Experiment Success' + '*' * 10)

            # Add metrics for each round
            for i in range(self.config.rounds):
                round_metrics = f"Round {i + 1} : "
                for key in metrics:
                    round_metrics += f"{key}: {metrics[key][i]:.4f} "
                body.append(round_metrics)


            # Add formatted config dictionary
            body.append(self.format_and_sort_config_dict(self.config.__dict__, 3))
        else:
            temp = body
            body = [self.format_and_sort_config_dict(self.config.__dict__, 3), temp]

        # Get email credentials
        email_code_address = os.path.expanduser('~') + '/qq_smtp_info.pickle'
        try:
            with open(email_code_address, 'rb') as f:
                all_info = pickle.load(f)
            sender_email = all_info['email']
            sender_password = all_info['password']
        except FileNotFoundError:
            print("Non-admin user, email sending functionality is disabled")
            return False

        try:
            # Initialize the SMTP server
            yag = yagmail.SMTP(user=sender_email, password=sender_password, host='smtp.qq.com')

            # Prepare the contents
            contents = body

            # Get the attachment path
            attachment_path = self.plotter.exper_filename + '.pdf'

            # Send the email with the attachment
            yag.send(
                to=receiver_email,
                subject=subject,
                contents=contents,
                attachments=attachment_path if os.path.isfile(attachment_path) else None
            )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")


    def end_the_experiment(self):
        self.logger.info('```')
        self.logger.info('')
        # self.logger.info('<div  align="center"> ')
        # self.logger.info(f'<img src="../fig/{self.exper_time + self.filename}.pdf" ')
        # self.logger.info('width = "900" height = "800" ')
        # self.logger.info('alt="1" align=center />')
        # self.logger.info('</div>')
        # 使用os.walk来遍历目录
        root_directory = f'./results/'
        self.delete_empty_directories(root_directory)
