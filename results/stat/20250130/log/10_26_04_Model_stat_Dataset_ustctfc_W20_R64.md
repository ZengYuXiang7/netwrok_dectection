```python
|2025-01-30 10:26:04| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xea8006a0920>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 10:26:04| ********************Experiment Start********************
|2025-01-30 10:28:20| Round=1 BestEpoch= 74 Ac=0.9579 Pr=0.3201 Rc=0.3164 F1=0.3137 Training_time=25.4 s 

|2025-01-30 10:29:11| Round=2 BestEpoch= 81 Ac=0.9620 Pr=0.3456 Rc=0.3321 F1=0.3311 Training_time=28.1 s 

|2025-01-30 10:29:53| Round=3 BestEpoch= 61 Ac=0.9599 Pr=0.3502 Rc=0.3284 F1=0.3239 Training_time=21.1 s 

|2025-01-30 10:30:33| Round=4 BestEpoch= 56 Ac=0.9585 Pr=0.3760 Rc=0.3736 F1=0.3597 Training_time=19.5 s 

|2025-01-30 10:31:14| Round=5 BestEpoch= 59 Ac=0.9524 Pr=0.5013 Rc=0.3796 F1=0.4055 Training_time=20.9 s 

|2025-01-30 10:31:14| ********************Experiment Results:********************
|2025-01-30 10:31:14| AC: 0.9581 ± 0.0032
|2025-01-30 10:31:14| PR: 0.3786 ± 0.0638
|2025-01-30 10:31:14| RC: 0.3460 ± 0.0256
|2025-01-30 10:31:14| F1: 0.3468 ± 0.0331
|2025-01-30 10:31:14| train_time: 22.9955 ± 3.2163
|2025-01-30 10:31:15| Flops: 258816
|2025-01-30 10:31:15| Params: 3961
|2025-01-30 10:31:15| Inference time: 0.04 ms
|2025-01-30 10:31:16| ********************Experiment Success********************
```

