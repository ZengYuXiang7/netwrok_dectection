```python
|2025-01-19 09:17:51| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xae84b17b560>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 09:17:51| ********************Experiment Start********************
|2025-01-19 09:17:52| Acc=0.8860 F1=0.8207 Precision=0.8253 Recall=0.8178 time=86.0 s 
|2025-01-19 09:17:52| Acc=0.8877 F1=0.8285 Precision=0.8303 Recall=0.8279 time=124.2 s 
|2025-01-19 09:17:52| Acc=0.8881 F1=0.8233 Precision=0.8337 Recall=0.8180 time=137.1 s 
|2025-01-19 09:17:52| Acc=0.8831 F1=0.8231 Precision=0.8276 Recall=0.8211 time=139.6 s 
|2025-01-19 09:17:52| Acc=0.8833 F1=0.8134 Precision=0.8197 Recall=0.8088 time=103.0 s 
|2025-01-19 09:17:52| ********************Experiment Results:********************
|2025-01-19 09:17:52| Acc: 0.8856 ± 0.0021
|2025-01-19 09:17:52| F1: 0.8218 ± 0.0049
|2025-01-19 09:17:52| P: 0.8273 ± 0.0047
|2025-01-19 09:17:52| Recall: 0.8188 ± 0.0062
|2025-01-19 09:17:52| train_time: 117.9955 ± 20.5764
|2025-01-19 09:17:53| Flops: 126144000
|2025-01-19 09:17:53| Params: 62521
|2025-01-19 09:17:53| Inference time: 0.08 ms
|2025-01-19 09:17:53| ********************Experiment Success********************
```

