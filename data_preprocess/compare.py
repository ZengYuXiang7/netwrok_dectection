import test3
import ratio
import os
import glob
import matplotlib.pyplot as plt
import numpy as np  # 导入 numpy 库

radio_result = []
my_result = []

def plot_results(nmae_radio, cos_radio, nmae_my, cos_my, labels):
    x = np.arange(len(labels))  # 将 range 对象转换为 numpy 数组
    width = 0.35  # the width of the bars

    # 创建一个包含两个子图的图形
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # 绘制 NMAE 图表
    rects1 = axs[0].bar(x - width/2, nmae_radio, width, label='Radio NMAE')
    rects2 = axs[0].bar(x + width/2, nmae_my, width, label='My NMAE')

    axs[0].set_xlabel('Datasets')
    axs[0].set_ylabel('NMAE Scores')
    axs[0].set_title('Comparison of NMAE Scores')
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(labels, rotation=45, ha='right')  # 旋转标签并设置对齐方式
    axs[0].legend()

    def autolabel(rects, ax):
        """Attach a text label above each bar in *rects*, displaying its height with 3 decimal places."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{:.3f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1, axs[0])
    autolabel(rects2, axs[0])

    # 绘制 COS 图表
    rects3 = axs[1].bar(x - width/2, cos_radio, width, label='Radio COS')
    rects4 = axs[1].bar(x + width/2, cos_my, width, label='My COS')

    axs[1].set_xlabel('Datasets')
    axs[1].set_ylabel('COS Scores')
    axs[1].set_title('Comparison of COS Scores')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(labels, rotation=45, ha='right')  # 旋转标签并设置对齐方式
    axs[1].legend()

    autolabel(rects3, axs[1])
    autolabel(rects4, axs[1])

    fig.tight_layout()

    plt.show()

if __name__ == '__main__':
    csv_dir = './datasets/MedBIoT/csv/100s/'
    input_pattern = os.path.join(csv_dir, '*.csv')
    csv_files = glob.glob(input_pattern)
    labels = [os.path.splitext(os.path.basename(csv_file))[0] for csv_file in csv_files]  # 只保留文件名部分

    for csv_file in csv_files:
        radio_metrics = ratio.output(csv_file)
        my_metrics = test3.cluster_and_plot(csv_file, 8, 25)
        radio_result.append(radio_metrics)
        my_result.append(my_metrics)

    nmae_radio = [metrics[0] for metrics in radio_result]
    cos_radio = [metrics[1] for metrics in radio_result]
    nmae_my = [metrics[0] for metrics in my_result]
    cos_my = [metrics[1] for metrics in my_result]

    plot_results(nmae_radio, cos_radio, nmae_my, cos_my, labels)