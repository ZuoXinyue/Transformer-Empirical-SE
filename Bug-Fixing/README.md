# CodeXGLUE -- Bug Fixing (Code Refinement)

## Task Definition

Bug Fixing aims to fix buggy programs automatically.

## Dataset

We use the dataset provided by Tufano et al.(https://arxiv.org/pdf/1812.08693.pdf) as the benchmark dataset. The source side is a Java function with bugs and the target side is the fixed one. Their dataset contains two subsets (i.e.small and medium) based on the function length.

Our frequent dataset consists of 5 sub-datasets, including Defects4J, which is the most widely used dataset for bug fixing in the literature apart from the benchmark dataset. It is based on patches for buggy programs.

### Download and Preprocess
1.Download benchmark dataset from [website](https://sites.google.com/view/learning-fixes)

2.Download frequent dataset from [website](https://github.com/TruX-DTF/DL4PatchCorrectness/blob/master/data/experiment1/Patches_train.zip). Then, follow the instructions in Data-Preprocessing folder to obtain final data.

### Experiments

### Fine-tune and Evaluation (RQ2)
CodeBERT for example:
```shell
cd Benchmark-Experiments/codebert
./run_medium.sh
./eval.sh
```

The model files and result files are saved in `./codebert/saved_models` folder.
The resource consumption (RQ4) is recorded in the log files.

To change the dataset for training/evaluation, one can modify the corresponding arguments in run.sh/eval.sh. For experiments on codet5, filenames can be changed in utils.py, get_filenames function.

### Evaluation on the Other Dataset (RQ3)
We conducted two experiments for Bug Fixing in RQ3, in order to test the generalization ability of the datasets. The two sub-folders corresponds to the experiments for the two datasets. (Fine-tuned frequent model can be obtained with "Frequent-Experiments/codebert/run.sh", etc.)

To evaluate the benchmark model on frequent dataset:
```shell
./evaluate_benchmark_model_on_frequent.sh
```

To evaluate the frequent model on benchmark dataset:
```shell
./evaluate_frequent_model_on_benchmark.sh
```