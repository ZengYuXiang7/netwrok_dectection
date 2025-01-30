```python
|2025-01-19 12:39:07| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70ed583dc2c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:39:07| ********************Experiment Start********************
|2025-01-19 12:39:29| Round=1 BestEpoch= 61 Acc=0.6951 F1=0.6046 Precision=0.6538 Recall=0.5856 Training_time=8.9 s 

|2025-01-19 12:39:44| Round=2 BestEpoch= 31 Acc=0.7100 F1=0.6676 Precision=0.6797 Recall=0.6603 Training_time=4.5 s 

|2025-01-19 12:40:18| Round=3 BestEpoch=110 Acc=0.7100 F1=0.6408 Precision=0.6621 Recall=0.6286 Training_time=16.3 s 

|2025-01-19 12:40:46| Round=4 BestEpoch= 83 Acc=0.7289 F1=0.6686 Precision=0.6846 Recall=0.6565 Training_time=12.4 s 

|2025-01-19 12:41:14| Round=5 BestEpoch= 83 Acc=0.7607 F1=0.6905 Precision=0.7001 Recall=0.6848 Training_time=12.4 s 

|2025-01-19 12:41:14| ********************Experiment Results:********************
|2025-01-19 12:41:14| Acc: 0.7210 ± 0.0226
|2025-01-19 12:41:14| F1: 0.6544 ± 0.0295
|2025-01-19 12:41:14| P: 0.6761 ± 0.0165
|2025-01-19 12:41:14| Recall: 0.6432 ± 0.0338
|2025-01-19 12:41:14| train_time: 10.8982 ± 3.9718
|2025-01-19 12:41:14| Flops: 618496
|2025-01-19 12:41:14| Params: 4724
|2025-01-19 12:41:14| Inference time: 0.05 ms
|2025-01-19 12:41:15| ********************Experiment Success********************
```

