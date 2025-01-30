```python
|2025-01-14 15:40:48| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x734c412567e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 15:40:48| ********************Experiment Start********************
|2025-01-14 15:49:00| Round=1 BestEpoch= 73 Acc=0.9235 F1=0.8829 Precision=0.8832 Recall=0.8832 Training_time=314.1 s 

|2025-01-14 15:49:00| ********************Experiment Results:********************
|2025-01-14 15:49:00| Acc: 0.9235 ± 0.0000
|2025-01-14 15:49:00| F1: 0.8829 ± 0.0000
|2025-01-14 15:49:00| P: 0.8832 ± 0.0000
|2025-01-14 15:49:00| Recall: 0.8832 ± 0.0000
|2025-01-14 15:49:00| train_time: 314.0532 ± 0.0000
|2025-01-14 15:49:01| Flops: 1110873728
|2025-01-14 15:49:01| Params: 514957
|2025-01-14 15:49:01| Inference time: 0.56 ms
|2025-01-14 15:49:01| ********************Experiment Success********************
```

