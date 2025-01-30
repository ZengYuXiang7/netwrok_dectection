```python
|2025-01-18 23:58:17| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7674fff92b70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 23:58:17| ********************Experiment Start********************
|2025-01-19 00:03:53| Round=1 BestEpoch= 75 Acc=0.9346 F1=0.7364 Precision=0.7420 Recall=0.7312 Training_time=226.5 s 

|2025-01-19 00:03:53| ********************Experiment Results:********************
|2025-01-19 00:03:53| Acc: 0.9346 ± 0.0000
|2025-01-19 00:03:53| F1: 0.7364 ± 0.0000
|2025-01-19 00:03:53| P: 0.7420 ± 0.0000
|2025-01-19 00:03:53| Recall: 0.7312 ± 0.0000
|2025-01-19 00:03:53| train_time: 226.5060 ± 0.0000
|2025-01-19 00:03:53| Flops: 1444242432
|2025-01-19 00:03:53| Params: 1058565
|2025-01-19 00:03:53| Inference time: 1.80 ms
|2025-01-19 00:03:53| ********************Experiment Success********************
```

