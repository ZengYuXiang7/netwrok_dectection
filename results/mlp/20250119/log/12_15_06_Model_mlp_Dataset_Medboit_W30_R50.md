```python
|2025-01-19 12:15:06| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x146dde826cf0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:15:06| ********************Experiment Start********************
|2025-01-19 12:15:06| Acc=0.6951 F1=0.6046 Precision=0.6538 Recall=0.5856 time=9.5 s 
|2025-01-19 12:15:07| Acc=0.7100 F1=0.6676 Precision=0.6797 Recall=0.6603 time=4.8 s 
|2025-01-19 12:15:07| Acc=0.7100 F1=0.6408 Precision=0.6621 Recall=0.6286 time=16.8 s 
|2025-01-19 12:15:07| Acc=0.7289 F1=0.6686 Precision=0.6846 Recall=0.6565 time=12.9 s 
|2025-01-19 12:15:07| Acc=0.7607 F1=0.6905 Precision=0.7001 Recall=0.6848 time=12.9 s 
|2025-01-19 12:15:07| ********************Experiment Results:********************
|2025-01-19 12:15:07| Acc: 0.7210 ± 0.0226
|2025-01-19 12:15:07| F1: 0.6544 ± 0.0295
|2025-01-19 12:15:07| P: 0.6761 ± 0.0165
|2025-01-19 12:15:07| Recall: 0.6432 ± 0.0338
|2025-01-19 12:15:07| train_time: 11.3551 ± 4.0366
|2025-01-19 12:15:07| Flops: 618496
|2025-01-19 12:15:07| Params: 4724
|2025-01-19 12:15:07| Inference time: 0.08 ms
|2025-01-19 12:15:07| ********************Experiment Success********************
```

