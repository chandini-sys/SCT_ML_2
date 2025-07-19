# 🛍️ Customer Segmentation using K-Means Clustering

This project performs **customer segmentation** using the **K-Means Clustering algorithm**. It groups customers based on their **Annual Income** and **Spending Score**, helping a retail business target different customer groups more effectively.

---

## 📊 Dataset

A simulated `Mall_Customers.csv` dataset is used, which includes:

- `CustomerID`
- `Gender`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

You can easily scale this with real-world datasets in the future.

---

## 🧠 Technologies Used

- Python 🐍
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📈 Key Steps

1. **Create/Load Dataset**
2. **Visualize Raw Data**
3. **Apply Elbow Method** to find optimal number of clusters
4. **Train KMeans Model**
5. **Visualize Clusters**
6. **Export Clustered Data**

---

## 📂 Files in this Project

| File | Description |
|------|-------------|
| `kmeans_customer_segmentation.py` | Main Python script |
| `Mall_Customers.csv` | Input dataset |
| `clustered_mall_customers.csv` | Output with cluster labels |
| `elbow_method.png` | Elbow graph to choose optimal clusters |
| `clustered_customers.png` | Visual plot of clustered customers |

---

## 🔍 Sample Output (Clusters)

Clusters are formed based on how much a customer earns and spends:

- 🎯 High Income, High Spend
- 💸 Low Income, High Spend
- ⚠️ Low Spend, Any Income

---

## 📌 How to Run

1. Clone this repository or download the `.py` and `.csv` files
2. Make sure you have the required packages:

```bash
pip install pandas matplotlib seaborn scikit-learn
