```python
|2025-01-20 03:56:29| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70b9a4f23980>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 03:56:29| ********************Experiment Start********************
|2025-01-20 04:09:35| Round=1 BestEpoch=170 Acc=0.9268 F1=0.8707 Precision=0.8730 Recall=0.8693 Training_time=635.5 s 

|2025-01-20 04:18:43| Round=2 BestEpoch=109 Acc=0.9115 F1=0.8652 Precision=0.8733 Recall=0.8631 Training_time=408.7 s 

|2025-01-20 04:27:09| Round=3 BestEpoch= 98 Acc=0.9194 F1=0.8619 Precision=0.8660 Recall=0.8588 Training_time=368.1 s 

|2025-01-20 04:35:19| Round=4 BestEpoch= 94 Acc=0.9225 F1=0.8690 Precision=0.8755 Recall=0.8675 Training_time=352.8 s 

|2025-01-20 04:45:53| Round=5 BestEpoch=130 Acc=0.9190 F1=0.8613 Precision=0.8662 Recall=0.8577 Training_time=489.4 s 

|2025-01-20 04:45:53| ********************Experiment Results:********************
|2025-01-20 04:45:53| Acc: 0.9199 ± 0.0050
|2025-01-20 04:45:53| F1: 0.8656 ± 0.0038
|2025-01-20 04:45:53| P: 0.8708 ± 0.0039
|2025-01-20 04:45:53| Recall: 0.8633 ± 0.0046
|2025-01-20 04:45:53| train_time: 450.8941 ± 103.7352
|2025-01-20 04:45:54| Flops: 740752896
|2025-01-20 04:45:54| Params: 643989
|2025-01-20 04:45:54| Inference time: 1.17 ms
|2025-01-20 04:45:55| ********************Experiment Success********************
```

