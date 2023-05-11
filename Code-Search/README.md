# CodeXGLUE -- Code Search (AdvTest)

## Task Definition

Code Search aims to search for relevant code snippets given their natural language descriptions by matching semantics.

## Dataset

The dataset we use comes from [CodeSearchNet](https://arxiv.org/pdf/1909.09436.pdf).

### Data Download ans Preprocess

dataset.zip can be downloaded from this [website](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/NL-code-search-Adv).

```shell
unzip dataset.zip
cd dataset
wget https://zenodo.org/record/7857872/files/python.zip
unzip python.zip
python preprocess.py
rm -r python
rm -r *.pkl
rm python.zip
cd ..
```

### Fine-tune and Evaluation
CodeBERT for example:
```shell
cd codebert
./run.sh
./eval.sh
```

The model files and result files are saved in `./codebert/saved_models` folder.