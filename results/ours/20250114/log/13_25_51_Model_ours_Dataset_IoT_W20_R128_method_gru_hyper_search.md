```python
|2025-01-14 13:25:51| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e258b4b3ec0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 13:25:51| ********************Experiment Start********************
|2025-01-14 13:39:45| Round=1 BestEpoch=140 Acc=0.9258 F1=0.8883 Precision=0.8875 Recall=0.8896 Training_time=619.0 s 

|2025-01-14 13:39:45| ********************Experiment Results:********************
|2025-01-14 13:39:45| Acc: 0.9258 ± 0.0000
|2025-01-14 13:39:45| F1: 0.8883 ± 0.0000
|2025-01-14 13:39:45| P: 0.8875 ± 0.0000
|2025-01-14 13:39:45| Recall: 0.8896 ± 0.0000
|2025-01-14 13:39:45| train_time: 618.9853 ± 0.0000
|2025-01-14 13:39:49| Flops: 4384100352
|2025-01-14 13:39:49| Params: 2047445
|2025-01-14 13:39:49| Inference time: 0.67 ms
|2025-01-14 13:39:49| ********************Experiment Success********************
```

