import os
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity

def read_packet_data(csv_file):
    """读取数据包大小"""
    packet_sizes = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if(int(row['length']) > 1514): continue
            packet_sizes.append(int(row['length']))
    return np.array(packet_sizes)


def calculate_density_bins(data, adaptive_density, num_intervals=10):
    """根据核密度估计结果划分区间"""
    x_range = np.linspace(data.min(), data.max(), 1000)
    cumulative_density = np.cumsum(adaptive_density)  # 累计密度
    cumulative_density /= cumulative_density[-1]  # 归一化到 [0, 1]
    
    # 根据累积密度等分区间
    bin_edges = [x_range[0]]
    for i in range(1, num_intervals + 1):
        target = i / num_intervals
        idx = np.searchsorted(cumulative_density, target)
        bin_edges.append(x_range[idx])
    return bin_edges

def cluster_and_plot(csv_file, num_intervals, bandwidth, alpha = 0.5):
    """主流程：读取数据、密度估计、划分区间和绘图"""
    # 1. 读取数据包大小
    data = read_packet_data(csv_file)
    
    # 2. 自适应带宽核密度估计
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(data[:, None])

    log_density = kde.score_samples(data[:, None])
    local_density = np.exp(log_density)
    avg_density = np.mean(local_density)
    adaptive_bandwidth = bandwidth * (local_density / avg_density) ** (-alpha)
    x_range = np.linspace(data.min(), data.max(), 1000)
    adaptive_density = np.zeros_like(x_range)
    for i, x in enumerate(x_range):
        weights = np.exp(-0.5 * ((x - data) / adaptive_bandwidth) ** 2) / (adaptive_bandwidth * np.sqrt(2 * np.pi))
        adaptive_density[i] = weights.sum() / len(data)
        
    # 3. 根据密度划分区间
    bin_edges = calculate_density_bins(data, adaptive_density, num_intervals)

    # 4. 绘制结果
    plot_density_and_bins(data, kde, bin_edges)
    
    # 5. 输出误差率
    clac_COS_and_NMAE(data, bin_edges)

def clac_COS_and_NMAE(data, bin_edges):
    """计算COS和NMAE"""
    data = list(data)
    data_=[]
    for packet in data:
        flag = False
        for i in range(len(bin_edges) - 1):
            if bin_edges[i] <= packet < bin_edges[i+1] or packet == bin_edges[-1]:
                packet_compress = (bin_edges[i+1] + bin_edges[i]) / 2
                packet_compress = int(packet_compress)
                data_.append(packet_compress)
                flag = True
                break
        if flag == False:
            print(f"some packet is not in the range it's size={packet}")
    data_=np.array(data_)
    data=np.array(data)
    print(len(data))
    print(len(data_))
    COS=np.sum(data*data_)/np.sqrt(np.sum(data*data))/np.sqrt(np.sum(data_*data_))
    NMAE=np.sum(np.abs(data-data_))/np.sum(np.abs(data))
    print(f'NMAE={NMAE},COS={COS}')
def plot_density_and_bins(data, kde, bin_edges):
    """绘制密度估计和区间划分结果"""

    
    # 统计数据包大小的数量
    size_counts = Counter(data)
    sizes = list(size_counts.keys())
    counts = list(size_counts.values())

    x_range = np.linspace(data.min(), data.max(), 1000)
    density = np.exp(kde.score_samples(x_range[:, None]))

    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.plot(x_range, density, color='blue', label='KDE')
    ax1.set_xlabel('Packet Size')
    ax1.set_ylabel('Density', color='blue')
    ax1.tick_params('y', colors='blue')
    ax1.grid(True)
    
    ax2 = ax1.twinx()
    
    cmap = plt.get_cmap('Paired')
    
    for i in range(len(bin_edges) - 1):
        start, end = bin_edges[i], bin_edges[i + 1]
        ax1.axvspan(start, end, alpha=0.2, color=cmap(i), label=f'Bin {i+1}: [{start:.1f}, {end:.1f}]')

        indices = [j for j, size in enumerate(sizes) if start <= size <= end]
        cluster_size = [sizes[j] for j in indices]
        cluster_count = [counts[j] for j in indices]
        
        sorted_indices = np.argsort(cluster_size)
        cluster_size = np.array(cluster_size)[sorted_indices]
        cluster_count = np.array(cluster_count)[sorted_indices]
        
        ax2.scatter(cluster_size, cluster_count, marker='*', label=f'Cluster {i+1}: [{start:.1f}, {end:.1f}]', color=cmap(i))

    # 设置第二个 Y 轴的标签和颜色
    ax2.set_ylabel('Count', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

    plt.title('Packet Size Density and Interval Division')
    if not os.path.exists('./exprimental'): os.mkdir('./exprimental')
    fig_path = f"./exprimental/{csv_file.split('/')[-1].replace('.csv','.png')}"
    plt.savefig(fig_path)

# 替换为您的数据文件路径
csv_file = './datasets/MedBIoT/csv/1000s/mirai_mal_spread_all_1000s.csv'
cluster_and_plot(csv_file, num_intervals=16, bandwidth=25)
