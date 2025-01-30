```python
|2025-01-20 17:00:06| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e70e71b2600>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 17:00:06| ********************Experiment Start********************
|2025-01-20 17:15:55| Round=1 BestEpoch=190 Acc=0.9263 F1=0.8708 Precision=0.8785 Recall=0.8652 Training_time=714.7 s 

|2025-01-20 17:26:42| Round=2 BestEpoch=113 Acc=0.9253 F1=0.8786 Precision=0.8863 Recall=0.8741 Training_time=425.8 s 

|2025-01-20 17:26:42| ********************Experiment Results:********************
|2025-01-20 17:26:42| Acc: 0.9258 ± 0.0005
|2025-01-20 17:26:42| F1: 0.8747 ± 0.0039
|2025-01-20 17:26:42| P: 0.8824 ± 0.0039
|2025-01-20 17:26:42| Recall: 0.8696 ± 0.0045
|2025-01-20 17:26:42| train_time: 570.2749 ± 144.4282
|2025-01-20 17:26:42| Flops: 1115185152
|2025-01-20 17:26:42| Params: 972309
|2025-01-20 17:26:42| Inference time: 1.16 ms
|2025-01-20 17:26:42| ********************Experiment Success********************
```

