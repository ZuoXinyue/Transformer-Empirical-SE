# Data Pre-processing

## Bug Fixing
1.Download data from [website](https://github.com/TruX-DTF/DL4PatchCorrectness/blob/master/data/experiment1/Patches_train.zip).

2.preprocess.py: this file consists of three steps - converting files in .txt format into .patch format; split patches into sections; convert split patches into buggy/fixed codes.

3.shuffle.py: shuffle the order of the data.

4.split.py: split the data into train/valid/test sets.


## Code Summarization

### Frequent Dataset preparation
After downloading dataset from [website](https://drive.google.com/drive/folders/1mKcCoMoGKV6R7p8MQBpXLSGXP62PmxSf), use preprocess.py to obtain data in .jsonl format.

### Mix-Bench Dataset Generation
To generate the mix-bench dataset, we combine the benchmark dataset with randomly sampled equivalent-volume frequent dataset. 

1.generate.py: generate sampled frequent dataset.

2.combine sampled frequent dataset with the corresponding benchmark dataset.

3.shuffle.py: shuffle the train/valid/test sets.

### Mix-Frequent Dataset Generation
To generate the mix-frequent dataset, we combine the frequent dataset with randomly over-sampled equivalent-volume benchmark dataset. 

1.generate.py: generate over-sampled benchmark dataset.

2.combine over-sampled benchmark dataset with the corresponding frequent dataset.

3.shuffle.py: shuffle the train/valid/test sets.