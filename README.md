# Machine Learning Projects

This workspace contains two small ML projects:

1. **Iris classification model** (Random Forest) in [irisModel/](irisModel/)
2. **Smartphone price regression model** (Random Forest) in [smartphoneModel/](smartphoneModel/)

It also includes a synthetic data generator for smartphone pricing.

## Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn

Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

## Project: Iris model

**Location:** [irisModel/](irisModel/)

**Dataset:** [irisModel/Dataset/](irisModel/Dataset/)

**Notebook:** [irisModel/model.ipynb](irisModel/model.ipynb)

**What it does:**

- Trains a Random Forest classifier on `train.xlsx`.
- Predicts on `test.xlsx`.
- Writes results to `result.xlsx` and prints accuracy stats.

**How to run:**

Open [irisModel/model.ipynb](irisModel/model.ipynb) and run the cells top-to-bottom.

**Accuracy reporting (Iris):**

After generating `result.xlsx`, use this snippet to report accuracy:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(result['actual'], result['predictions'])
error_percentage = (1 - accuracy) * 100

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Error Percentage: {error_percentage:.2f}%")
print(f"\nNumber of correct predictions: {(result['predictions'] == result['actual']).sum()}")
print(f"Number of incorrect predictions: {(result['predictions'] != result['actual']).sum()}")
```

**Latest results (Iris):**

- Accuracy: 97.06%
- Error Percentage: 2.94%
- Correct predictions: 33
- Incorrect predictions: 1

## Project: Smartphone price model

**Location:** [smartphoneModel/](smartphoneModel/)

**Dataset:** [smartphoneModel/Dataset/](smartphoneModel/Dataset/)

**Notebook:** [smartphoneModel/model.ipynb](smartphoneModel/model.ipynb)

**What it does:**

- Trains a Random Forest regressor on `Dataset/train.csv`.
- Tests on `Dataset/test.csv`.
- Saves predictions to `Dataset/result.csv` and prints MAE, RMSE, and R2.

**How to run:**

Open [smartphoneModel/model.ipynb](smartphoneModel/model.ipynb) and run the cells top-to-bottom.

**Accuracy reporting (Smartphone regression):**

After generating `Dataset/result.csv`, you can compute accuracy as the fraction of predictions within a tolerance of the true price:

```python
tolerance = 0.10  # 10%
within_tol = (result['prediction'].sub(result['actual']).abs() <= tolerance * result['actual'])
accuracy = within_tol.mean()
error_percentage = (1 - accuracy) * 100

print(f"Accuracy (within {tolerance*100:.0f}%): {accuracy * 100:.2f}%")
print(f"Error Percentage: {error_percentage:.2f}%")
print(f"\nNumber of correct predictions: {within_tol.sum()}")
print(f"Number of incorrect predictions: {(~within_tol).sum()}")

# Exact-match accuracy (usually near 0 for continuous targets)
exact_match = (result['prediction'].round().astype(int) == result['actual'])
print(f"\nExact-match Accuracy: {exact_match.mean() * 100:.2f}%")
print(f"Exact correct: {exact_match.sum()}, exact incorrect: {(~exact_match).sum()}")
```

**Latest results (Smartphone regression):**

- Accuracy (within 10%): 40.00%
- Error Percentage: 60.00%
- Correct predictions: 80
- Incorrect predictions: 120
- Exact-match Accuracy: 0.00%
- Exact correct: 0
- Exact incorrect: 200

## Smartphone dataset generator

**Script:** [smartphones-Data.py](smartphones-Data.py)

**What it does:**

- Generates a synthetic smartphone dataset with 1,000 rows.
- Writes the dataset to `smartphone_data.csv`.
- Prints the first few rows to the console.

**How to run:**

```bash
python smartphones-Data.py
```
