# CodeXGLUE -- Code-To-Text

## Task Definition

Code Summarization generates a natural language summary for a code snippet to aid programmers’ understanding.

## Dataset

We use the java subset of the [CodeSearchNet](https://arxiv.org/pdf/1909.09436.pdf) dataset as the benchmark dataset. But the code is applicable to other languages as well.

### Download and preprocess
1.The relevant files for the benchmark dataset can be downloaded from this [website](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text).

```shell
unzip dataset.zip
cd dataset
wget https://zenodo.org/record/7857872/files/java.zip

unzip java.zip
rm *.zip
rm *.pkl

python preprocess.py
rm -r */final
cd ..
```

2.Download frequent dataset from [website](https://drive.google.com/drive/folders/1mKcCoMoGKV6R7p8MQBpXLSGXP62PmxSf). Follow the instructions in Data-Preprocessing folder to obtain data in .jsonl format.

### Experiments

### Fine-tune and Evaluation (RQ2)
CodeBERT for example:
```shell
cd codebert
./run.sh
./eval.sh
```

The model files and result files are saved in `./codebert/saved_models` folder.
The resource consumption (RQ4) is recorded in the log files.

To change the dataset for training/evaluation, one can modify the corresponding arguments in run.sh/eval.sh. For experiments on codet5, filenames can be changed in utils.py, get_filenames function.

### Evaluation on the Other Dataset (RQ3)
We conducted four experiments for Code Summarization in RQ3, in order to test the generalization ability of the datasets. The four sub-folders corresponds to the experiments on the two datasets as well as on the combination of them.

Mix-Bench Dataset: the benchmark dataset combined with randomly sampled equivalent-volume frequent dataset

Mix-Frequent Dataset: the frequent dataset combined with randomly over-sampled equivalent-volume benchmark dataset

To evaluate the benchmark model on frequent dataset:
```shell
./evaluate_benchmark_model_on_frequent.sh
```

To evaluate the frequent model on benchmark dataset:
```shell
./evaluate_frequent_model_on_benchmark.sh
```

To evaluate the Mix-Bench model on benchmark dataset:
```shell
./evaluate_mix_bench_model_on_benchmark.sh
```

To evaluate the Mix-Frequent model on frequent dataset:
```shell
./evaluate_mix_freq_model_on_frequent.sh
```

### Results & Conclusions (RQ3)
| Code Summarization | B Model on B | F Model on B | Mix-Bench Model on B | F Model on F | B Model on F | Mix-Frequent Model on F |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| CodeBERT | 18.74/13.16/35.03 | 8.70/5.29/14.46 | 19.31/13.25/35.73 | 32.20/20.52/42.17 | 17.61/12.87/25.75 | 31.23/19.77/41.02 |
| CodeGPT | 14.15/15.89/33.23 | 2.70/1.91/7.81 | 13.92/15.41/32.80 | 31.97/20.19/41.83 | 12.85/13.19/22.89 | 31.59/19.89/41.55 |
| CodeT5 | 20.20/15.06/38.2 | 12.10/8.92/21.53 | 20.52/14.51/38.08 | 32.94/22.05/44.33 | 19.24/14.25/28.35 | 31.89/21.44/43.53 |

The performance of the models trained on the Mix-Bench dataset and evaluated on the benchmark dataset is shown in the "Mix-Bench model on B" column of the table. Comparing with "B model on B", we found only CodeBERT’s BLEU-4 and ROUGE-L have been significantly improved. The improvement in CodeBERT’s METEOR and CodeT5’s BLEU-4 are insignificant. Moreover, additional training data has led to significant performance drop in CodeGPT across all metrics, and CodeT5 on METEOR. Similarly, when comparing "Mix-Frequent model on F" to "F model on F", we found a significant performance drop for all models across the three metrics except for CodeGPT on rouge. Therefore, we can conclude that including more diverse data into the training dataset does not necessarily increase model generalization ability. We thus suggest future work look into the possibility of utilizing dataset pruning/selection techniques to improve the dataset quality, which in turn will increase model generalization ability.