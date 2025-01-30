```python
|2025-01-14 20:45:46| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': True, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x782621d45fa0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 20:45:46| ********************Experiment Start********************
|2025-01-14 20:55:44| Round=1 BestEpoch= 96 Acc=0.9238 F1=0.8856 Precision=0.8846 Recall=0.8871 Training_time=412.6 s 

|2025-01-14 20:55:44| ********************Experiment Results:********************
|2025-01-14 20:55:44| Acc: 0.9238 ± 0.0000
|2025-01-14 20:55:44| F1: 0.8856 ± 0.0000
|2025-01-14 20:55:44| P: 0.8846 ± 0.0000
|2025-01-14 20:55:44| Recall: 0.8871 ± 0.0000
|2025-01-14 20:55:44| train_time: 412.6091 ± 0.0000
|2025-01-14 20:55:45| Flops: 4383379456
|2025-01-14 20:55:45| Params: 2041813
|2025-01-14 20:55:45| Inference time: 0.58 ms
|2025-01-14 20:55:46| ********************Experiment Success********************
```

