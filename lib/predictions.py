import sys
import random
import numpy as np
from scipy.stats import mode
from contextlib import contextmanager
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense
#from tensorflow.keras.optimizers import Adam

class Ensemble:
  def __init__(self, *models):
    self.model_infos = models
    self.n = len(models)

  def fit(self, x, y):
    for model, args in self.model_infos:
      if "fit_size" in args:
        model.fit(x[:args["fit_size"]], y[:args["fit_size"]])
      else:
        model.fit(x, y)

  def predict(self, x):
    return np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=[model.predict(x) for model, _ in self.model_infos])

class Predictions:
  def __init__(self, df, x_columns, y_column, random_seed=None, output=sys.stdout):
    x = df[*x_columns]
    y = df[y_column]
    self.random_seed = random_seed
    self.output = output
    with self.use_random_seed():
      self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.4)

  def test_accuracy(self, model, label, fit_size=None):
    print(label, file=self.output)
    with self.use_random_seed():
      if fit_size:
        model.fit(self.x_train[:fit_size], self.y_train[:fit_size])
      else:
        model.fit(self.x_train, self.y_train)
      y_pred = model.predict(self.x_test)
      print("Accuracy: ", accuracy_score(self.y_test, y_pred), file=self.output)
      print("Classification Report:\n", classification_report(self.y_test, y_pred), file=self.output)

  def test_models(self):
    for model, args in self._classifiers():
      self.test_accuracy(model, **args)

  # Classifiers

  def _classifiers(self):
    return (self.logistic_regression,
            self.polynomial_svc,
            self.linear_svc,
            self.rbf_svc,
            self.sigmoid_svc,
            self.decision_tree,
            self.random_forest,
            self.gaussian_nb,
            self.knn,
            self.ensemble,
            self.control
    )

  @property
  def logistic_regression(self):
    return (LogisticRegression(class_weight="balanced"), {"label": "Logistic Regression"})

  @property
  def polynomial_svc(self):
    return (SVC(kernel="poly", class_weight="balanced"), {"label": "Polynomial SVC", "fit_size": 1000})

  @property
  def linear_svc(self):
    return (SVC(kernel="linear", class_weight="balanced"), {"label": "Linear SVC", "fit_size": 1000})

  @property
  def rbf_svc(self):
    return (SVC(kernel="rbf", class_weight="balanced"), {"label": "RBF SVC", "fit_size": 1000})

  @property
  def sigmoid_svc(self):
    return (SVC(kernel="sigmoid", class_weight="balanced"), {"label": "Sigmoid SVC", "fit_size": 1000})

  @property
  def decision_tree(self):
    return (DecisionTreeClassifier(class_weight="balanced"), {"label": "Decision Tree"})

  @property
  def random_forest(self):
    return (RandomForestClassifier(n_estimators=10), {"label": "Random Forest (N=10)"})

  @property
  def gaussian_nb(self):
    return (GaussianNB(), {"label": "Gaussian Naive Bayse"})

  @property
  def knn(self):
    return (KNeighborsClassifier(n_neighbors=10), {"label": "KNN (N=10)"})

  @property
  def control(self):
    return (DummyClassifier(strategy="stratified"), {"label": "Control"})

  @property
  def ensemble(self):
    return (Ensemble(self.logistic_regression, self.polynomial_svc, self.rbf_svc), {"label": "Ensemble (Logistic, Poly SVC, RBF SVC)"})

  @contextmanager
  def use_random_seed(self):
    if self.random_seed:
      state = random.getstate()
      random.seed(self.random_seed)
      try:
        yield
      finally:
        random.setstate(state)
    else:
      yield
