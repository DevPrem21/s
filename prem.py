import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset (Iris)
iris = load_iris()
X, y = iris.data, iris.target

# Split into training & testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Initialize LDA
lda = LinearDiscriminantAnalysis(n_components=2)

# Fit the model and transform data
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# Accuracy on test set
acc = lda.score(X_test, y_test)
print("LDA Test Accuracy:", acc)

# Plot results
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']

for i, color in zip(range(len(iris.target_names)), colors):
    plt.scatter(
        X_train_lda[y_train == i, 0],
        X_train_lda[y_train == i, 1],
        alpha=0.7,
        c=color,
        label=iris.target_names[i]
    )

plt.xlabel("LD1")
plt.ylabel("LD2")
plt.title("LDA Projection of Iris Dataset - PREMCHAND KUMAR MANDAL (Roll No 40)")
plt.legend()
plt.grid(True)
plt.show()
