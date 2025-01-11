```python
|2025-01-09 17:19:08| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7becf12deea0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:19:08| ********************Experiment Start********************
|2025-01-09 17:30:22| Round=1 BestEpoch=450 Acc=0.7735 F1=0.6702 Precision=0.7218 Recall=0.6430 Training_time=519.9 s 

|2025-01-09 17:30:22| ********************Experiment Results:********************
|2025-01-09 17:30:22| Acc: 0.7735 ± 0.0000
|2025-01-09 17:30:22| F1: 0.6702 ± 0.0000
|2025-01-09 17:30:22| P: 0.7218 ± 0.0000
|2025-01-09 17:30:22| Recall: 0.6430 ± 0.0000
|2025-01-09 17:30:22| train_time: 519.9101 ± 0.0000
|2025-01-09 17:30:22| Flops: 4691200
|2025-01-09 17:30:22| Params: 35871
|2025-01-09 17:30:22| Inference time: 0.06 ms
|2025-01-09 17:30:23| ********************Experiment Success********************
```

