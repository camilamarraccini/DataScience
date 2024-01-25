import sys
import scipy
import numpy
import matplotlib
import pandas as pd
import sklearn
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#carregar dataset 
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

#formatar colunas
colunas = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
dataset = pd.read_csv(url, names = colunas)
dataset.columns = colunas


# shape
print(dataset.shape)


# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# distribuindo classes
print(dataset.groupby('class').size())

# partindo para a visualização! 
# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

#Visualização OK, hora de trabalhar com algoritmos!


#criando um conjunto de dados de VALIDAÇÃO
# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
                      

#VALIDAÇÃO CRUZADA (cross validation) para estimar a precisão:

scoring = 'accuracy'

#Regressão Logística (LR)
#Análise Linear Discriminante (LDA)
#K-vizinhos mais próximos (KNN).
#Árvores de Classificação (Decision Tree) e Regressão (CART).
#Gaussian Naive Bayes (NB).
#Support Vector Machines (SVM).