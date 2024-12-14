# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "scikit-learn",
#   "python-dotenv",
#   "chardet",
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.ensemble import IsolationForest
from dotenv import load_dotenv
from os import getenv
import requests
import json
import matplotlib
import chardet

load_dotenv()
matplotlib.use('Agg')

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def analyze_csv(file_path):
    encoding = detect_encoding(file_path)
    try:
        data = pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        print(f"Error reading {file_path} with encoding {encoding}: {e}")
        return


    # Basic information
    print(f"Dataset: {file_path}\n")
    print(data.info())
    print("\nSample Data:\n", data.head())

    # Summary statistics
    summary = data.describe(include='all')
    print("\nSummary Statistics:\n", summary)

    # Missing values
    missing_values = data.isnull().sum()
    print("\nMissing Values:\n", missing_values)

    # Correlation matrix (numeric columns only)
    numeric_data = data.select_dtypes(include=['number'])
    if not numeric_data.empty:
        correlation = numeric_data.corr()
        print("\nCorrelation Matrix:\n", correlation)
        
        # Visualize the correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        plt.savefig(f'{file_path}_correlation_matrix.png')
        plt.close()

    # Clustering using PCA
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

    # Clustering using t-SNE
        tsne = TSNE(n_components=2, random_state=42)
        tsne_data = tsne.fit_transform(scaled_data)

        plt.figure(figsize=(8, 6))
        plt.scatter(tsne_data[:, 0], tsne_data[:, 1], c=clusters, cmap='viridis')
        plt.title('Clustering Visualization (t-SNE)')
        plt.savefig(f'{file_path}_clustering_tsne.png')
        plt.close()

    # Outliers using Isolation Forest
    isolation_forest = IsolationForest(random_state=42, contamination=0.05)
    outliers = isolation_forest.fit_predict(scaled_data)

    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=outliers, cmap='coolwarm', alpha=0.6)
    plt.title('Outlier Detection (Isolation Forest)')
    plt.savefig(f'{file_path}_outliers.png')
    plt.close()

    # Save analysis context
    context = {
        'columns': data.columns.tolist(),
        'dtypes': data.dtypes.tolist(),
        'missing_values': missing_values.to_dict(),
        'summary': summary.to_dict(),
    }

    return context

def narrate_analysis(context, file_path):
    # Create a unique filename for each dataset
    base_name = os.path.splitext(os.path.basename(file_path))[0]  # Extracts the base name of the file
    readme_file = f"{base_name}_README.md"
    
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    api_key = os.getenv("AIPROXY_TOKEN")

    prompt = (
        f"Analyze the dataset '{file_path}'. Here is the context:\n"
        f"Columns and types: {context['columns']}, {context['dtypes']}\n"
        f"Missing values: {context['missing_values']}\n"
        f"Summary statistics: {context['summary']}\n"
        "Write a narrative describing the dataset and insights from the analysis."
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        story = response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error generating narrative: {e}")
        story = "Error generating narrative."

    # Prepare the Markdown content
    readme_content = f"# Analysis of {file_path}\n\n"
    
    # Add the context and tables
    readme_content += "## Summary Statistics\n\n"
    summary_str = context['summary'].to_string()
    readme_content += f"```\n{summary_str}\n```\n"

    readme_content += "## Missing Values\n\n"
    missing_values_str = json.dumps(context['missing_values'], indent=2)
    readme_content += f"```\n{missing_values_str}\n```\n"
    
    # Write the generated narrative and analysis details to README
    readme_content += "## Insights\n\n"
    readme_content += story
    
    # Save the generated analysis to the README file
    try:
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        print(f"Narrative saved to {readme_file}")
    except Exception as e:
        print(f"Error saving README: {e}")


if __name__ == "__main__":
    # Get file paths from command-line arguments
    if len(sys.argv) < 2:
        print("Usage: uv run autolysis.py <file1.csv> <file2.csv> ...")
        sys.exit(1)

    file_paths = sys.argv[1:]

    for file_path in file_paths:
        if os.path.exists(file_path):
            print(f"\nAnalyzing: {file_path}")
            context = analyze_csv(file_path)
            if context:
                narrate_analysis(context, file_path)
        else:
            print(f"File not found: {file_path}")
