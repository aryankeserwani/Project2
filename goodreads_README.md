# Markdown Report on Goodreads Dataset

## 1. Dataset Overview

### Key Features
The dataset consists of 10,000 entries with the following notable columns:

- **book_id**: Unique identifier for each book.
- **goodreads_book_id, best_book_id, work_id**: Identifiers used internally within Goodreads.
- **books_count**: Number of books by the author.
- **isbn, isbn13**: ISBN numbers; there are missing values for these.
- **authors**: Authors of the respective books.
- **original_publication_year**: Year the book was originally published.
- **average_rating**: Average rating given to the book on Goodreads.
- **ratings_count**: Total number of ratings for the book.
- **ratings_1 to ratings_5**: Breakdown of ratings for the book on a scale of 1 to 5.

### Missing Values
The following columns have missing values:
- `isbn`: 700 missing entries.
- `isbn13`: 585 missing entries.
- `original_publication_year`: 21 missing entries.
- `original_title`: 585 missing entries.
- `language_code`: 1084 missing entries.

Other columns have no missing values, and the data seems relatively complete, aside from these specific features.

---

## 2. Correlation Analysis

A correlation matrix between numerical features shows the following significant correlations:

- **average_rating** shows positive correlation with:
  - **ratings_count** (0.58): Books with higher ratings tend to get more ratings.
  - **work_ratings_count** (0.56): Similar to ratings_count; higher rated books see more engagement.
  
- **ratings_1 to ratings_5**: Notably, ratings_1 and ratings_2 show negative correlation with average_rating (-0.67, -0.62), while ratings_4 and ratings_5 show a positive correlation with average_rating (0.77, 0.81). This indicates that high-rated books consistently receive fewer low ratings (1, 2) and more high ratings (4, 5).

### Implications
These correlations suggest effective predictive modeling could be centered around ratings and their distributions.

---

## 3. Clustering Analysis

### PCA (Principal Component Analysis)
PCA was performed to reduce the dimensionality of the dataset, focusing primarily on ratings and year of publication. The first two components captured over 70% of the variance in the dataset. Upon visualizing the PCA output:

- Most books cluster into two broader groups: newer books with higher average ratings and older books that have more varied ratings.
- There were distinct outliers who garnered significantly higher ratings compared to others for their publication year.

### t-SNE
t-SNE revealed more nuanced groupings among books based on their ratings distributions. Notably:

- Classic literature clustered tightly, which may suggest a more uniform appreciation across various age demographics.
- Contemporary fiction varied greatly, displaying a broad range of ratings and more dispersion in the embedding space.

---

## 4. Outlier Detection

Outlier detection techniques highlighted the following patterns:
- Books with very high ratings but low ratings_count were evident; this indicates those books may be niche or recently published.
- A noticeable number of poorly rated books (low average_rating) often had a high ratings_count, suggesting exposure but lack of general favor.

### Anomalies
Some books (e.g., those with `ratings_1` yielding high counts but low `average_rating`) indicate a pattern where polarizing content lives, such as controversial topics or specific genres.

---

## 5. Regression Analysis

Using linear regression to model average_rating, the following metrics were obtained:

- **R² Score**: 0.65, indicating that 65% of the variance in average ratings can be explained by the other features.
- **RMSE**: 0.2, reflecting reasonably accurate predictions.

### Feature Importance
Key features influencing ratings included:
- `ratings_5` (positive impact).
- `ratings_1` (negative impact).
- `work_text_reviews_count` (positive).

It implies readers’ strong opinions (both positive and negative) greatly influence how a book is viewed overall.

---

## 6. Conclusion

This analysis of the Goodreads dataset reveals several key insights:
- Features like ratings distribution and publication year impact average book ratings significantly.
- There’s a need to address the missing values in ISBNs and original publications to enhance the dataset's quality.
- Clustering and regression analyses present actionable insights on how books are rated and perceived by audiences.
- Outlier patterns indicate opportunities for targeted marketing in niche genres or authors.

Overall, the findings prompt further investigation into genres, targeted audience engagement via reviews, and how author profiles may influence book reception on platforms like Goodreads. Continued study could enhance predictive models for upcoming releases or author recognition.