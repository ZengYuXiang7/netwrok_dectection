```python
|2025-01-13 19:30:45| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76d3fea84f20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 19:30:45| ********************Experiment Start********************
|2025-01-13 19:47:50| Round=1 BestEpoch=171 Acc=0.9249 F1=0.8854 Precision=0.8837 Recall=0.8881 Training_time=792.8 s 

|2025-01-13 19:47:50| ********************Experiment Results:********************
|2025-01-13 19:47:50| Acc: 0.9249 ± 0.0000
|2025-01-13 19:47:50| F1: 0.8854 ± 0.0000
|2025-01-13 19:47:50| P: 0.8837 ± 0.0000
|2025-01-13 19:47:50| Recall: 0.8881 ± 0.0000
|2025-01-13 19:47:50| train_time: 792.7516 ± 0.0000
|2025-01-13 19:47:51| Flops: 4387180544
|2025-01-13 19:47:51| Params: 2061397
|2025-01-13 19:47:51| Inference time: 0.81 ms
|2025-01-13 19:47:51| ********************Experiment Success********************
```

