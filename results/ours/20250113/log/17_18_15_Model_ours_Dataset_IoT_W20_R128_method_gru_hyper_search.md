```python
|2025-01-13 17:18:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7485ad436cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 17:18:15| ********************Experiment Start********************
|2025-01-13 17:34:49| Round=1 BestEpoch=164 Acc=0.9238 F1=0.8879 Precision=0.8905 Recall=0.8863 Training_time=763.9 s 

|2025-01-13 17:34:49| ********************Experiment Results:********************
|2025-01-13 17:34:49| Acc: 0.9238 ± 0.0000
|2025-01-13 17:34:49| F1: 0.8879 ± 0.0000
|2025-01-13 17:34:49| P: 0.8905 ± 0.0000
|2025-01-13 17:34:49| Recall: 0.8863 ± 0.0000
|2025-01-13 17:34:49| train_time: 763.9210 ± 0.0000
|2025-01-13 17:34:53| Flops: 4386988032
|2025-01-13 17:34:53| Params: 2057493
|2025-01-13 17:34:53| Inference time: 0.80 ms
|2025-01-13 17:34:53| ********************Experiment Success********************
```

