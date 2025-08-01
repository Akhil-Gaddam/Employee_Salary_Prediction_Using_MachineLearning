# Employee Salary Prediction Using Machine Learning

## Project Overview

The aim of this project is to estimate employee salaries (in USD and INR) from provided job and company-related details. It uses historical salary data and applies machine learning models to predict salary with high accuracy.


## Tools and Technologies Used

- **Languages & IDE**: Python, Jupyter Notebook
- **Web Framework**: Streamlit
- **Libraries**: 
  - `pandas`, `numpy` – data handling
  - `matplotlib`, `seaborn` – EDA and visualization
  - `scikit-learn` – model building
  - `joblib` – saving/loading models
  - `streamlit` – web app interface


## Dataset

- **File**: `Salaries.csv`
- **Target Variable**: `salary_in_usd`
- **Features Used**:
  - Work Year
  - Experience Level
  - Employment Type
  - Job Title
  - Employee Residence
  - Remote Ratio
  - Company Location
  - Company Size


## Workflow

1. **Data Loading** – Import `Salaries.csv` dataset using pandas.
2. **Data Cleaning** – Remove irrelevant columns like `salary`, `salary_currency`.
3. **EDA** – Visualizations like boxplots and distributions using `seaborn` and `matplotlib`..
4. **Feature Engineering** – Apply one-hot encoding to categorical columns.
5. **Train-Test Split**  
   Split the dataset into training and testing sets (80-20 split).
6. **Model Training** – Train 4 models:
   - Linear Regression
   - Decision Tree Regressor
   - Random Forest Regressor
   - Gradient Boosting Regressor
7. **Model Comparison** – Use R2 Score, MAE, RMSE to evaluate model performance.
8. **Model Saving** – Save the best model (Gradient Boosting) with `joblib`.
9. **Build Web App**  
   Build a **Streamlit** app that takes user input and displays predicted salary in USD and INR.

## Screenshots





### Boxplot Visualization

<img width="1024" height="508" alt="Screenshot_visualization" src="https://github.com/user-attachments/assets/1617ddd5-457a-4ed8-aa23-509d5de37322" />

### Evaluation Metrics

<img width="675" height="128" alt="Screenshot_Evaluation_Metrics" src="https://github.com/user-attachments/assets/2a22289d-c1da-4197-9c40-235c3e0b7a25" />
    
### Model Comparsion Visualization

<img width="1343" height="739" alt="Screenshot_Model_Comparsion" src="https://github.com/user-attachments/assets/899170c3-3f2e-4156-9942-3ace162f9f1e" />

###  Home Page

<img width="1919" height="1020" alt="Screenshot_Homepage" src="https://github.com/user-attachments/assets/663c984f-e67c-4aa8-9f62-b41e0d2b1e5f" />

###  Prediction Output

<img width="1919" height="1013" alt="Screenshot_Output_Prediction" src="https://github.com/user-attachments/assets/a3a51d45-9b25-4589-8396-b171d6580be4" />

## Output

- Predicts salaries in **USD** and converted **INR**.
- User-friendly Streamlit app to input employee attributes and receive predictions.
- Shows dropdowns for fields like job title, company size, location, etc.


## Key Insights

- Gradient Boosting performed best with highest R2 score(R2 ~0.44).
- Salary strongly depends on job title, company location, and experience level.
- Many outliers were identified in salary, but retained to preserve real-world variability.


## Files Included

- `Salaries.csv` – Cleaned dataset
- `Employee_Salary_Prediction.ipynb` – Jupyter notebook for model training & EDA
- `model.pkl` – Saved Gradient Boosting model
- `feature_columns.pkl` – Saved list of feature columns
- `app.py` – Streamlit app for deployment
- `requirements.txt` – Required libraries


## How to Run

**Clone this repository:**

```
git clone [https://github.com/Akhil-Gaddam/Employee_Salary_Prediction.git](https://github.com/Akhil-Gaddam/Employee_Salary_Prediction_Using_Machine_Learning.git)
```
**Install Dependencies**
- pip install -r requirements.txt

**Steps to Run the Project:**

- Open Salaries.csv in Jupyter Notebook.

- Run Employee_Salary_Prediction.ipynb to preprocess and train the model.

- Ensure model.pkl and feature_columns.pkl are saved.

- Open app.py in any code editor to check the Streamlit app code.

- Run the web app using the command:

  ```
  streamlit run app.py
  ```
- Then click enter, it opens a web application of streamlit app
  
- Interact with the app to predict salaries in USD and 'Coverted INR' using various employee inputs.


## App Features

- Predicts salary in real-time
- User inputs via dropdowns and sliders
- Dual currency output: USD and INR
- Clean and simple UI using Streamlit

