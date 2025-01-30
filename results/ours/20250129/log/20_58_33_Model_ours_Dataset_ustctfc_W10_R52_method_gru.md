```python
|2025-01-29 20:58:33| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa1d255d6e40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:58:33| ********************Experiment Start********************
|2025-01-29 21:00:51| Round=1 BestEpoch=  3 Ac=0.9827 Pr=0.7775 Rc=0.7556 F1=0.7618 Training_time=2.7 s 

|2025-01-29 21:02:39| Round=2 BestEpoch= 60 Ac=0.9872 Pr=0.7717 Rc=0.7050 F1=0.7170 Training_time=50.7 s 

|2025-01-29 21:02:39| ********************Experiment Results:********************
|2025-01-29 21:02:39| AC: 0.9849 ± 0.0023
|2025-01-29 21:02:39| PR: 0.7746 ± 0.0029
|2025-01-29 21:02:39| RC: 0.7303 ± 0.0253
|2025-01-29 21:02:39| F1: 0.7394 ± 0.0224
|2025-01-29 21:02:39| train_time: 26.6962 ± 24.0190
|2025-01-29 21:02:39| Flops: 247024128
|2025-01-29 21:02:39| Params: 215403
|2025-01-29 21:02:39| Inference time: 0.56 ms
|2025-01-29 21:02:40| ********************Experiment Success********************
```

