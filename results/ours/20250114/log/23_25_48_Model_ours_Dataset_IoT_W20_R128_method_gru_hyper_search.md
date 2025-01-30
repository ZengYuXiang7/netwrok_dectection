```python
|2025-01-14 23:25:48| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ca40a6d2b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-14 23:25:48| ********************Experiment Start********************
|2025-01-14 23:43:08| Round=1 BestEpoch= 82 Acc=0.9224 F1=0.8827 Precision=0.8842 Recall=0.8817 Training_time=724.2 s 

|2025-01-14 23:43:08| ********************Experiment Results:********************
|2025-01-14 23:43:08| Acc: 0.9224 ± 0.0000
|2025-01-14 23:43:08| F1: 0.8827 ± 0.0000
|2025-01-14 23:43:08| P: 0.8842 ± 0.0000
|2025-01-14 23:43:08| Recall: 0.8817 ± 0.0000
|2025-01-14 23:43:08| train_time: 724.1976 ± 0.0000
|2025-01-14 23:43:09| Flops: 7452856320
|2025-01-14 23:43:09| Params: 5668181
|2025-01-14 23:43:09| Inference time: 1.47 ms
|2025-01-14 23:43:09| ********************Experiment Success********************
```

