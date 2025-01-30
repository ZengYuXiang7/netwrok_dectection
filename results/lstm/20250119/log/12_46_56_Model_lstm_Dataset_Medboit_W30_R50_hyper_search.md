```python
|2025-01-19 12:46:56| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75d331073860>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:46:56| ********************Experiment Start********************
|2025-01-19 12:47:42| Round=1 BestEpoch=143 Acc=0.7289 F1=0.6641 Precision=0.6645 Recall=0.6642 Training_time=24.0 s 

|2025-01-19 12:48:15| Round=2 BestEpoch= 93 Acc=0.7229 F1=0.6671 Precision=0.6903 Recall=0.6547 Training_time=15.3 s 

|2025-01-19 12:48:44| Round=3 BestEpoch= 78 Acc=0.7170 F1=0.6695 Precision=0.6776 Recall=0.6758 Training_time=13.3 s 

|2025-01-19 12:49:24| Round=4 BestEpoch=116 Acc=0.7527 F1=0.6967 Precision=0.7046 Recall=0.6902 Training_time=19.9 s 

|2025-01-19 12:50:06| Round=5 BestEpoch=128 Acc=0.7527 F1=0.6756 Precision=0.6637 Recall=0.6952 Training_time=21.4 s 

|2025-01-19 12:50:06| ********************Experiment Results:********************
|2025-01-19 12:50:06| Acc: 0.7349 ± 0.0151
|2025-01-19 12:50:06| F1: 0.6746 ± 0.0117
|2025-01-19 12:50:06| P: 0.6801 ± 0.0156
|2025-01-19 12:50:06| Recall: 0.6760 ± 0.0152
|2025-01-19 12:50:06| train_time: 18.7745 ± 3.9128
|2025-01-19 12:50:06| Flops: 123648000
|2025-01-19 12:50:06| Params: 43008
|2025-01-19 12:50:06| Inference time: 0.07 ms
|2025-01-19 12:50:07| ********************Experiment Success********************
```

