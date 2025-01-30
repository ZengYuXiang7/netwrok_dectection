```python
|2025-01-19 02:39:47| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x770e51168500>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:39:47| ********************Experiment Start********************
|2025-01-19 02:41:14| Round=1 BestEpoch= 94 Acc=0.7866 F1=0.6848 Precision=0.7195 Recall=0.6717 Training_time=52.7 s 

|2025-01-19 02:41:14| ********************Experiment Results:********************
|2025-01-19 02:41:14| Acc: 0.7866 ± 0.0000
|2025-01-19 02:41:14| F1: 0.6848 ± 0.0000
|2025-01-19 02:41:14| P: 0.7195 ± 0.0000
|2025-01-19 02:41:14| Recall: 0.6717 ± 0.0000
|2025-01-19 02:41:14| train_time: 52.6729 ± 0.0000
|2025-01-19 02:41:14| Flops: 708352
|2025-01-19 02:41:14| Params: 5413
|2025-01-19 02:41:14| Inference time: 0.06 ms
|2025-01-19 02:41:15| ********************Experiment Success********************
```

