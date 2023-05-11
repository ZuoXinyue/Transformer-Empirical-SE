# Empirical Study on Transformer-based Techniques for SE Research

## Environment Preparation

- *Hardware*: NVIDIA RTX A4000

- CUDA Version: 11.6

- python 3.8+
    ```
    argparse               1.4.0
    numpy                  1.23.5
    pandas                 1.5.2
    matplotlib             3.4.1
    tqdm                   4.64.1
    torch                  1.13.0
    torchaudio             0.13.1
    torchvision            0.14.1
    tensorboardX           2.5.1
    transformers           4.26.0
    tokenizers             0.13.2
    ```

## Code Structure
```
├── Bug-Detection
│   ├── codebert
|   ├── codegpt
│   └── codet5
├── Bug-Fixing
│   ├── Benchmark-Experiments
|   |   ├── ...
│   ├── Suboptimal-Experiments (RQ3)
|   |   ├── ...
├── Code-Search
│   ├── ...
├── Code-Summarization
│   ├── Benchmark-Experiments
|   |   ├── ...
│   ├── Suboptimal-Experiments (RQ3)
|   |   ├── ...
│   ├── Mix-Experiments (RQ3)
|   |   ├── codebert
|   |   ├── codebert_half
|   |   ├── codegpt
|   |   ├── codegpt_half
|   |   ├── codet5
│   │   └── codet5_half
├── Data-Preprocessing
│   ├── Bug-Fixing
│   ├── Code-Summarization
|   |   ├── Suboptimal-Dataset
|   |   ├── Mix-Dataset
|   |   └── Mix-Half-Dataset
```

## Running Experiments
Instructions on how to conduct the experiments are given in detail in the respective folders.

## Acknowledgement
Our implementation is adapted from: https://github.com/microsoft/CodeXGLUE, https://github.com/microsoft/CodeBERT, https://github.com/salesforce/CodeT5, https://github.com/ZZR0/ISSTA22-CodeStudy/tree/master