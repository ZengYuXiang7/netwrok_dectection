```python
|2025-01-27 20:14:44| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'dimension': None, 'epochs': 500,
     'eval_set': True, 'experiment': False, 'flow_length_limit': 30, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x75bdbfaae1b0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': ML, 'n_heads': 4, 'num_classes': 21, 'num_layers': 2,
     'optim': AdamW, 'path': ./datasets/, 'patience': 50, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'seq_method': gru, 'time_interval': 10, 'train_size': 500,
     'try_exp': 1, 'verbose': 1,
}
|2025-01-27 20:14:44| TestConfig(classification=True, num_classes=21, Ablation=0, try_exp=1, bs=128, lr=0.001, decay=0.0001, loss_func='CrossEntropyLoss', optim='AdamW', path='./datasets/', dataset='IoT', train_size=500, density=0.8, eval_set=True, time_interval=10, logger='None', model='ML', rank=64, retrain=False, seed=0, rounds=5, epochs=500, patience=50, verbose=1, device='cuda', debug=False, experiment=False, program_test=False, record=True, hyper_search=False, continue_train=False, flow_length_limit=30, seq_method='gru', bidirectional=True, num_layers=2, n_heads=4)
|2025-01-27 20:14:44| ********************Experiment Start********************
