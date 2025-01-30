```python
|2025-01-19 08:22:59| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74753646bce0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 08:22:59| ********************Experiment Start********************
|2025-01-19 08:25:23| Round=1 BestEpoch=191 Acc=0.7935 F1=0.6874 Precision=0.6977 Recall=0.6849 Training_time=98.4 s 

|2025-01-19 08:27:39| Round=2 BestEpoch=174 Acc=0.7975 F1=0.6961 Precision=0.7146 Recall=0.6887 Training_time=92.2 s 

|2025-01-19 08:31:23| Round=3 BestEpoch=310 Acc=0.8041 F1=0.7058 Precision=0.7624 Recall=0.6969 Training_time=161.1 s 

|2025-01-19 08:34:39| Round=4 BestEpoch=264 Acc=0.7940 F1=0.6936 Precision=0.7115 Recall=0.6825 Training_time=138.8 s 

|2025-01-19 08:36:38| Round=5 BestEpoch=144 Acc=0.7884 F1=0.6805 Precision=0.7042 Recall=0.6705 Training_time=77.3 s 

|2025-01-19 08:36:38| ********************Experiment Results:********************
|2025-01-19 08:36:38| Acc: 0.7955 ± 0.0052
|2025-01-19 08:36:38| F1: 0.6927 ± 0.0085
|2025-01-19 08:36:38| P: 0.7181 ± 0.0229
|2025-01-19 08:36:38| Recall: 0.6847 ± 0.0086
|2025-01-19 08:36:38| train_time: 113.5602 ± 31.3002
|2025-01-19 08:36:38| Flops: 924672
|2025-01-19 08:36:38| Params: 7083
|2025-01-19 08:36:38| Inference time: 0.05 ms
|2025-01-19 08:36:39| ********************Experiment Success********************
```

