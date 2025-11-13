AIM:
To implement Linear Discriminant Analysis (LDA) for dimensionality reduction and classification using the Iris dataset.


THEORY:
 Linear Discriminant Analysis (LDA)

Linear Discriminant Analysis (LDA) is a supervised machine learning technique used for dimensionality reduction and classification.
The main goal of LDA is to project high-dimensional data onto a lower-dimensional space in such a way that the separation between different classes is maximized.

LDA works by finding new axes (called linear discriminants) that best separate the data points of different classes.
It uses both class labels and feature information, unlike PCA, which is an unsupervised method and only focuses on maximizing variance without considering class labels.

In LDA, two types of scatter (variation) are measured:

Within-class scatter (SW): measures how much the data points in the same class vary from their mean.
Between-class scatter (SB): measures how much the class means differ from the overall mean.
LDA tries to maximize the ratio of between-class scatter to within-class scatter, ensuring that the classes are as distinct as possible after projection.

Mathematically, LDA finds a projection matrix W that maximizes the function:


J(W) = |W^T S_B W| /   |W^T S_W W|


where:

( S_B ) = Between-class scatter matrix
( S_W ) = Within-class scatter matrix
After finding this projection, data is transformed into a lower-dimensional space where it becomes easier to classify.

LDA is widely used in applications such as pattern recognition, face recognition, speech recognition, and bioinformatics, where both dimensionality reduction and class separability are important.


Conclusion:
In this experiment, Linear Discriminant Analysis (LDA) was applied to the Iris dataset to reduce its four features into two.
The transformed data clearly showed good separation between the three flower classes — Iris Setosa, Iris Versicolor, and Iris Virginica.
The model achieved high accuracy, proving that LDA effectively reduces dimensions while maintaining class separability.



