```python
|2025-01-19 12:15:09| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7eda5fa78aa0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:15:09| ********************Experiment Start********************
|2025-01-19 12:15:57| Round=1 BestEpoch=130 Acc=0.7269 F1=0.6651 Precision=0.6670 Recall=0.6648 Training_time=24.1 s 

|2025-01-19 12:16:53| Round=2 BestEpoch=159 Acc=0.7438 F1=0.6873 Precision=0.6986 Recall=0.6794 Training_time=30.8 s 

|2025-01-19 12:17:25| Round=3 BestEpoch= 91 Acc=0.7190 F1=0.6517 Precision=0.6783 Recall=0.6325 Training_time=15.5 s 

|2025-01-19 12:17:59| Round=4 BestEpoch= 82 Acc=0.7468 F1=0.6774 Precision=0.6780 Recall=0.6831 Training_time=15.8 s 

|2025-01-19 12:18:44| Round=5 BestEpoch=123 Acc=0.7627 F1=0.6888 Precision=0.6916 Recall=0.6959 Training_time=22.7 s 

|2025-01-19 12:18:44| ********************Experiment Results:********************
|2025-01-19 12:18:44| Acc: 0.7398 ± 0.0154
|2025-01-19 12:18:44| F1: 0.6741 ± 0.0140
|2025-01-19 12:18:44| P: 0.6827 ± 0.0111
|2025-01-19 12:18:44| Recall: 0.6711 ± 0.0217
|2025-01-19 12:18:44| train_time: 21.7921 ± 5.7082
|2025-01-19 12:18:44| Flops: 80486400
|2025-01-19 12:18:44| Params: 29608
|2025-01-19 12:18:44| Inference time: 0.07 ms
|2025-01-19 12:18:46| ********************Experiment Success********************
```

