```python
|2025-01-17 23:48:11| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76d1ec74c770>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:48:11| ********************Experiment Start********************
|2025-01-17 23:51:53| Round=1 BestEpoch=315 Acc=0.7367 F1=0.6249 Precision=0.6447 Recall=0.6152 Training_time=164.6 s 

|2025-01-17 23:51:53| ********************Experiment Results:********************
|2025-01-17 23:51:53| Acc: 0.7367 ± 0.0000
|2025-01-17 23:51:53| F1: 0.6249 ± 0.0000
|2025-01-17 23:51:53| P: 0.6447 ± 0.0000
|2025-01-17 23:51:53| Recall: 0.6152 ± 0.0000
|2025-01-17 23:51:53| train_time: 164.6225 ± 0.0000
|2025-01-17 23:51:53| Flops: 517632
|2025-01-17 23:51:53| Params: 3943
|2025-01-17 23:51:53| Inference time: 0.05 ms
|2025-01-17 23:51:53| ********************Experiment Success********************
```

