```python
|2025-01-20 13:48:01| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x760bf52e4890>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 13:48:01| ********************Experiment Start********************
|2025-01-20 13:54:53| Round=1 BestEpoch=138 Acc=0.8039 F1=0.7250 Precision=0.7535 Recall=0.7126 Training_time=314.5 s 

|2025-01-20 13:59:51| Round=2 BestEpoch= 90 Acc=0.7411 F1=0.6584 Precision=0.6940 Recall=0.6393 Training_time=207.0 s 

|2025-01-20 13:59:51| ********************Experiment Results:********************
|2025-01-20 13:59:51| Acc: 0.7725 ± 0.0314
|2025-01-20 13:59:51| F1: 0.6917 ± 0.0333
|2025-01-20 13:59:51| P: 0.7238 ± 0.0298
|2025-01-20 13:59:51| Recall: 0.6760 ± 0.0366
|2025-01-20 13:59:51| train_time: 260.7367 ± 53.7620
|2025-01-20 13:59:51| Flops: 2232336384
|2025-01-20 13:59:51| Params: 2178453
|2025-01-20 13:59:51| Inference time: 0.73 ms
|2025-01-20 13:59:51| ********************Experiment Success********************
```

