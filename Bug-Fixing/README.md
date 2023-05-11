# CodeXGLUE -- Bug Fixing (Code Refinement)

## Task Definition

Bug Fixing aims to fix buggy programs automatically.

## Dataset

We use the dataset provided by Tufano et al.(https://arxiv.org/pdf/1812.08693.pdf) as the benchmark dataset. The source side is a Java function with bugs and the target side is the fixed one. Their dataset contains two subsets (i.e.small and medium) based on the function length.

Our sub-optimal dataset consists of 5 sub-datasets, including Defects4J, which is the most widely used dataset for bug fixing in the literature apart from the benchmark dataset. It is based on patches for buggy programs.

### Download and Preprocess
1.Download benchmark dataset from [website](https://sites.google.com/view/learning-fixes)

2.Download sub-optimal dataset from [website](https://github.com/TruX-DTF/DL4PatchCorrectness/blob/master/data/experiment1/Patches_train.zip). Then, follow the instructions in Data-Preprocessing folder to obtain final data. Alternatively, the pre-processed dataset is available at [website](https://drive.google.com/file/d/1BTzr2H5O9y1L4oR7yjIlqPnJ9jUGIXeI/view?usp=share_link).


### Experiments
We conducted two experiments for Bug Fixing in RQ3, in order to test the generalization ability of the datasets. The two sub-folders corresponds to the experiments for the two datasets.

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