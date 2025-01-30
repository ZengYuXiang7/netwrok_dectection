```python
|2025-01-19 12:50:09| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f7e1e04ab70>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:50:09| ********************Experiment Start********************
|2025-01-19 12:51:07| Round=1 BestEpoch=187 Acc=0.7408 F1=0.6741 Precision=0.6757 Recall=0.6733 Training_time=31.0 s 

|2025-01-19 12:51:34| Round=2 BestEpoch= 74 Acc=0.7378 F1=0.6733 Precision=0.6822 Recall=0.6756 Training_time=12.3 s 

|2025-01-19 12:52:08| Round=3 BestEpoch= 96 Acc=0.7329 F1=0.6812 Precision=0.6830 Recall=0.6814 Training_time=16.0 s 

|2025-01-19 12:53:03| Round=4 BestEpoch=173 Acc=0.7468 F1=0.6860 Precision=0.6917 Recall=0.6820 Training_time=29.5 s 

|2025-01-19 12:53:39| Round=5 BestEpoch=105 Acc=0.7716 F1=0.6953 Precision=0.6893 Recall=0.7066 Training_time=17.7 s 

|2025-01-19 12:53:39| ********************Experiment Results:********************
|2025-01-19 12:53:39| Acc: 0.7460 ± 0.0136
|2025-01-19 12:53:39| F1: 0.6820 ± 0.0082
|2025-01-19 12:53:39| P: 0.6844 ± 0.0057
|2025-01-19 12:53:39| Recall: 0.6838 ± 0.0119
|2025-01-19 12:53:39| train_time: 21.3011 ± 7.5266
|2025-01-19 12:53:39| Flops: 176025600
|2025-01-19 12:53:39| Params: 58808
|2025-01-19 12:53:39| Inference time: 0.07 ms
|2025-01-19 12:53:40| ********************Experiment Success********************
```

