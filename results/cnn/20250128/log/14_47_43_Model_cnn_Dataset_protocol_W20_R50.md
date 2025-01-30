```python
|2025-01-28 14:47:43| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7af62bc6a20>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:47:43| ********************Experiment Start********************
|2025-01-28 14:48:33| Round=1 BestEpoch=205 Ac=0.5618 Pr=0.5002 Rc=0.4825 F1=0.4742 Training_time=23.0 s 

|2025-01-28 14:49:08| Round=2 BestEpoch=137 Ac=0.5689 Pr=0.5060 Rc=0.4562 F1=0.4516 Training_time=15.1 s 

|2025-01-28 14:49:08| ********************Experiment Results:********************
|2025-01-28 14:49:08| AC: 0.5654 ± 0.0035
|2025-01-28 14:49:08| PR: 0.5031 ± 0.0029
|2025-01-28 14:49:08| RC: 0.4694 ± 0.0131
|2025-01-28 14:49:08| F1: 0.4629 ± 0.0113
|2025-01-28 14:49:08| train_time: 19.0443 ± 3.9720
|2025-01-28 14:49:08| Flops: 20915200
|2025-01-28 14:49:08| Params: 9327
|2025-01-28 14:49:08| Inference time: 0.09 ms
|2025-01-28 14:49:09| ********************Experiment Success********************
```

