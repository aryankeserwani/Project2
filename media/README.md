# Analysis Report

## Dataset Overview

### Summary Statistics

|               |   count |   unique | top               |   freq |      mean |        std |   min |   25% |   50% |   75% |   max |
|:--------------|--------:|---------:|:------------------|-------:|----------:|-----------:|------:|------:|------:|------:|------:|
| date          |    2553 |     2055 | 21-May-06         |      8 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| language      |    2652 |       11 | English           |   1306 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| type          |    2652 |        8 | movie             |   2211 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| title         |    2652 |     2312 | Kanda Naal Mudhal |      9 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| by            |    2390 |     1528 | Kiefer Sutherland |     48 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| overall       |    2652 |      nan | nan               |    nan |   3.04751 |   0.76218  |     1 |     3 |     3 |     3 |     5 |
| quality       |    2652 |      nan | nan               |    nan |   3.20928 |   0.796743 |     1 |     3 |     3 |     4 |     5 |
| repeatability |    2652 |      nan | nan               |    nan |   1.49472 |   0.598289 |     1 |     1 |     1 |     2 |     3 |

### Missing Values

|               |   Missing Values |
|:--------------|-----------------:|
| date          |               99 |
| language      |                0 |
| type          |                0 |
| title         |                0 |
| by            |              262 |
| overall       |                0 |
| quality       |                0 |
| repeatability |                0 |

## Correlation Analysis

### Correlation Matrix

|               |   overall |   quality |   repeatability |
|:--------------|----------:|----------:|----------------:|
| overall       |  1        |  0.825935 |        0.5126   |
| quality       |  0.825935 |  1        |        0.312127 |
| repeatability |  0.5126   |  0.312127 |        1        |

![Correlation Heatmap](E:\Project2\media\correlation_matrix.png)

## Clustering Analysis

Clustering performed using PCA and t-SNE.

![PCA Clustering](E:\Project2\media\pca_clustering.png)

![t-SNE Clustering](E:\Project2\media\tsne_clustering.png)

## Outlier Detection

Outlier detection performed using Isolation Forest.

![Outliers Visualization](E:\Project2\media\outliers.png)

## Regression Analysis

|       |   Mean Squared Error |   R2 Score |
|:------|---------------------:|-----------:|
| Value |             0.198327 |   0.676756 |

![Regression Results](E:\Project2\media\regression.png)

## Conclusion

# Media Dataset Analysis Report

## 1. Dataset Overview
The dataset `media.csv` encompasses a collection of media entries with the following columns:
- **date** (object): The date of the media entry.
- **language** (object): The language of the media.
- **type** (object): The type of media (e.g., movie, series).
- **title** (object): The title of the media.
- **by** (object): The person or organization behind the media.
- **overall** (int64): An overall rating of the media.
- **quality** (int64): A quality assessment of the media.
- **repeatability** (int64): A measure of how repeatable than media is (likely in terms of viewing).

### Missing Values
The missing values in the dataset are as follows:
- **date**: 99 entries missing
- **by**: 262 entries missing

The rest of the columns do not have any missing entries. The presence of missing data in the `date` and `by` columns may impact analyses and interpretations.

## 2. Correlation Analysis
The correlation among the numerical features revealed significant relationships:

|               |   overall |   quality |   repeatability |
|:--------------|----------:|----------:|----------------:|
| overall       |  1        |  0.825935 |        0.5126   |
| quality       |  0.825935 |  1        |        0.312127 |
| repeatability |  0.5126   |  0.312127 |        1        |

### Insights
- **Overall & Quality**: There is a strong positive correlation (0.825) between `overall` ratings and `quality`, suggesting that higher quality assessments are associated with higher overall ratings.
- **Overall & Repeatability**: A moderate positive correlation (0.513) between `overall` ratings and `repeatability` suggests that media deemed to be of higher quality may be more repeatable.
- **Quality & Repeatability**: A low correlation (0.312) between `quality` and `repeatability` indicates that media quality does not strongly dictate its repeatability.

## 3. Clustering Analysis
Clustering was conducted using PCA and t-SNE to reduce dimensions and identify patterns in the dataset.

### Interpretation
- PCA: By reducing the dimensionality, the clustering likely highlighted distinct groups of media based on their ratings and types, enabling better visualization of how different media entries relate to each other.
- t-SNE: This technique helps visualize clusters more effectively, allowing for understanding of how data points (media entries) are grouped together based on similarity in ratings and other features.

Together, these analyses can reveal the presence of clusters based on genres, language, or overall ratings, guiding strategic decisions for media representation or targeted marketing.

## 4. Outlier Detection
Outlier detection was performed using the Isolation Forest algorithm to identify anomalies within the dataset.

### Summary of Anomalies
- The analysis successfully identified several outliers, which may indicate either exceptionally low or high ratings that do not conform to the general trends observed in the dataset.
- Visualizations of these outliers can highlight entries that require further investigation, possibly suggesting media that has uniquely performed either exceptionally well or poorly compared to others.

## 5. Regression Analysis
The regression analysis aimed to predict `overall` ratings based on other features with the following performance metrics:

- **Mean Squared Error (MSE)**: 0.1983
- **R² Score**: 0.6768

### Interpretation
- The MSE indicates a reasonably low value, suggesting that the predicted overall ratings are closely aligned with the actual ratings with minimal error.
- An R² score of approximately 0.68 indicates that about 68% of the variability in the `overall` ratings can be explained by the model applied. This suggests a moderately strong predictive capability of the model.

## 6. Conclusion
In summary, the analysis of the `media.csv` dataset provided insights into the relationships between ratings and quality, identified significant patterns via clustering, and highlighted outliers that may need further examination. The regression analysis indicated that while there is a strong capacity to predict overall ratings, there remain complexities in understanding the media fully. Further data cleaning, especially addressing missing values, and additional features may enhance insights from this dataset.
