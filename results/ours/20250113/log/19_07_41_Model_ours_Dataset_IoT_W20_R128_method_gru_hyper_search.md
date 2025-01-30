```python
|2025-01-13 19:07:41| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c3ae020ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 19:07:41| ********************Experiment Start********************
|2025-01-13 19:16:32| Round=1 BestEpoch= 80 Acc=0.9146 F1=0.8681 Precision=0.8769 Recall=0.8632 Training_time=350.7 s 

|2025-01-13 19:16:32| ********************Experiment Results:********************
|2025-01-13 19:16:32| Acc: 0.9146 ± 0.0000
|2025-01-13 19:16:32| F1: 0.8681 ± 0.0000
|2025-01-13 19:16:32| P: 0.8769 ± 0.0000
|2025-01-13 19:16:32| Recall: 0.8632 ± 0.0000
|2025-01-13 19:16:32| train_time: 350.7172 ± 0.0000
|2025-01-13 19:16:35| Flops: 4389277696
|2025-01-13 19:16:35| Params: 2077781
|2025-01-13 19:16:35| Inference time: 0.77 ms
|2025-01-13 19:16:36| ********************Experiment Success********************
```

