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

2.Download sub-optimal dataset from [website](https://drive.google.com/drive/folders/1mKcCoMoGKV6R7p8MQBpXLSGXP62PmxSf). Follow the instructions in Data-Preprocessing folder to obtain data in .jsonl format.

### Experiments
We conducted four experiments for Code Summarization in RQ3, in order to test the generalization ability of the datasets. The three sub-folders corresponds to the experiments on the two datasets as well as on the combination of them.

### Fine-tune and Evaluation
CodeBERT for example:
```shell
cd codebert
./run.sh
./eval.sh
```

The model files and result files are saved in `./codebert/saved_models` folder.

To change the dataset for training/evaluation, one can modify the corresponding arguments in run.sh/eval.sh. For experiments on codet5, filenames can be changed in utils.py, get_filenames function.

### Evaluation on the Other Dataset
To evaluate the benchmark model on sub-optimal dataset:
```shell
./evaluate_benchmark_model_on_suboptimal.sh
```

To evaluate the sub-optimal model on benchmark dataset:
```shell
./evaluate_suboptimal_model_on_benchmark.sh
```