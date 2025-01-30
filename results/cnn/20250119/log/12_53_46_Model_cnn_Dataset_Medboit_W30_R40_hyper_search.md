```python
|2025-01-19 12:53:46| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7afdb94fa0c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:53:46| ********************Experiment Start********************
|2025-01-19 12:55:02| Round=1 BestEpoch=253 Acc=0.7160 F1=0.6169 Precision=0.6740 Recall=0.5992 Training_time=41.7 s 

|2025-01-19 12:56:12| Round=2 BestEpoch=225 Acc=0.6971 F1=0.6353 Precision=0.6404 Recall=0.6375 Training_time=37.7 s 

|2025-01-19 12:57:34| Round=3 BestEpoch=274 Acc=0.7170 F1=0.6233 Precision=0.6804 Recall=0.6012 Training_time=45.6 s 

|2025-01-19 12:58:18| Round=4 BestEpoch=130 Acc=0.6465 F1=0.5433 Precision=0.6281 Recall=0.5052 Training_time=21.7 s 

|2025-01-19 12:59:39| Round=5 BestEpoch=268 Acc=0.7507 F1=0.6900 Precision=0.7024 Recall=0.6861 Training_time=44.8 s 

|2025-01-19 12:59:39| ********************Experiment Results:********************
|2025-01-19 12:59:39| Acc: 0.7055 ± 0.0342
|2025-01-19 12:59:39| F1: 0.6218 ± 0.0470
|2025-01-19 12:59:39| P: 0.6650 ± 0.0271
|2025-01-19 12:59:39| Recall: 0.6058 ± 0.0594
|2025-01-19 12:59:39| train_time: 38.2878 ± 8.7503
|2025-01-19 12:59:39| Flops: 20321280
|2025-01-19 12:59:39| Params: 5488
|2025-01-19 12:59:39| Inference time: 0.09 ms
|2025-01-19 12:59:40| ********************Experiment Success********************
```

