```python
|2025-01-19 12:43:36| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x5ebb6f63950>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:43:36| ********************Experiment Start********************
|2025-01-19 12:43:36| Acc=0.6951 F1=0.6046 Precision=0.6538 Recall=0.5856 time=8.9 s 
|2025-01-19 12:43:36| Acc=0.7100 F1=0.6676 Precision=0.6797 Recall=0.6603 time=4.5 s 
|2025-01-19 12:43:36| Acc=0.7100 F1=0.6408 Precision=0.6621 Recall=0.6286 time=16.3 s 
|2025-01-19 12:43:37| Acc=0.7289 F1=0.6686 Precision=0.6846 Recall=0.6565 time=12.4 s 
|2025-01-19 12:43:37| Acc=0.7607 F1=0.6905 Precision=0.7001 Recall=0.6848 time=12.4 s 
|2025-01-19 12:43:37| ********************Experiment Results:********************
|2025-01-19 12:43:37| Acc: 0.7210 ± 0.0226
|2025-01-19 12:43:37| F1: 0.6544 ± 0.0295
|2025-01-19 12:43:37| P: 0.6761 ± 0.0165
|2025-01-19 12:43:37| Recall: 0.6432 ± 0.0338
|2025-01-19 12:43:37| train_time: 10.8982 ± 3.9718
|2025-01-19 12:43:37| Flops: 618496
|2025-01-19 12:43:37| Params: 4724
|2025-01-19 12:43:37| Inference time: 0.07 ms
|2025-01-19 12:43:37| ********************Experiment Success********************
```

