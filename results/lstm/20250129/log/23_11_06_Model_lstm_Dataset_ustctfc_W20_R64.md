```python
|2025-01-29 23:11:06| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10b79f944170>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 10,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 23:11:06| ********************Experiment Start********************
|2025-01-29 23:11:33| Round=1 BestEpoch=118 Ac=0.8900 Pr=0.4795 Rc=0.4827 F1=0.4804 Training_time=12.8 s 

|2025-01-29 23:11:58| Round=2 BestEpoch=106 Ac=0.8738 Pr=0.5340 Rc=0.5562 F1=0.5433 Training_time=11.4 s 

|2025-01-29 23:12:25| Round=3 BestEpoch=121 Ac=0.8673 Pr=0.5261 Rc=0.4669 F1=0.4787 Training_time=13.1 s 

|2025-01-29 23:12:48| Round=4 BestEpoch=100 Ac=0.8673 Pr=0.5507 Rc=0.4437 F1=0.4707 Training_time=10.8 s 

|2025-01-29 23:13:16| Round=5 BestEpoch=122 Ac=0.8608 Pr=0.4514 Rc=0.4879 F1=0.4646 Training_time=13.6 s 

|2025-01-29 23:13:47| Round=6 BestEpoch=135 Ac=0.8932 Pr=0.5114 Rc=0.5013 F1=0.5030 Training_time=14.8 s 

|2025-01-29 23:14:09| Round=7 BestEpoch= 93 Ac=0.8447 Pr=0.4958 Rc=0.4887 F1=0.4851 Training_time=10.1 s 

|2025-01-29 23:14:33| Round=8 BestEpoch=103 Ac=0.8997 Pr=0.4848 Rc=0.4636 F1=0.4698 Training_time=11.1 s 

|2025-01-29 23:14:53| Round=9 BestEpoch= 84 Ac=0.8641 Pr=0.5271 Rc=0.4643 F1=0.4782 Training_time=9.0 s 

|2025-01-29 23:15:19| Round=10 BestEpoch=109 Ac=0.8641 Pr=0.5194 Rc=0.5235 F1=0.5180 Training_time=11.7 s 

|2025-01-29 23:15:19| ********************Experiment Results:********************
|2025-01-29 23:15:19| AC: 0.8725 ± 0.0161
|2025-01-29 23:15:19| PR: 0.5080 ± 0.0284
|2025-01-29 23:15:19| RC: 0.4879 ± 0.0311
|2025-01-29 23:15:19| F1: 0.4892 ± 0.0236
|2025-01-29 23:15:19| train_time: 11.8365 ± 1.6371
|2025-01-29 23:15:19| Flops: 134676480
|2025-01-29 23:15:19| Params: 73490
|2025-01-29 23:15:19| Inference time: 0.07 ms
|2025-01-29 23:15:21| ********************Experiment Success********************
```

