import numpy as np


class MinMaxScaler:
    """
    Min-Max 归一化类，用于将数据缩放到指定范围（默认为 [0, 1]）。
    支持反归一化操作。
    """

    def __init__(self, feature_range=(0, 1)):
        self.min_val = None
        self.max_val = None
        self.feature_range = feature_range

    def fit(self, data):
        """
        计算数据的最小值和最大值，用于归一化。

        Args:
            data (numpy.ndarray): 输入数据。
        """
        self.min_val = np.min(data, axis=0)
        self.max_val = np.max(data, axis=0)

    def transform(self, data):
        """
        对数据进行归一化。

        Args:
            data (numpy.ndarray): 输入数据。
        Returns:
            numpy.ndarray: 归一化后的数据。
        """
        if self.min_val is None or self.max_val is None:
            raise ValueError("MinMaxScaler is not fitted yet. Call 'fit' first.")

        scale = self.feature_range[1] - self.feature_range[0]
        normalized_data = (data - self.min_val) / (self.max_val - self.min_val)
        return normalized_data * scale + self.feature_range[0]

    def inverse_transform(self, normalized_data):
        """
        将归一化后的数据反归一化回原始范围。

        Args:
            normalized_data (numpy.ndarray): 归一化的数据。
        Returns:
            numpy.ndarray: 反归一化后的数据。
        """
        if self.min_val is None or self.max_val is None:
            raise ValueError("MinMaxScaler is not fitted yet. Call 'fit' first.")

        scale = self.feature_range[1] - self.feature_range[0]
        data = (normalized_data - self.feature_range[0]) / scale
        return data * (self.max_val - self.min_val) + self.min_val