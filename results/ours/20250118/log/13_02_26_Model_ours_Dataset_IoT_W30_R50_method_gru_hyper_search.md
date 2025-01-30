```python
|2025-01-18 13:02:26| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x776082e6a150>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 50, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 13:02:26| ********************Experiment Start********************
|2025-01-18 13:10:39| Round=1 BestEpoch= 70 Acc=0.8943 F1=0.8280 Precision=0.8301 Recall=0.8274 Training_time=273.3 s 

|2025-01-18 13:10:39| ********************Experiment Results:********************
|2025-01-18 13:10:39| Acc: 0.8943 ± 0.0000
|2025-01-18 13:10:39| F1: 0.8280 ± 0.0000
|2025-01-18 13:10:39| P: 0.8301 ± 0.0000
|2025-01-18 13:10:39| Recall: 0.8274 ± 0.0000
|2025-01-18 13:10:39| train_time: 273.3417 ± 0.0000
|2025-01-18 13:10:39| Flops: 1166227200
|2025-01-18 13:10:39| Params: 652275
|2025-01-18 13:10:39| Inference time: 1.09 ms
|2025-01-18 13:10:39| ********************Experiment Success********************
```

