```python
|2025-01-19 12:12:43| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x728a0ebf8800>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:12:43| ********************Experiment Start********************
|2025-01-19 12:13:05| Round=1 BestEpoch= 57 Acc=0.6902 F1=0.5258 Precision=0.5320 Recall=0.5261 Training_time=8.7 s 

|2025-01-19 12:13:35| Round=2 BestEpoch= 91 Acc=0.7299 F1=0.6753 Precision=0.6820 Recall=0.6703 Training_time=13.8 s 

|2025-01-19 12:14:11| Round=3 BestEpoch=114 Acc=0.7061 F1=0.6418 Precision=0.6658 Recall=0.6245 Training_time=17.3 s 

|2025-01-19 12:14:33| Round=4 BestEpoch= 59 Acc=0.7279 F1=0.6639 Precision=0.6811 Recall=0.6522 Training_time=9.0 s 

|2025-01-19 12:15:02| Round=5 BestEpoch= 80 Acc=0.7458 F1=0.6802 Precision=0.6743 Recall=0.6877 Training_time=12.9 s 

|2025-01-19 12:15:02| ********************Experiment Results:********************
|2025-01-19 12:15:02| Acc: 0.7200 ± 0.0195
|2025-01-19 12:15:02| F1: 0.6374 ± 0.0573
|2025-01-19 12:15:02| P: 0.6471 ± 0.0578
|2025-01-19 12:15:02| Recall: 0.6322 ± 0.0570
|2025-01-19 12:15:02| train_time: 12.3467 ± 3.2086
|2025-01-19 12:15:02| Flops: 818176
|2025-01-19 12:15:02| Params: 6264
|2025-01-19 12:15:02| Inference time: 0.05 ms
|2025-01-19 12:15:04| ********************Experiment Success********************
```

