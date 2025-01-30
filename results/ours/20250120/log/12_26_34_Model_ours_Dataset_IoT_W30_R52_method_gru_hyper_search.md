```python
|2025-01-20 12:26:34| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7eac932a3440>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 4, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 12:26:34| ********************Experiment Start********************
|2025-01-20 12:51:21| Round=1 BestEpoch=185 Acc=0.9287 F1=0.8742 Precision=0.8760 Recall=0.8731 Training_time=1234.0 s 

|2025-01-20 13:04:42| Round=2 BestEpoch= 85 Acc=0.9256 F1=0.8763 Precision=0.8827 Recall=0.8720 Training_time=570.1 s 

