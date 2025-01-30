```python
|2025-01-19 12:59:43| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7db9957978c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:59:43| ********************Experiment Start********************
|2025-01-19 13:01:06| Round=1 BestEpoch=270 Acc=0.6981 F1=0.5906 Precision=0.6650 Recall=0.5727 Training_time=45.9 s 

|2025-01-19 13:01:51| Round=2 BestEpoch=129 Acc=0.6941 F1=0.6260 Precision=0.6643 Recall=0.6163 Training_time=22.2 s 

|2025-01-19 13:02:49| Round=3 BestEpoch=172 Acc=0.7041 F1=0.5819 Precision=0.6636 Recall=0.5623 Training_time=30.1 s 

|2025-01-19 13:04:15| Round=4 BestEpoch=279 Acc=0.7259 F1=0.6415 Precision=0.6908 Recall=0.6170 Training_time=48.0 s 

|2025-01-19 13:05:04| Round=5 BestEpoch=143 Acc=0.7120 F1=0.6650 Precision=0.6727 Recall=0.6618 Training_time=24.6 s 

|2025-01-19 13:05:04| ********************Experiment Results:********************
|2025-01-19 13:05:04| Acc: 0.7069 ± 0.0113
|2025-01-19 13:05:04| F1: 0.6210 ± 0.0311
|2025-01-19 13:05:04| P: 0.6713 ± 0.0103
|2025-01-19 13:05:04| Recall: 0.6060 ± 0.0357
|2025-01-19 13:05:04| train_time: 34.1512 ± 10.7733
|2025-01-19 13:05:04| Flops: 31161600
|2025-01-19 13:05:04| Params: 8358
|2025-01-19 13:05:04| Inference time: 0.10 ms
|2025-01-19 13:05:06| ********************Experiment Success********************
```

