```python
|2025-01-20 00:21:08| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7728b97e6300>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 00:21:08| ********************Experiment Start********************
|2025-01-20 00:24:24| Round=1 BestEpoch= 51 Acc=0.9126 F1=0.8550 Precision=0.8714 Recall=0.8525 Training_time=115.7 s 

|2025-01-20 00:32:37| Round=2 BestEpoch=173 Acc=0.9216 F1=0.8699 Precision=0.8756 Recall=0.8664 Training_time=392.6 s 

|2025-01-20 00:40:41| Round=3 BestEpoch=170 Acc=0.9225 F1=0.8696 Precision=0.8763 Recall=0.8666 Training_time=384.7 s 

|2025-01-20 00:48:01| Round=4 BestEpoch=151 Acc=0.9235 F1=0.8717 Precision=0.8762 Recall=0.8705 Training_time=342.6 s 

|2025-01-20 00:51:54| Round=5 BestEpoch= 66 Acc=0.9123 F1=0.8513 Precision=0.8683 Recall=0.8415 Training_time=149.6 s 

|2025-01-20 00:51:54| ********************Experiment Results:********************
|2025-01-20 00:51:54| Acc: 0.9185 ± 0.0050
|2025-01-20 00:51:54| F1: 0.8635 ± 0.0086
|2025-01-20 00:51:54| P: 0.8736 ± 0.0032
|2025-01-20 00:51:54| Recall: 0.8595 ± 0.0109
|2025-01-20 00:51:54| train_time: 277.0236 ± 119.5941
|2025-01-20 00:51:54| Flops: 375737856
|2025-01-20 00:51:54| Params: 363345
|2025-01-20 00:51:54| Inference time: 0.73 ms
|2025-01-20 00:51:56| ********************Experiment Success********************
```

