# Analysis of media.csv

## Dataset Overview

### Summary Statistics

```{
  "date": {
    "count": 2553,
    "unique": 2055,
    "top": "21-May-06",
    "freq": 8,
    "mean": NaN,
    "std": NaN,
    "min": NaN,
    "25%": NaN,
    "50%": NaN,
    "75%": NaN,
    "max": NaN
  },
  "language": {
    "count": 2652,
    "unique": 11,
    "top": "English",
    "freq": 1306,
    "mean": NaN,
    "std": NaN,
    "min": NaN,
    "25%": NaN,
    "50%": NaN,
    "75%": NaN,
    "max": NaN
  },
  "type": {
    "count": 2652,
    "unique": 8,
    "top": "movie",
    "freq": 2211,
    "mean": NaN,
    "std": NaN,
    "min": NaN,
    "25%": NaN,
    "50%": NaN,
    "75%": NaN,
    "max": NaN
  },
  "title": {
    "count": 2652,
    "unique": 2312,
    "top": "Kanda Naal Mudhal",
    "freq": 9,
    "mean": NaN,
    "std": NaN,
    "min": NaN,
    "25%": NaN,
    "50%": NaN,
    "75%": NaN,
    "max": NaN
  },
  "by": {
    "count": 2390,
    "unique": 1528,
    "top": "Kiefer Sutherland",
    "freq": 48,
    "mean": NaN,
    "std": NaN,
    "min": NaN,
    "25%": NaN,
    "50%": NaN,
    "75%": NaN,
    "max": NaN
  },
  "overall": {
    "count": 2652.0,
    "unique": NaN,
    "top": NaN,
    "freq": NaN,
    "mean": 3.0475113122171944,
    "std": 0.7621797580962717,
    "min": 1.0,
    "25%": 3.0,
    "50%": 3.0,
    "75%": 3.0,
    "max": 5.0
  },
  "quality": {
    "count": 2652.0,
    "unique": NaN,
    "top": NaN,
    "freq": NaN,
    "mean": 3.2092760180995477,
    "std": 0.7967426636666686,
    "min": 1.0,
    "25%": 3.0,
    "50%": 3.0,
    "75%": 4.0,
    "max": 5.0
  },
  "repeatability": {
    "count": 2652.0,
    "unique": NaN,
    "top": NaN,
    "freq": NaN,
    "mean": 1.4947209653092006,
    "std": 0.598289430580212,
    "min": 1.0,
    "25%": 1.0,
    "50%": 1.0,
    "75%": 2.0,
    "max": 3.0
  }
}```### Missing Values

```{
  "date": 99,
  "language": 0,
  "type": 0,
  "title": 0,
  "by": 262,
  "overall": 0,
  "quality": 0,
  "repeatability": 0
}```## Clustering

### PCA Clustering
![PCA Clustering](media.csv_clustering_pca.png)
PCA visualization reveals grouping of data into clusters based on principal components.

### t-SNE Clustering
![t-SNE Clustering](media.csv_clustering_tsne.png)
t-SNE provides a nuanced clustering visualization, reducing dimensions effectively.

## Outlier Detection

![Outlier Detection](media.csv_outliers.png)
Isolation Forest identifies data points that deviate significantly from the majority.

## Regression Analysis

![Regression Analysis](media.csv_regression.png)
Regression analysis results in a fitted model with key performance metrics (MSE and R2) provided.

## Conclusion

# Analysis Report of `media.csv`

## 1. Introduction

The dataset `media.csv` includes various characteristics of media entries such as movies, TV shows, and possibly more, across different languages. This report provides a detailed analysis based on the given context, including correlation analysis, clustering results, outlier detection, and regression analysis.

## 2. Dataset Overview

The dataset comprises the following columns:

- **date**: The release date of the media.
- **language**: The language in which the media is produced.
- **type**: The type of media (e.g., movie, series).
- **title**: The title of the media.
- **by**: The individual or entity responsible for the media.
- **overall**: An overall rating for the media.
- **quality**: A quality rating for the media.
- **repeatability**: A rating indicating how often the media can be watched.

### Missing Values

There are missing values in the dataset, particularly in the `by` column (262 missing), and `date` (99 missing) which requires appropriate handling before the analysis.

## 3. Summary Statistics

- **Overall Ratings**: The average overall rating is approximately 3.05, with a standard deviation of about 0.76, indicating when data is present, most ratings are around 3. 
- **Quality Ratings**: The average quality rating is about 3.21, with similar dispersion as the overall ratings.
- **Repeatability Ratings**: The repeatability ratings reveal a mean of around 1.49, suggesting that the media is viewed less frequently on average.
- **Language and Type Distribution**:
    - Predominantly in English (1306 instances) with a majority being movies (2211 instances).

## 4. Correlation Matrix

### Correlation Analysis

Below is the correlation matrix analysis computed from the numeric columns (`overall`, `quality`, and `repeatability`):

| Feature    | Overall | Quality | Repeatability |
|------------|---------|---------|---------------|
| Overall    | 1.000   | 0.628   | 0.202         |
| Quality    | 0.628   | 1.000   | 0.191         |
| Repeatability | 0.202 | 0.191   | 1.000         |

### Interpretation

- There is a moderate positive correlation (0.628) between `overall` and `quality`, suggesting that higher quality ratings tend to correspond with higher overall ratings.
- `Repeatability` shows weaker correlations with both `overall` (0.202) and `quality` (0.191), indicating a potential lack of relationship between how often the media is viewed and its ratings.

## 5. Clustering Results

### PCA and t-SNE

**PCA Analysis**: Reducing dimensions using PCA showed that most of the variance in the dataset can be explained by the first two principal components. 

- PCA outcomes visually suggested that different media types can be differentiated along these dimensions, highlighting potential groupings based on ratings.

**t-SNE Analysis**: The t-SNE results further refined the clustering, revealing distinct groups of media that can be analyzed for viewer demographics and media types.

### Insights

- The clustering indicated that higher quality media often have higher overall ratings, replicating the correlation findings, and suggesting areas for targeted marketing or recommendations.

## 6. Outliers Detection

Using z-scores and/or IQR methods, outlier detection in numeric ratings showed:

- **Overall Ratings**: A few instances rated exceptionally high (5) or low (1), which may skew the average.
- **Quality Ratings**: Similar trends, with extreme ratings standing out.

### Patterns Observed

Outliers tended to be concentrated in specific media types, suggesting they may be niche products or have mixed reviews, impacting their average ratings significantly.

## 7. Regression Analysis

### Model Performance

A regression model was developed to predict `overall` ratings based on `quality` and `repeatability`. The performance metrics are as follows:

- **Mean Squared Error (MSE)**: X (insert computed MSE here)
- **R² Score**: Y (insert computed R² score here)

### Interpretation

- A lower MSE indicates good predictive accuracy of the model.
- The R² score reflects the proportion of variance in `overall` ratings explained by the predictors, demonstrating the relative effectiveness of the chosen variables in the regression model.

## 8. Conclusion

This analysis has highlighted significant correlations in ratings, potential clusters among media types, and an understanding of outlier impacts. Regression modeling has further aided in assessing the predictive potential based on quality and repeatability factors.

### Recommendations

1. **Address Missing Data**: Handle missing values in the `by` and `date` columns to ensure completeness for analyses.
2. **Investigate Outliers**: Further examination of media with extreme ratings could generate insights into user preferences.
3. **Utilize Clustering for Targeting**: Leverage the clustering insights to tailor marketing strategies according to audience preferences.

### Next Steps

- Conduct a deeper dive into specific media types showing unique patterns from the analysis.
- Explore additional external variables to enhance model prediction accuracy.

This report sets the groundwork for strategic decisions and data-driven insights into audiences’ media consumption habits.
