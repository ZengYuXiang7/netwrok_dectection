```python
|2025-01-19 02:41:17| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d533f77e9f0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:41:17| ********************Experiment Start********************
|2025-01-19 02:43:51| Round=1 BestEpoch=191 Acc=0.7935 F1=0.6874 Precision=0.6977 Recall=0.6849 Training_time=105.9 s 

|2025-01-19 02:43:51| ********************Experiment Results:********************
|2025-01-19 02:43:51| Acc: 0.7935 ± 0.0000
|2025-01-19 02:43:51| F1: 0.6874 ± 0.0000
|2025-01-19 02:43:51| P: 0.6977 ± 0.0000
|2025-01-19 02:43:51| Recall: 0.6849 ± 0.0000
|2025-01-19 02:43:51| train_time: 105.8786 ± 0.0000
|2025-01-19 02:43:51| Flops: 924672
|2025-01-19 02:43:51| Params: 7083
|2025-01-19 02:43:51| Inference time: 0.05 ms
|2025-01-19 02:43:51| ********************Experiment Success********************
```

