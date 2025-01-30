```python
|2025-01-19 12:08:11| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7334ec98bb00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:08:11| ********************Experiment Start********************
|2025-01-19 12:08:39| Round=1 BestEpoch= 81 Acc=0.7011 F1=0.6125 Precision=0.6591 Recall=0.5952 Training_time=12.3 s 

|2025-01-19 12:08:57| Round=2 BestEpoch= 44 Acc=0.7071 F1=0.6574 Precision=0.6673 Recall=0.6529 Training_time=6.6 s 

|2025-01-19 12:09:34| Round=3 BestEpoch=118 Acc=0.7071 F1=0.6443 Precision=0.6724 Recall=0.6235 Training_time=18.2 s 

|2025-01-19 12:10:04| Round=4 BestEpoch= 87 Acc=0.7488 F1=0.6793 Precision=0.6930 Recall=0.6675 Training_time=13.3 s 

|2025-01-19 12:10:23| Round=5 BestEpoch= 47 Acc=0.7249 F1=0.6708 Precision=0.6823 Recall=0.6619 Training_time=7.4 s 

|2025-01-19 12:10:23| ********************Experiment Results:********************
|2025-01-19 12:10:23| Acc: 0.7178 ± 0.0174
|2025-01-19 12:10:23| F1: 0.6529 ± 0.0234
|2025-01-19 12:10:23| P: 0.6748 ± 0.0118
|2025-01-19 12:10:23| Recall: 0.6402 ± 0.0271
|2025-01-19 12:10:23| train_time: 11.5534 ± 4.2215
|2025-01-19 12:10:24| Flops: 444416
|2025-01-19 12:10:24| Params: 3384
|2025-01-19 12:10:24| Inference time: 0.09 ms
|2025-01-19 12:10:25| ********************Experiment Success********************
```

