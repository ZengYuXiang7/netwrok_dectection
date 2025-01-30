```python
|2025-01-29 22:20:41| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x105b44bcfd40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:20:41| ********************Experiment Start********************
|2025-01-29 22:21:07| Round=1 BestEpoch=118 Ac=0.8900 Pr=0.4795 Rc=0.4827 F1=0.4804 Training_time=12.1 s 

|2025-01-29 22:21:29| Round=2 BestEpoch=106 Ac=0.8738 Pr=0.5340 Rc=0.5562 F1=0.5433 Training_time=10.4 s 

|2025-01-29 22:21:54| Round=3 BestEpoch=121 Ac=0.8673 Pr=0.5261 Rc=0.4669 F1=0.4787 Training_time=12.0 s 

|2025-01-29 22:22:15| Round=4 BestEpoch=100 Ac=0.8673 Pr=0.5507 Rc=0.4437 F1=0.4707 Training_time=9.9 s 

|2025-01-29 22:22:41| Round=5 BestEpoch=122 Ac=0.8608 Pr=0.4514 Rc=0.4879 F1=0.4646 Training_time=12.6 s 

|2025-01-29 22:22:41| ********************Experiment Results:********************
|2025-01-29 22:22:41| AC: 0.8718 ± 0.0099
|2025-01-29 22:22:41| PR: 0.5084 ± 0.0370
|2025-01-29 22:22:41| RC: 0.4875 ± 0.0376
|2025-01-29 22:22:41| F1: 0.4875 ± 0.0284
|2025-01-29 22:22:41| train_time: 11.4096 ± 1.0540
|2025-01-29 22:22:41| Flops: 134676480
|2025-01-29 22:22:41| Params: 73490
|2025-01-29 22:22:41| Inference time: 0.07 ms
|2025-01-29 22:22:43| ********************Experiment Success********************
```

