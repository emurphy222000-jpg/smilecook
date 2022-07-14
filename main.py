from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Load dataset
def execute_model() :
	url = 	"https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
	names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
	dataset = read_csv(url, names=names)
# 	Split-out validation dataset
	array = dataset.values
	X = array[:,0:4]
	y = array[:,4]
	X_train, X_validation, Y_train, Y_validation = 	train_test_split(X, y, test_size=0.20, random_state=1)
# 	Make predictions on validation dataset
	model = SVC(gamma='auto')
	model.fit(X_train, Y_train)
	predictions = model.predict(X_validation)
# 	Evaluate predictions
	return accuracy_score(Y_validation, predictions), confusion_matrix(Y_validation, predictions),classification_report(Y_validation, predictions)

if __name__  == "__main__:
	execute_model()