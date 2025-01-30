```python
|2025-01-25 19:29:11| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7c83e00a7410>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-25 19:29:11| ********************Experiment Start********************
|2025-01-25 19:36:04| Round=1 BestEpoch=136 Acc=0.6577 F1=0.5973 Precision=0.6170 Recall=0.5869 Training_time=28.8 s 

|2025-01-25 19:36:46| Round=2 BestEpoch= 75 Acc=0.6913 F1=0.6233 Precision=0.6308 Recall=0.6270 Training_time=15.9 s 

|2025-01-25 19:36:46| ********************Experiment Results:********************
|2025-01-25 19:36:46| Acc: 0.6745 ± 0.0168
|2025-01-25 19:36:46| F1: 0.6103 ± 0.0130
|2025-01-25 19:36:46| P: 0.6239 ± 0.0069
|2025-01-25 19:36:46| Recall: 0.6070 ± 0.0201
|2025-01-25 19:36:46| train_time: 22.3493 ± 6.4621
|2025-01-25 19:36:46| Flops: 743489536
|2025-01-25 19:36:46| Params: 648334
|2025-01-25 19:36:46| Inference time: 0.95 ms
|2025-01-25 19:36:47| ********************Experiment Success********************
```

