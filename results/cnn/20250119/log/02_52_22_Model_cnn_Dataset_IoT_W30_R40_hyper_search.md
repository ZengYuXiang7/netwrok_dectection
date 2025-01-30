```python
|2025-01-19 02:52:22| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f960c955d00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:52:22| ********************Experiment Start********************
|2025-01-19 02:55:53| Round=1 BestEpoch=244 Acc=0.8630 F1=0.7843 Precision=0.8426 Recall=0.7743 Training_time=149.5 s 

|2025-01-19 02:55:53| ********************Experiment Results:********************
|2025-01-19 02:55:53| Acc: 0.8630 ± 0.0000
|2025-01-19 02:55:53| F1: 0.7843 ± 0.0000
|2025-01-19 02:55:53| P: 0.8426 ± 0.0000
|2025-01-19 02:55:53| Recall: 0.7743 ± 0.0000
|2025-01-19 02:55:53| train_time: 149.5276 ± 0.0000
|2025-01-19 02:55:53| Flops: 20387840
|2025-01-19 02:55:53| Params: 6021
|2025-01-19 02:55:53| Inference time: 0.09 ms
|2025-01-19 02:55:53| ********************Experiment Success********************
```

