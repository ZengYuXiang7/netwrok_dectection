```python
|2025-01-19 19:00:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x766da88ca570>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 3, 'verbose': 1,
}
|2025-01-19 19:00:20| ********************Experiment Start********************
|2025-01-19 19:04:43| Round=1 BestEpoch=116 Acc=0.9014 F1=0.8326 Precision=0.8358 Recall=0.8335 Training_time=189.8 s 

|2025-01-19 19:08:52| Round=2 BestEpoch=107 Acc=0.9045 F1=0.8448 Precision=0.8530 Recall=0.8408 Training_time=176.4 s 

|2025-01-19 19:08:52| ********************Experiment Results:********************
|2025-01-19 19:08:52| Acc: 0.9030 ± 0.0015
|2025-01-19 19:08:52| F1: 0.8387 ± 0.0061
|2025-01-19 19:08:52| P: 0.8444 ± 0.0086
|2025-01-19 19:08:52| Recall: 0.8371 ± 0.0036
|2025-01-19 19:08:52| train_time: 183.1222 ± 6.6868
|2025-01-19 19:08:52| Flops: 686668800
|2025-01-19 19:08:52| Params: 253325
|2025-01-19 19:08:52| Inference time: 0.51 ms
|2025-01-19 19:08:53| ********************Experiment Success********************
```

