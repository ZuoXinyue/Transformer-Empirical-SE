# CodeXGLUE -- Bug Detection (Defect Detection)

## Task Definition

Bug Detection performs binary classification - determining if a program is buggy or not.

### Dataset

The dataset we use comes from the paper [*Devign*: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks](http://papers.nips.cc/paper/9209-devign-effective-vulnerability-identification-by-learning-comprehensive-program-semantics-via-graph-neural-networks.pdf).

### Download and Preprocess

1.Download dataset from [website](https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF/view?usp=sharing) to "dataset" folder or run the following command:

```shell
cd dataset
pip install gdown
gdown https://drive.google.com/uc?id=1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF
cd ..
```

2.Preprocess dataset: preprocessing files can be downloaded from [website](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Defect-detection/dataset):

```shell
cd dataset
python preprocess.py
cd ..
```

### Fine-tune and Evaluation (RQ2)
CodeBERT for example:
```shell
cd codebert
./run.sh
./eval.sh
```

The model files and result files are saved in `./codebert/saved_models` folder.
The resource consumption (RQ4) is recorded in the log files.