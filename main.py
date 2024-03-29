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

models = []    #lista que irá armazenar diferentes modelos de aprendizagem de máquina

models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
# LR = Logistics Regression (modelo), configurado com o solver 'liblinear' e abordagem ovr(one vs rest).
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results = []    #lista de resultados
names = []

for name, model in models:
   kfold = model_selection.KFold(n_splits=10, random_state=seed)
   cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
   results.append(cv_results)
   names.append(name)
   msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
   print(msg)

#model_selection.KFold(n_splits=10, random_state=seed): Define a estratégia de validação cruzada com 10 folds (ou partições) usando a classe KFold do módulo model_selection.
#model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring): Realiza a validação cruzada para o modelo atual (model) usando os dados de treinamento (X_train e Y_train). cv=kfold especifica a estratégia de validação cruzada a ser usada e scoring=scoring define a métrica de avaliação a ser utilizada.
#results.append(cv_results): Adiciona os resultados da validação cruzada para o modelo atual à lista results.
#names.append(name): Adiciona o nome do modelo à lista names.
#msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std()): Formata uma mensagem contendo o nome do modelo, a média e o desvio padrão dos resultados da validação cruzada.


#adicionando gráficos dos resultados da avaliação do modelo e comparar o spread e a accuracy média de cada modelo

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

