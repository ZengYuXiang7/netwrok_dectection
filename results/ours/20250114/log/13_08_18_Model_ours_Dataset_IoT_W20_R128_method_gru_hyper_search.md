```python
|2025-01-14 13:08:18| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7705ad98a420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 4, 'verbose': 10,
}
|2025-01-14 13:08:18| ********************Experiment Start********************
|2025-01-14 13:24:10| Round=1 BestEpoch=165 Acc=0.9216 F1=0.8830 Precision=0.8825 Recall=0.8839 Training_time=724.0 s 

|2025-01-14 13:25:35| ********************Experiment Results:********************
|2025-01-14 13:25:35| Acc: 0.9216 ± 0.0000
|2025-01-14 13:25:35| F1: 0.8830 ± 0.0000
|2025-01-14 13:25:35| P: 0.8825 ± 0.0000
|2025-01-14 13:25:35| Recall: 0.8839 ± 0.0000
|2025-01-14 13:25:35| train_time: 724.0465 ± 0.0000
