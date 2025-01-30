```python
|2025-01-19 18:36:22| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c3b45337a10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 18:36:22| ********************Experiment Start********************
|2025-01-19 18:39:57| Round=1 BestEpoch= 89 Acc=0.9049 F1=0.8383 Precision=0.8459 Recall=0.8397 Training_time=146.5 s 

|2025-01-19 18:39:57| ********************Experiment Results:********************
|2025-01-19 18:39:57| Acc: 0.9049 ± 0.0000
|2025-01-19 18:39:57| F1: 0.8383 ± 0.0000
|2025-01-19 18:39:57| P: 0.8459 ± 0.0000
|2025-01-19 18:39:57| Recall: 0.8397 ± 0.0000
|2025-01-19 18:39:57| train_time: 146.4932 ± 0.0000
|2025-01-19 18:39:57| Flops: 686668800
|2025-01-19 18:39:57| Params: 253325
|2025-01-19 18:39:57| Inference time: 0.49 ms
|2025-01-19 18:39:58| ********************Experiment Success********************
```

