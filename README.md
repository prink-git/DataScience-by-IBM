# DataScience-by-IBM
A curated collection of Jupyter notebooks and hands-on projects from the IBM Data Science Professional Certificate program. Covers Python, data analysis, visualization, EDA, machine learning, and real-world applications.
#### Project consists of:
### Predicting Falcon 9 launch success using machine learning on historical SpaceX data.
#### Overview
This project builds a classification model to predict whether a SpaceX Falcon 9 launch will be successful based on features like payload mass, launch site, and orbit.

#### Dataset & Features
Source: SpaceX API & Wikipedia
Features: FlightNumber, LaunchSite, PayloadMass, Orbit, etc.
Target: LaunchSuccess (0 = Failure, 1 = Success)

#### Preprocessing
One-hot encoding for categorical variables
Filled missing values
Feature scaling using StandardScaler
#### Models Used
Logistic Regression, Decision Tree, SVM, Random Forest, KNN (also tested)
###### Best Model: LogisticRegression(C=1.0, penalty='l2', solver='liblinear')

#### Model	Accuracy
Logistic Reg.	92% ,Random Forest	94%, SVM (RBF)	89%
#### Key Insights
Orbit and payload mass strongly influence success
Most launches succeed from certain sites (e.g., KSC LC-39A)
Random Forest performed best, but logistic regression is interpretable.

### Titanic Survival Prediction
Predicting which passengers survived the Titanic disaster using machine learning.
#### Overview
Using the classic Titanic dataset, this project builds a binary classification model to predict passenger survival based on attributes like age, gender, class, and fare.
Best-performing model:
LogisticRegression(C=1.0, solver='liblinear')
Also tested:
Random Forest, Decision Tree, KNN, SVM
###### Performance
Model	Accuracy
Logistic Reg.	80%
Random Forest	83%
KNN	77%
###### Key Insights
Females had much higher survival rates.
Passengers in 1st class were more likely to survive.
Younger passengers had a better chance of survival.
