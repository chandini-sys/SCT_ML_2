import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# 1️⃣ Create the dataset
data = {
    'CustomerID': range(1, 11),
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
    'Age': [19, 21, 20, 23, 31, 22, 35, 40, 29, 18],
    'Annual Income (k$)': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'Spending Score (1-100)': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}
df = pd.DataFrame(data)
df.to_csv('Mall_Customers.csv', index=False)
print("✅ Mall_Customers.csv created successfully!")

# 2️⃣ Load dataset
df = pd.read_csv('Mall_Customers.csv')

# 3️⃣ Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# 4️⃣ Elbow Method to determine best k
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.savefig("elbow_method.png")
plt.show()

# 5️⃣ Apply K-Means with 3 clusters (good for this data size)
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# 6️⃣ Visualize clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set2',
    data=df,
    s=100
)
plt.title('Customer Segments')
plt.grid(True)
plt.savefig("clustered_customers.png")
plt.show()

# 7️⃣ Save clustered data
df.to_csv('clustered_mall_customers.csv', index=False)
print("✅ Clustered data saved to clustered_mall_customers.csv")
