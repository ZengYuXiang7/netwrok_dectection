```python
|2025-01-14 15:49:04| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b4c9791af00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 15:49:04| ********************Experiment Start********************
|2025-01-14 16:02:32| Round=1 BestEpoch=140 Acc=0.9258 F1=0.8883 Precision=0.8875 Recall=0.8896 Training_time=599.8 s 

|2025-01-14 16:02:32| ********************Experiment Results:********************
|2025-01-14 16:02:32| Acc: 0.9258 ± 0.0000
|2025-01-14 16:02:32| F1: 0.8883 ± 0.0000
|2025-01-14 16:02:32| P: 0.8875 ± 0.0000
|2025-01-14 16:02:32| Recall: 0.8896 ± 0.0000
|2025-01-14 16:02:32| train_time: 599.8245 ± 0.0000
|2025-01-14 16:02:36| Flops: 4383444992
|2025-01-14 16:02:36| Params: 2042069
|2025-01-14 16:02:36| Inference time: 0.55 ms
|2025-01-14 16:02:36| ********************Experiment Success********************
```

