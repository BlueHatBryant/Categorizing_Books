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
