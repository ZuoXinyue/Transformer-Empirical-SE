# Data Pre-processing

## Bug Fixing
1.Download data from [website](https://github.com/TruX-DTF/DL4PatchCorrectness/blob/master/data/experiment1/Patches_train.zip).

2.preprocess.py: this file consists of three steps - converting files in .txt format into .patch format; split patches into sections; convert split patches into buggy/fixed codes.

3.shuffle.py: shuffle the order of the data.

4.split.py: split the data into train/valid/test sets.


## Code Summarization

### Suboptimal Dataset preparation
After downloading dataset from [website](https://drive.google.com/drive/folders/1mKcCoMoGKV6R7p8MQBpXLSGXP62PmxSf), use preprocess.py to obtain data in .jsonl format.

### Mix Dataset Generation
To generate the mix dataset, we combine the benchmark dataset with randomly sampled equivalent-volume sub-optimal dataset. 

1.generate.py: generate sampled sub-optimal dataset.

2.combine sampled sub-optimal datasets with the corresponding benchmark datasets.

3.shuffle.py: generate randomized train/valid/test sets.

### Mix-Half Dataset Generation
The procedures to generate the mix-half dataset is the same as generating the mix dataset, except that the sample ratios have been changed correspondingly.