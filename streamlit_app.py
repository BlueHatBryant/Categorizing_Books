import streamlit as st
from utils.preprocess import load_and_preprocess
from utils.clustering import train_kmeans, get_top_terms

# Load dataset
file_path = "AllITBooks_DataSet.xlsx"
df, X, vectorizer = load_and_preprocess(file_path)

# Train K-Means
num_clusters = 5
kmeans, labels = train_kmeans(X, num_clusters)
df["Cluster"] = labels

# Get related topics with scores
top_topics = get_top_terms(kmeans, vectorizer)

# Streamlit UI
st.title("Book Categorization App")
df.columns = df.columns.str.strip()

# User selects a book
book_title = st.selectbox("Choose a book:", df["Book_name"])

# Get book details
book_info = df[df["Book_name"] == book_title].iloc[0]
predicted_category = book_info["Cluster"]
actual_category = book_info["Category"]
related_topics = top_topics[predicted_category]

# Display results
st.write(f"### Predicted Category: Cluster {predicted_category}")
st.write(f"**Actual Category:** {actual_category}")

# Show related topics with scores
st.write("**Related Topics:**")
for term, score in related_topics:
    st.write(f"- {term} (Score: {score:.4f})")

# Add cluster labels
cluster_labels = {
    0: "Programming",
    1: "Linux & Unix",
    2: "Web Development",
    3: "Machine Learning",
    4: "Cybersecurity"
}

# Display cluster names and numbers for reference
st.write("### Available Clusters")
st.write("These are the available clusters for reference:")

for cluster, label in cluster_labels.items():
    st.write(f"- **Cluster {cluster}**: {label}")
