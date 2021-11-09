from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np


data = pd.read_csv('diabetes.csv')

X = data.iloc[:, :-1].values

y = data.iloc[:,-1].values

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[ : , : ])
X[:, :] = imputer.transform(X[:, :])
imputer = SimpleImputer(missing_values=0, strategy="mean")
imputer.fit(X[:, :])
X[:, :] = imputer.transform(X[:, :])
# Encoding categorical data
# Encoding the Independent Variable
ct = ColumnTransformer(
    transformers=[('encoders', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Encoding the Dependent Variable
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)


# Feature Scaling
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
