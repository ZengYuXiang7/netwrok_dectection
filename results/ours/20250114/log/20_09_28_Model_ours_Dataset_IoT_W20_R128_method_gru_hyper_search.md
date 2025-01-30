```python
|2025-01-14 20:09:28| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c9c04b1d820>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 20:09:28| ********************Experiment Start********************
|2025-01-14 20:23:38| Round=1 BestEpoch=153 Acc=0.9176 F1=0.8726 Precision=0.8709 Recall=0.8753 Training_time=642.9 s 

|2025-01-14 20:23:38| ********************Experiment Results:********************
|2025-01-14 20:23:38| Acc: 0.9176 ± 0.0000
|2025-01-14 20:23:38| F1: 0.8726 ± 0.0000
|2025-01-14 20:23:38| P: 0.8709 ± 0.0000
|2025-01-14 20:23:38| Recall: 0.8753 ± 0.0000
|2025-01-14 20:23:38| train_time: 642.9134 ± 0.0000
|2025-01-14 20:23:39| Flops: 4383379456
|2025-01-14 20:23:39| Params: 2041813
|2025-01-14 20:23:39| Inference time: 0.54 ms
|2025-01-14 20:23:39| ********************Experiment Success********************
```

