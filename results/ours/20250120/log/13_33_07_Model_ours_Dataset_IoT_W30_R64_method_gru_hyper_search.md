```python
|2025-01-20 13:33:07| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74a6cbaaa4b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 13:33:07| ********************Experiment Start********************
|2025-01-20 13:40:10| Round=1 BestEpoch=145 Acc=0.9224 F1=0.8647 Precision=0.8684 Recall=0.8623 Training_time=327.7 s 

|2025-01-20 13:47:58| Round=2 BestEpoch=161 Acc=0.9208 F1=0.8680 Precision=0.8755 Recall=0.8640 Training_time=367.2 s 

|2025-01-20 13:47:58| ********************Experiment Results:********************
|2025-01-20 13:47:58| Acc: 0.9216 ± 0.0008
|2025-01-20 13:47:58| F1: 0.8663 ± 0.0017
|2025-01-20 13:47:58| P: 0.8719 ± 0.0035
|2025-01-20 13:47:58| Recall: 0.8631 ± 0.0009
|2025-01-20 13:47:58| train_time: 347.4226 ± 19.7565
|2025-01-20 13:47:58| Flops: 565665792
|2025-01-20 13:47:58| Params: 548565
|2025-01-20 13:47:58| Inference time: 0.74 ms
|2025-01-20 13:47:59| ********************Experiment Success********************
```

