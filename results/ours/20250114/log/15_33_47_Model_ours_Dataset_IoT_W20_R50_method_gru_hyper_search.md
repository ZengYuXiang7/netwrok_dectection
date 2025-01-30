```python
|2025-01-14 15:33:47| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x754af60a59d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 15:33:47| ********************Experiment Start********************
|2025-01-14 15:40:44| Round=1 BestEpoch= 59 Acc=0.9181 F1=0.8738 Precision=0.8845 Recall=0.8659 Training_time=248.7 s 

|2025-01-14 15:40:44| ********************Experiment Results:********************
|2025-01-14 15:40:44| Acc: 0.9181 ± 0.0000
|2025-01-14 15:40:44| F1: 0.8738 ± 0.0000
|2025-01-14 15:40:44| P: 0.8845 ± 0.0000
|2025-01-14 15:40:44| Recall: 0.8659 ± 0.0000
|2025-01-14 15:40:44| train_time: 248.7276 ± 0.0000
|2025-01-14 15:40:45| Flops: 683174400
|2025-01-14 15:40:45| Params: 315975
|2025-01-14 15:40:45| Inference time: 0.55 ms
|2025-01-14 15:40:45| ********************Experiment Success********************
```

