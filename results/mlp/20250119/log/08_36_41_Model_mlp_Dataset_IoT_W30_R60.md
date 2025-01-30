```python
|2025-01-19 08:36:41| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf6f835d4500>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 08:36:41| ********************Experiment Start********************
|2025-01-19 08:36:42| Acc=0.7935 F1=0.6874 Precision=0.6977 Recall=0.6849 time=98.4 s 
|2025-01-19 08:36:42| Acc=0.7975 F1=0.6961 Precision=0.7146 Recall=0.6887 time=92.2 s 
|2025-01-19 08:36:42| Acc=0.8041 F1=0.7058 Precision=0.7624 Recall=0.6969 time=161.1 s 
|2025-01-19 08:36:43| Acc=0.7940 F1=0.6936 Precision=0.7115 Recall=0.6825 time=138.8 s 
|2025-01-19 08:36:43| Acc=0.7884 F1=0.6805 Precision=0.7042 Recall=0.6705 time=77.3 s 
|2025-01-19 08:36:43| ********************Experiment Results:********************
|2025-01-19 08:36:43| Acc: 0.7955 ± 0.0052
|2025-01-19 08:36:43| F1: 0.6927 ± 0.0085
|2025-01-19 08:36:43| P: 0.7181 ± 0.0229
|2025-01-19 08:36:43| Recall: 0.6847 ± 0.0086
|2025-01-19 08:36:43| train_time: 113.5602 ± 31.3002
|2025-01-19 08:36:43| Flops: 924672
|2025-01-19 08:36:43| Params: 7083
|2025-01-19 08:36:43| Inference time: 0.06 ms
|2025-01-19 08:36:43| ********************Experiment Success********************
```

