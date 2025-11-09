![WhatsApp Image 2025-11-09 at 18 00 37](https://github.com/user-attachments/assets/3e6bdbce-ad97-45eb-bef2-722843d585a8)
To Implement Linear Discriminant Analysis (LDA)

Objective:

To perform dimensionality reduction using Linear Discriminant Analysis (LDA) and observe how it separates different classes in a dataset.

Theory:

Linear Discriminant Analysis (LDA) is a supervised linear transformation technique used for dimensionality reduction and classification.
It projects high-dimensional data onto a lower-dimensional space while maximizing class separability.

Unlike Principal Component Analysis (PCA) which is unsupervised and focuses only on maximum variance, LDA uses class labels to find a projection that:

Maximizes the distance between the means of different classes (between-class variance), and

Minimizes the spread within each class (within-class variance).

Hence, LDA finds a linear combination of features that best separates two or more classes.

Mathematical Formulation:

Algorithm Steps:


Result:

The dataset was successfully reduced to two dimensions using LDA.
The plot shows that LDA clearly separates different classes, demonstrating maximum class separability in the reduced space.



