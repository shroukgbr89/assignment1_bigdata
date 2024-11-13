import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def model(df):
    # Apply PCA
    pca = PCA(n_components=3)
    x_pca = pd.DataFrame(pca.fit_transform(df), columns=["col1", "col2", "col3"])

    # K-means clustering
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(x_pca)
    x_pca["Clusters"], df["Clusters"] = clusters, clusters

    # Write cluster counts to file
    with open("k.txt", "w") as file:
        for cluster, count in df['Clusters'].value_counts().items():
            file.write(f"Cluster {cluster}: {count} records\n")
