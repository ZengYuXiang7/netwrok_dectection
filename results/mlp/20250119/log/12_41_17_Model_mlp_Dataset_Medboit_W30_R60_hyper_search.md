```python
|2025-01-19 12:41:17| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b22b0c09c40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:41:17| ********************Experiment Start********************
|2025-01-19 12:41:39| Round=1 BestEpoch= 57 Acc=0.6902 F1=0.5258 Precision=0.5320 Recall=0.5261 Training_time=8.4 s 

|2025-01-19 12:42:08| Round=2 BestEpoch= 91 Acc=0.7299 F1=0.6753 Precision=0.6820 Recall=0.6703 Training_time=13.4 s 

|2025-01-19 12:42:43| Round=3 BestEpoch=114 Acc=0.7061 F1=0.6418 Precision=0.6658 Recall=0.6245 Training_time=16.9 s 

|2025-01-19 12:43:05| Round=4 BestEpoch= 59 Acc=0.7279 F1=0.6639 Precision=0.6811 Recall=0.6522 Training_time=8.8 s 

|2025-01-19 12:43:32| Round=5 BestEpoch= 80 Acc=0.7458 F1=0.6802 Precision=0.6743 Recall=0.6877 Training_time=12.2 s 

|2025-01-19 12:43:32| ********************Experiment Results:********************
|2025-01-19 12:43:32| Acc: 0.7200 ± 0.0195
|2025-01-19 12:43:32| F1: 0.6374 ± 0.0573
|2025-01-19 12:43:32| P: 0.6471 ± 0.0578
|2025-01-19 12:43:32| Recall: 0.6322 ± 0.0570
|2025-01-19 12:43:32| train_time: 11.9389 ± 3.1428
|2025-01-19 12:43:32| Flops: 818176
|2025-01-19 12:43:32| Params: 6264
|2025-01-19 12:43:32| Inference time: 0.05 ms
|2025-01-19 12:43:33| ********************Experiment Success********************
```

