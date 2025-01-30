```python
|2025-01-29 22:10:52| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf21b0c53ce0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:10:52| ********************Experiment Start********************
|2025-01-29 22:11:00| Round=1 BestEpoch= 19 Ac=0.8608 Pr=0.4990 Rc=0.4468 F1=0.4641 Training_time=2.0 s 

|2025-01-29 22:11:10| Round=2 BestEpoch= 29 Ac=0.8252 Pr=0.5354 Rc=0.4472 F1=0.4723 Training_time=2.9 s 

