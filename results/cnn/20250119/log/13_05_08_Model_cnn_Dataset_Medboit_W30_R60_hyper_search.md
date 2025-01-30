```python
|2025-01-19 13:05:08| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79fa08bbab70>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 13:05:08| ********************Experiment Start********************
|2025-01-19 13:06:29| Round=1 BestEpoch=270 Acc=0.7150 F1=0.6084 Precision=0.6432 Recall=0.5953 Training_time=44.9 s 

|2025-01-19 13:07:32| Round=2 BestEpoch=200 Acc=0.7378 F1=0.6865 Precision=0.6934 Recall=0.6850 Training_time=33.5 s 

|2025-01-19 13:08:32| Round=3 BestEpoch=191 Acc=0.7358 F1=0.6381 Precision=0.6875 Recall=0.6272 Training_time=31.9 s 

|2025-01-19 13:09:15| Round=4 BestEpoch=127 Acc=0.6832 F1=0.5904 Precision=0.6606 Recall=0.5649 Training_time=21.0 s 

|2025-01-19 13:10:40| Round=5 BestEpoch=286 Acc=0.7577 F1=0.6940 Precision=0.7094 Recall=0.6888 Training_time=47.4 s 

|2025-01-19 13:10:40| ********************Experiment Results:********************
|2025-01-19 13:10:40| Acc: 0.7259 ± 0.0253
|2025-01-19 13:10:40| F1: 0.6435 ± 0.0412
|2025-01-19 13:10:40| P: 0.6788 ± 0.0238
|2025-01-19 13:10:40| Recall: 0.6322 ± 0.0488
|2025-01-19 13:10:40| train_time: 35.7272 ± 9.5377
|2025-01-19 13:10:40| Flops: 44305920
|2025-01-19 13:10:40| Params: 11828
|2025-01-19 13:10:40| Inference time: 0.09 ms
|2025-01-19 13:10:42| ********************Experiment Success********************
```

