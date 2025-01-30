```python
|2025-01-20 16:31:56| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7cd9bf9363f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 2, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 16:31:56| ********************Experiment Start********************
|2025-01-20 16:43:14| Round=1 BestEpoch=121 Acc=0.9120 F1=0.8562 Precision=0.8626 Recall=0.8524 Training_time=455.9 s 

|2025-01-20 17:00:03| Round=2 BestEpoch=204 Acc=0.9151 F1=0.8673 Precision=0.8684 Recall=0.8668 Training_time=769.3 s 

|2025-01-20 17:00:03| ********************Experiment Results:********************
|2025-01-20 17:00:03| Acc: 0.9136 ± 0.0015
|2025-01-20 17:00:03| F1: 0.8617 ± 0.0056
|2025-01-20 17:00:03| P: 0.8655 ± 0.0029
|2025-01-20 17:00:03| Recall: 0.8596 ± 0.0072
|2025-01-20 17:00:03| train_time: 612.5997 ± 156.6861
|2025-01-20 17:00:03| Flops: 1115185152
|2025-01-20 17:00:03| Params: 972309
|2025-01-20 17:00:03| Inference time: 1.16 ms
|2025-01-20 17:00:04| ********************Experiment Success********************
```

