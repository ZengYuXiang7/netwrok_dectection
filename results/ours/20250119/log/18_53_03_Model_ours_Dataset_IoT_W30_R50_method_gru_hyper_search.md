```python
|2025-01-19 18:53:03| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a9be7f22810>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 2, 'verbose': 1,
}
|2025-01-19 18:53:03| ********************Experiment Start********************
|2025-01-19 18:56:23| Round=1 BestEpoch= 82 Acc=0.8997 F1=0.8336 Precision=0.8417 Recall=0.8333 Training_time=132.3 s 

|2025-01-19 19:00:17| Round=2 BestEpoch=101 Acc=0.9040 F1=0.8403 Precision=0.8483 Recall=0.8365 Training_time=163.9 s 

|2025-01-19 19:00:17| ********************Experiment Results:********************
|2025-01-19 19:00:17| Acc: 0.9018 ± 0.0022
|2025-01-19 19:00:17| F1: 0.8370 ± 0.0034
|2025-01-19 19:00:17| P: 0.8450 ± 0.0033
|2025-01-19 19:00:17| Recall: 0.8349 ± 0.0016
|2025-01-19 19:00:17| train_time: 148.0921 ± 15.7893
|2025-01-19 19:00:17| Flops: 686668800
|2025-01-19 19:00:17| Params: 253325
|2025-01-19 19:00:17| Inference time: 0.47 ms
|2025-01-19 19:00:18| ********************Experiment Success********************
```

