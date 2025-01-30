```python
|2025-01-14 16:02:39| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c1fa771ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 256, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 16:02:39| ********************Experiment Start********************
|2025-01-14 16:10:58| Round=1 BestEpoch= 47 Acc=0.9158 F1=0.8715 Precision=0.8683 Recall=0.8759 Training_time=279.4 s 

|2025-01-14 16:10:58| ********************Experiment Results:********************
|2025-01-14 16:10:58| Acc: 0.9158 ± 0.0000
|2025-01-14 16:10:58| F1: 0.8715 ± 0.0000
|2025-01-14 16:10:58| P: 0.8683 ± 0.0000
|2025-01-14 16:10:58| Recall: 0.8759 ± 0.0000
|2025-01-14 16:10:58| train_time: 279.3693 ± 0.0000
|2025-01-14 16:10:59| Flops: 17413971968
|2025-01-14 16:10:59| Params: 8135061
|2025-01-14 16:10:59| Inference time: 1.23 ms
|2025-01-14 16:11:00| ********************Experiment Success********************
```

