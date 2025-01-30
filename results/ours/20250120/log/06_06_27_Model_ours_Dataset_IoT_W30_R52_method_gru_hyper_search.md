```python
|2025-01-20 06:06:27| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75994f215010>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 2, 'num_classes': 21, 'num_layers': 3, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 06:06:27| ********************Experiment Start********************
|2025-01-20 06:20:21| Round=1 BestEpoch=122 Acc=0.8864 F1=0.8209 Precision=0.8485 Recall=0.8134 Training_time=642.1 s 

|2025-01-20 06:37:53| Round=2 BestEpoch=161 Acc=0.7417 F1=0.6608 Precision=0.6954 Recall=0.6467 Training_time=851.2 s 

|2025-01-20 06:51:18| Round=3 BestEpoch=116 Acc=0.9235 F1=0.8679 Precision=0.8708 Recall=0.8668 Training_time=612.7 s 

|2025-01-20 07:12:11| Round=4 BestEpoch=197 Acc=0.9168 F1=0.8584 Precision=0.8602 Recall=0.8574 Training_time=1042.7 s 

|2025-01-20 07:26:10| Round=5 BestEpoch=122 Acc=0.9003 F1=0.8486 Precision=0.8649 Recall=0.8401 Training_time=645.5 s 

|2025-01-20 07:26:10| ********************Experiment Results:********************
|2025-01-20 07:26:10| Acc: 0.8737 ± 0.0673
|2025-01-20 07:26:10| F1: 0.8113 ± 0.0769
|2025-01-20 07:26:10| P: 0.8280 ± 0.0667
|2025-01-20 07:26:10| Recall: 0.8049 ± 0.0812
|2025-01-20 07:26:10| train_time: 758.8402 ± 165.5079
|2025-01-20 07:26:10| Flops: 1105767936
|2025-01-20 07:26:10| Params: 924633
|2025-01-20 07:26:10| Inference time: 1.64 ms
|2025-01-20 07:26:12| ********************Experiment Success********************
```

