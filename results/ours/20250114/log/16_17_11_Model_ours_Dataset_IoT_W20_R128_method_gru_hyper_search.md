```python
|2025-01-14 16:17:11| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ec9ba8bab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 16:17:11| ********************Experiment Start********************
|2025-01-14 16:29:32| Round=1 BestEpoch=122 Acc=0.9194 F1=0.8820 Precision=0.8843 Recall=0.8799 Training_time=534.2 s 

|2025-01-14 16:29:32| ********************Experiment Results:********************
|2025-01-14 16:29:32| Acc: 0.9194 ± 0.0000
|2025-01-14 16:29:32| F1: 0.8820 ± 0.0000
|2025-01-14 16:29:32| P: 0.8843 ± 0.0000
|2025-01-14 16:29:32| Recall: 0.8799 ± 0.0000
|2025-01-14 16:29:32| train_time: 534.1593 ± 0.0000
|2025-01-14 16:29:35| Flops: 4383444992
|2025-01-14 16:29:35| Params: 2042069
|2025-01-14 16:29:35| Inference time: 0.66 ms
|2025-01-14 16:29:36| ********************Experiment Success********************
```

