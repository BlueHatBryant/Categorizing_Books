# Book Categorization App
This is a Streamlit-based app that categorizes books into different clusters using machine learning techniques. The app takes in a dataset of books and uses K-Means clustering to group them into relevant categories based on book attributes like title, description, and author. The app also displays related topics and allows users to interactively explore the clustering results.

## Features
* Book Selection: Users can select a book from a dropdown list and view the predicted category for that book.
* Predicted vs Actual Category: Displays the predicted category (from the K-Means model) and the actual category from the dataset.
* Related Topics: Shows the top related topics to the selected book, with scores indicating the strength of the relationship.
* Cluster Overview: Displays human-readable names for each cluster, helping users understand what each cluster represents.
* Dynamic K Selection: Users can adjust the number of clusters (K) using a slider, allowing for customization based on dataset size and complexity.
* Clustering Performance: Displays visualizations of the Elbow Method and Silhouette Score to help determine the optimal number of clusters.

## Technologies Used
1. Python: The core programming language for the app.
2. Streamlit: For building the interactive web interface.
3. Scikit-learn: For implementing the K-Means clustering algorithm and calculating related terms.
4. Pandas: For handling the dataset and data manipulation.
5. Matplotlib: For visualizing the Elbow Method and Silhouette Score graphs.

## Disclaimer
Please note that the dataset currently being used in this project is not clean. It contains some inconsistencies, missing values, and possibly incorrect categorization. As a result, the model may produce some wrong answers or unexpected results. The accuracy of the categorization and related topics depends on the quality of the data, and improvements to the dataset may be necessary to achieve better results.

## Example
Predicting the Category of a Book:
Select a book from the dropdown menu.
The app will display the Predicted Category (Cluster) and the Actual Category.
It will also show related topics with scores indicating their relevance to the selected book.

### Cluster Overview:
The app will display the names of the clusters, such as:

Cluster 0: Programming
Cluster 1: Linux & Unix
Cluster 2: Web Development
Cluster 3: Security
Cluster 4: Data Science

### Potential Improvements
Refining Clusters: Use more advanced algorithms like DBSCAN or Agglomerative Clustering for better-defined groups.
Additional Features: Add more features like Pages, Language, or Year for clustering.

User Feedback: Implement a feedback loop where users can help label clusters to improve model accuracy.
Enhanced Visualizations: Add visual representations of clusters using t-SNE or PCA for better understanding.

## License
This project is licensed under the APACHE License - see the LICENSE file for details.