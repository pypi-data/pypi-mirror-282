
<!-- Main title -->
# ID3 Decision Tree Classifier

<!-- Brief introduction -->
This repository contains a Python implementation of the ID3 (Iterative Dichotomiser 3) algorithm for decision tree classification. The implementation includes an `ID3` class that can be used to train a decision tree model and make predictions on new data.

<!-- Table of Contents -->
## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Reference](#api-reference)
7. [Example](#example)
8. [Contributing](#contributing)
9. [License](#license)

<!-- Detailed introduction -->
## Introduction

The ID3 algorithm is a simple decision tree learning algorithm introduced by Ross Quinlan in 1986. It builds a decision tree from a fixed set of examples and uses the concept of information gain to select the best attribute for splitting the data at each node.

This implementation provides a flexible and efficient ID3 classifier with additional features such as maximum depth limitation and minimum samples for splitting.

<!-- List of features -->
## Features

- Build decision trees using the ID3 algorithm
- Support for both categorical and numerical features
- Customizable maximum tree depth and minimum samples for splitting
- Automatic handling of missing or unseen values during prediction
- Tree visualization through a print method
- Integration with scikit-learn's LabelEncoder for handling non-numeric labels

<!-- Requirements section -->
## Requirements

- Python 3.6+
- NumPy
- pandas
- scikit-learn

<!-- Installation instructions -->
## Installation

1. Clone this repository:
   
   
```bash
git clone https://github.com/yourusername/id3-decision-tree.git
```
   

2. Install the required dependencies:
  ```bash
  pip install numpy pandas scikit-learn
  ```

<!-- Usage instructions -->
## Usage

To use the ID3 classifier in your project, import the `ID3` class from the main script:

```python
from id3_classifier import ID3

# Create an instance of the ID3 classifier
model = ID3(max_depth=3, min_samples_split=2)

# Fit the model to your data
model.fit(X, y)

# Make predictions
predictions = model.predict(X_test)

# Print the decision tree
model.print_tree()
```

<!-- API Reference section -->
## API Reference

### `ID3` Class

#### `__init__(self, max_depth=None, min_samples_split=2)`

Initializes the ID3 classifier.

- `max_depth` (int, optional): The maximum depth of the tree. If None, the tree will expand until all leaves are pure or contain less than `min_samples_split` samples.
- `min_samples_split` (int, default=2): The minimum number of samples required to split an internal node.

#### `fit(self, X, y)`

Builds the decision tree from the training data.

- `X` (pandas.DataFrame): The input features.
- `y` (pandas.Series or numpy.ndarray): The target values.

#### `predict(self, X)`

Predicts the target values for the given input features.

- `X` (pandas.DataFrame): The input features for which to make predictions.

Returns:
- numpy.ndarray: The predicted target values.

#### `print_tree(self, node=None, indent="")`

Prints the decision tree structure.

- `node` (Node, optional): The starting node. If None, starts from the root of the tree.
- `indent` (str, default=""): The indentation string for formatting the output.

### `Node` Class

Represents a node in the decision tree.

#### `__init__(self, attribute=None, label=None, branches=None)`

- `attribute` (str, optional): The attribute used for splitting at this node.
- `label` (any, optional): The predicted label if this is a leaf node.
- `branches` (dict, optional): A dictionary of child nodes, where keys are attribute values and values are Node objects.

<!-- Example usage -->
## Example

Here's a simple example of how to use the ID3 classifier:

```python
import pandas as pd
from id3_classifier import ID3

# Create a sample dataset
df = pd.DataFrame({
    'feature1': ['A', 'A', 'B', 'B'],
    'feature2': ['X', 'Y', 'X', 'Y'],
    'label': ['yes', 'no', 'yes', 'no']
})

X = df[['feature1', 'feature2']]
y = df['label']

# Create and train the model
model = ID3(max_depth=3, min_samples_split=2)
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print("Predictions:", predictions)

# Print the decision tree
print("\nDecision Tree:")
model.print_tree()
```

<!-- Contributing section -->
## Contributing

Contributions to this project are welcome! Please feel free to submit a Pull Request.

<!-- License information -->
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
      
