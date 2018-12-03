#install graphviz from internet for windows (https://graphviz.gitlab.io/_pages/Download/Download_windows.html) download .msi file and install
#set environmental variable path to C:/Program Files (x86)/Graphviz2.38/bin
# output of this program will be generated as pdf file in location where program is saved
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
clf.predict([[2., 2.]])
clf.predict_proba([[2., 2.]])
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
print(iris)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris")