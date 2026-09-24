# AI Senior Project Lab

> A public learning lab for building the foundations of an AI-focused Electrical Engineering senior project.

This repository documents my preparation before choosing and building my final senior project. It is a place to learn deliberately, test ideas, keep experiments reproducible, and record progress in public.

## Roadmap

| Stage | Goal | Status |
| --- | --- | --- |
| **Stage 1 — Knowledge Gathering** | Build the programming, machine-learning, evaluation, and tooling foundations. | In progress |
| **Stage 2 — Project Definition** | Select a realistic EE + AI problem with a clear dataset, baseline, evaluation plan, and scope. | Planned |

## What I have completed so far

- Created an isolated Python environment for reproducible work.
- Set up Git, GitHub, VS Code, JupyterLab, pytest, and Ruff.
- Practised Python variables, functions, loops, lists, dictionaries, conditionals, and input validation.
- Wrote automated tests for a small rule-based score classifier.
- Built a first end-to-end scikit-learn classifier using the Iris dataset.

## First machine-learning experiment

The notebook `01_first_ml_classifier.ipynb` is a small, complete supervised-learning workflow:

- **Dataset:** Iris flowers (150 samples, 4 numeric features, 3 classes)
- **Task:** Multiclass classification
- **Split:** 80% training / 20% held-out testing, with stratified classes
- **Pipeline:** `StandardScaler` + `LogisticRegression`
- **Evaluation:** Accuracy, classification report, and confusion matrix
- **Initial result:** **93.3%** test accuracy (28 correct predictions out of 30)

This is a learning exercise, not a research claim. The purpose is to understand the full workflow: inspect data, split it correctly, train a baseline, and evaluate it on data the model did not see during training.

## Repository structure

```text
AI_Senior_Project_Lab/
├── notebooks/
│   ├── 00_environment_check.ipynb
│   └── 01_first_ml_classifier.ipynb
├── src/
│   └── python_basics.py
├── tests/
│   └── test_python_basics.py
└── .gitignore
```

## Run the project locally

Clone the repository and create a virtual environment:

```powershell
git clone https://github.com/NasirAldeen/AI-Senior-Project-Lab.git
Set-Location AI-Senior-Project-Lab
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install numpy pandas scipy matplotlib seaborn scikit-learn jupyterlab ipykernel pytest ruff
```

Open the folder in VS Code:

```powershell
code .
```

Run the tests and style check from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\ruff.exe check src tests
```

## Learning principles

- Start with a simple baseline before complex models.
- Keep training and test data separate to avoid data leakage.
- Track code, notebooks, and decisions with Git.
- Report more than one metric when the problem requires it.
- Treat results as evidence to investigate, not just a score to maximize.

## Next topics

1. Explore and visualize a real dataset with pandas, NumPy, Matplotlib, and Seaborn.
2. Compare several classifiers and understand when accuracy is misleading.
3. Learn feature engineering, cross-validation, and hyperparameter tuning.
4. Study signal/time-series data and possible EE applications.
5. Explore PyTorch and practical local LLM / RAG workflows.
6. Use what I learn to define a focused Stage 2 senior-project problem.

---

Learning in public by [NasirAldeen](https://github.com/NasirAldeen).
