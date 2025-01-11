# coding : utf-8
# Author : Yuxiang Zeng
import torch


def merge_features(seq_input, time_stamp):
    N = len(seq_input)
    v = torch.zeros(2 * N)
    for i in range(1, 2 * N + 1):
        I = (i + 1) % 2  # Indicator function
        index = (i - 1) // 2  # Corresponding index in s_i or l_i
        if I == 1:
            v[i - 1] = seq_input[index]
        else:
            v[i - 1] = -time_stamp[index]
    return v


if __name__ == "__main__":
    # 示例归一化后的包长度
    normalized_lengths = torch.tensor([0.8, 0.9333, 0.4, 0.5333], dtype=torch.float32)
    # 示例归一化后的时间间隔
    normalized_times = torch.tensor([0.05, 0.1, 0.2, 0.3], dtype=torch.float32)

    # 调用函数
    merged_vector = merge_features(normalized_lengths, normalized_times)

    # 输出结果
    print("Normalized lengths:", normalized_lengths)
    print("Normalized times:", normalized_times)
    print("Merged feature vector:", merged_vector)