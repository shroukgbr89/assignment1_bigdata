import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vis(df):
    # PCA Transformation
    pca = PCA(n_components=3)
    x_pca = pd.DataFrame(pca.fit_transform(df), columns=["col1", "col2", "col3"])

    # K-means clustering
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(x_pca)

    # 3D plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("KMeans Clustering", fontsize=15)
    scatter = ax.scatter(x_pca['col1'], x_pca['col2'], x_pca['col3'], c=clusters, cmap='viridis')
    plt.colorbar(scatter)
    plt.savefig('vis.png')
