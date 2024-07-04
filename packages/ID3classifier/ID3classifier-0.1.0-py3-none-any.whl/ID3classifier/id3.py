import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class Node:
    def __init__(self, attribute=None, label=None, branches=None):
        self.attribute = attribute
        self.label = label
        self.branches = branches or {}

class ID3:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.tree = None
        self.le = LabelEncoder()
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return -np.sum(probabilities * np.log2(probabilities + 1e-10))

    def information_gain(self, X, y, attribute):
        entropy_before = self.entropy(y)
        values, counts = np.unique(X[:, attribute], return_counts=True)
        
        subset_entropies = {}
        for value in values:
            subset = y[X[:, attribute] == value]
            subset_entropies[value] = self.entropy(subset)
        
        weighted_entropy = sum(counts[i] / len(y) * subset_entropies[values[i]] for i in range(len(values)))
        return entropy_before - weighted_entropy

    def get_best_attribute(self, X, y):
        gains = [self.information_gain(X, y, i) for i in range(X.shape[1])]
        return np.argmax(gains)

    def id3(self, X, y, attribute_names, depth=0):
        if len(np.unique(y)) == 1:
            return Node(label=y[0])
        
        if len(attribute_names) == 0 or (self.max_depth and depth >= self.max_depth) or len(y) < self.min_samples_split:
            return Node(label=np.bincount(y).argmax())
        
        best_attribute = self.get_best_attribute(X, y)
        node = Node(attribute=attribute_names[best_attribute])
        
        for value in np.unique(X[:, best_attribute]):
            subset_indices = X[:, best_attribute] == value
            subset_X = np.delete(X[subset_indices], best_attribute, axis=1)
            subset_y = y[subset_indices]
            subset_attribute_names = np.delete(attribute_names, best_attribute)
            
            if len(subset_X) == 0:
                node.branches[value] = Node(label=np.bincount(y).argmax())
            else:
                node.branches[value] = self.id3(subset_X, subset_y, subset_attribute_names, depth + 1)
        
        return node

    def fit(self, X, y):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("X should be a pandas DataFrame")
        if not isinstance(y, (pd.Series, np.ndarray)):
            raise ValueError("y should be a pandas Series or numpy array")
        
        self.feature_names = X.columns.tolist()
        self.le.fit(y)
        y_encoded = self.le.transform(y)
        attribute_names = np.array(X.columns)
        self.tree = self.id3(X.values, y_encoded, attribute_names)

    def predict_single(self, x, node):
        if node.label is not None:
            return node.label
        
        value = x.get(node.attribute)
        if value is None or value not in node.branches:
            branch_labels = [n.label for n in node.branches.values() if n.label is not None]
            if branch_labels:
                return max(set(branch_labels), key=branch_labels.count)
            else:
                return self.le.transform(['unknown'])[0]
        
        return self.predict_single(x, node.branches[value])

    def predict(self, X):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("X should be a pandas DataFrame")
        
        if not all(col in X.columns for col in self.feature_names):
            raise ValueError("X does not contain all features used during training")
        
        predictions = [self.predict_single(X.iloc[i], self.tree) for i in range(len(X))]
        return self.le.inverse_transform(predictions)

    def print_tree(self, node=None, indent=""):
        if node is None:
            node = self.tree
        
        if node.label is not None:
            print(indent + "Predict:", self.le.inverse_transform([node.label])[0])
        else:
            print(indent + node.attribute + ":")
            for value, child in node.branches.items():
                print(indent + "    " + str(value) + " ->")
                self.print_tree(child, indent + "    ")