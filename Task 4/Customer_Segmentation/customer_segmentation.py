import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# K-Means Clustering
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(X)

# Show cluster assignments
print("\nCustomer Clusters:")
print(df[['CustomerID', 'Cluster']].head(10))

# Show cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("\nPCA Sample:")
print(X_pca[:5])

# Visualization
plt.figure(figsize=(8, 6))

plt.scatter(
    X['Annual Income (k$)'],
    X['Spending Score (1-100)'],
    c=df['Cluster']
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200
)

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segmentation using K-Means')

plt.show()