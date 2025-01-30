```python
|2025-01-25 19:08:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x75672b7152b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-25 19:08:15| ********************Experiment Start********************
|2025-01-25 19:14:49| Round=1 BestEpoch= 80 Acc=0.6150 F1=0.5524 Precision=0.5517 Recall=0.5680 Training_time=17.0 s 

|2025-01-25 19:15:58| Round=2 BestEpoch=163 Acc=0.6637 F1=0.6312 Precision=0.6368 Recall=0.6428 Training_time=34.2 s 

|2025-01-25 19:15:58| ********************Experiment Results:********************
|2025-01-25 19:15:58| Acc: 0.6394 ± 0.0243
|2025-01-25 19:15:58| F1: 0.5918 ± 0.0394
|2025-01-25 19:15:58| P: 0.5943 ± 0.0425
|2025-01-25 19:15:58| Recall: 0.6054 ± 0.0374
|2025-01-25 19:15:58| train_time: 25.5907 ± 8.5915
|2025-01-25 19:15:58| Flops: 1115160576
|2025-01-25 19:15:58| Params: 971982
|2025-01-25 19:15:58| Inference time: 1.21 ms
|2025-01-25 19:15:59| ********************Experiment Success********************
```

