```python
|2025-01-19 19:08:55| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x701abd4aa4b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 4, 'verbose': 1,
}
|2025-01-19 19:08:55| ********************Experiment Start********************
|2025-01-19 19:13:03| Round=1 BestEpoch=109 Acc=0.8982 F1=0.8291 Precision=0.8328 Recall=0.8273 Training_time=176.9 s 

|2025-01-19 19:16:52| Round=2 BestEpoch= 97 Acc=0.8969 F1=0.8291 Precision=0.8313 Recall=0.8283 Training_time=158.2 s 

|2025-01-19 19:16:52| ********************Experiment Results:********************
|2025-01-19 19:16:52| Acc: 0.8975 ± 0.0007
|2025-01-19 19:16:52| F1: 0.8291 ± 0.0000
|2025-01-19 19:16:52| P: 0.8320 ± 0.0007
|2025-01-19 19:16:52| Recall: 0.8278 ± 0.0005
|2025-01-19 19:16:52| train_time: 167.5157 ± 9.3468
|2025-01-19 19:16:52| Flops: 686668800
|2025-01-19 19:16:52| Params: 253325
|2025-01-19 19:16:52| Inference time: 0.48 ms
|2025-01-19 19:16:53| ********************Experiment Success********************
```

