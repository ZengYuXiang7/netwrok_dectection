# coding : utf-8
# Author : yuxiang Zeng

import torch as t
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def ErrorMetrics(realVec, estiVec, config):
    if isinstance(realVec, np.ndarray):
        realVec = realVec.astype(float)
    elif isinstance(realVec, t.Tensor):
        realVec = realVec.cpu().detach().numpy().astype(float)
    if isinstance(estiVec, np.ndarray):
        estiVec = estiVec.astype(float)
    elif isinstance(estiVec, t.Tensor):
        estiVec = estiVec.cpu().detach().numpy().astype(float)
    if not config.classification:
        absError = np.abs(estiVec - realVec)
        MAE = np.mean(absError)
        RMSE = np.linalg.norm(absError) / np.sqrt(np.array(absError.shape[0]))
        NMAE = np.sum(np.abs(realVec - estiVec)) / np.sum(realVec)
        NRMSE = np.sqrt(np.sum((realVec - estiVec) ** 2)) / np.sqrt(np.sum(realVec ** 2))
        Acc = []
        thresholds = [0.01, 0.05, 0.10]
        for threshold in thresholds:
            threshold = realVec * threshold  # 定义阈值为真实值的5%
            accurate_predictions = absError < threshold
            accuracy = np.mean(accurate_predictions.astype(float))
            Acc.append(accuracy)

        return {
            'NMAE': NMAE,
            'NRMSE': NRMSE,
            'MAE': MAE,
            'RMSE': RMSE,
            'Acc_10': Acc[2],
        }
    else:
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
        AC = accuracy_score(realVec, estiVec)
        PR = precision_score(realVec, estiVec, average='macro', zero_division=0)  # 添加 zero_division 参数
        RC = recall_score(realVec, estiVec, average='macro', zero_division=0)  # 保持已有的 zero_division 参数
        F1 = f1_score(realVec, estiVec, average='macro')  # 如果是多分类问题，可以修改 average 参数
        return {
            'AC': AC,
            'PR': PR,
            'RC': RC,
            'F1': F1,
        }

