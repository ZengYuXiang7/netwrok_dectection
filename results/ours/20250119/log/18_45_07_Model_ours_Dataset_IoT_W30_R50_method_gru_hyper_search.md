```python
|2025-01-19 18:45:07| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74c3d616fbf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 18:45:07| ********************Experiment Start********************
|2025-01-19 18:48:40| Round=1 BestEpoch= 89 Acc=0.9049 F1=0.8383 Precision=0.8459 Recall=0.8397 Training_time=144.6 s 

|2025-01-19 18:53:01| Round=2 BestEpoch=115 Acc=0.9054 F1=0.8419 Precision=0.8471 Recall=0.8382 Training_time=187.8 s 

|2025-01-19 18:53:01| ********************Experiment Results:********************
|2025-01-19 18:53:01| Acc: 0.9051 ± 0.0002
|2025-01-19 18:53:01| F1: 0.8401 ± 0.0018
|2025-01-19 18:53:01| P: 0.8465 ± 0.0006
|2025-01-19 18:53:01| Recall: 0.8389 ± 0.0007
|2025-01-19 18:53:01| train_time: 166.1780 ± 21.6198
|2025-01-19 18:53:01| Flops: 686668800
|2025-01-19 18:53:01| Params: 253325
|2025-01-19 18:53:01| Inference time: 0.49 ms
