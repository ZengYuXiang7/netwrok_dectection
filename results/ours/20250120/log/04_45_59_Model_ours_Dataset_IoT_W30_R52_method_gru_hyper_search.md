```python
|2025-01-20 04:45:59| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76f487033680>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 3, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 04:45:59| ********************Experiment Start********************
|2025-01-20 05:04:01| Round=1 BestEpoch=170 Acc=0.9338 F1=0.8818 Precision=0.8841 Recall=0.8803 Training_time=882.8 s 

|2025-01-20 05:18:27| Round=2 BestEpoch=129 Acc=0.8244 F1=0.7912 Precision=0.8338 Recall=0.7701 Training_time=672.9 s 

|2025-01-20 05:37:03| Round=3 BestEpoch=175 Acc=0.7484 F1=0.6633 Precision=0.7094 Recall=0.6444 Training_time=913.6 s 

|2025-01-20 05:51:13| Round=4 BestEpoch=126 Acc=0.9230 F1=0.8662 Precision=0.8689 Recall=0.8640 Training_time=658.9 s 

|2025-01-20 06:06:24| Round=5 BestEpoch=137 Acc=0.9211 F1=0.8623 Precision=0.8703 Recall=0.8564 Training_time=716.1 s 

|2025-01-20 06:06:24| ********************Experiment Results:********************
|2025-01-20 06:06:24| Acc: 0.8701 ± 0.0726
|2025-01-20 06:06:24| F1: 0.8129 ± 0.0811
|2025-01-20 06:06:24| P: 0.8333 ± 0.0641
|2025-01-20 06:06:24| Recall: 0.8030 ± 0.0881
|2025-01-20 06:06:24| train_time: 768.8505 ± 107.7237
|2025-01-20 06:06:24| Flops: 1105767936
|2025-01-20 06:06:24| Params: 924633
|2025-01-20 06:06:24| Inference time: 1.56 ms
|2025-01-20 06:06:25| ********************Experiment Success********************
```

