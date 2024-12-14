import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.ensemble import IsolationForest
import requests
import json

def analyze_csv(file_path):
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    print(f"Dataset: {file_path}\n")
    print(data.info())
    print("\nSample Data:\n", data.head())

    summary = data.describe(include='all')
    print("\nSummary Statistics:\n", summary)

    missing_values = data.isnull().sum()
    print("\nMissing Values:\n", missing_values)

    numeric_data = data.select_dtypes(include=['number'])
    if not numeric_data.empty:
        correlation = numeric_data.corr()
        print("\nCorrelation Matrix:\n", correlation)

        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        plt.savefig(f'{file_path}_correlation_matrix.png')
        plt.close()

    if numeric_data.shape[1] > 1:
        scaled_data = StandardScaler().fit_transform(numeric_data.dropna())
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(scaled_data)

        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(reduced_data)

        plt.figure(figsize=(8, 6))
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clusters, cmap='viridis')
        plt.title('Clustering Visualization (PCA)')
        plt.savefig(f'{file_path}_clustering_pca.png')
        plt.close()

        tsne = TSNE(n_components=2, random_state=42)
        tsne_data = tsne.fit_transform(scaled_data)

        plt.figure(figsize=(8, 6))
        plt.scatter(tsne_data[:, 0], tsne_data[:, 1], c=clusters, cmap='viridis')
        plt.title('Clustering Visualization (t-SNE)')
        plt.savefig(f'{file_path}_clustering_tsne.png')
        plt.close()

        isolation_forest = IsolationForest(random_state=42, contamination=0.05)
        outliers = isolation_forest.fit_predict(scaled_data)

        plt.figure(figsize=(8, 6))
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=outliers, cmap='coolwarm', alpha=0.6)
        plt.title('Outlier Detection (Isolation Forest)')
        plt.savefig(f'{file_path}_outliers.png')
        plt.close()

    context = {
        'columns': data.columns.tolist(),
        'dtypes': data.dtypes.tolist(),
        'missing_values': missing_values.to_dict(),
        'summary': summary.to_dict(),
    }

    return context

def narrate_analysis(context, file_path):
    proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    token = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDMxMjhAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.yKujqmaH6IoubSHHhGNj1JdP4CYKwBEQg718sTK_6Ck"

    prompt = (
        f"Analyze the dataset '{file_path}'. Here is the context:\n"
        f"Columns and types: {context['columns']}, {context['dtypes']}\n"
        f"Missing values: {context['missing_values']}\n"
        f"Summary statistics: {context['summary']}\n"
        "Write a narrative describing the dataset and insights from the analysis."
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(proxy_url, headers=headers, json=data)
        response.raise_for_status()
        story = response.json()["choices"][0]["message"]["content"].strip()
        with open('README.md', 'w') as f:
            f.write(f"# Analysis of {file_path}\n\n{story}\n")
        print("Narrative saved to README.md")
    except Exception as e:
        print(f"Error generating narrative: {e}")

if __name__ == "__main__":
    file_paths = ["\C:\Users\KIIT\Downloads\happiness.csv", "\C:\Users\KIIT\Downloads\goodreads.csv"]

    for file_path in file_paths:
        context = analyze_csv(file_path)
        if context:
            narrate_analysis(context, file_path)
