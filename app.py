import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Main function of application
def main(): 
  page = st.sidebar.radio(" ", ["Home", "Anime Recommender System", "Model application"])

  # Page content according to the sidebar
  if page == "Home": 
    st.title("Anime Recommender System")
    st.write("Welcome to the Anime Recommender System!")
  elif page == "Anime Recommender System": 
    st.title("Model Logic")
    st.write("Description of model used")
# Streamlit UI
  elif page == "Model application":
    st.title("🎥 Anime Recommender System")
    st.write("Find the best anime based on your preferences!")

    # User Input (Search method for the anime movie/show)
    st.subheader ("Search or select your favourite anime")
    option_1 = st.text_input("Search Anime")

    # User Input (Drop menu selection for anime show/movie)
    # Sort by rating and select the top 10 anime
    df_anime = load_data()
    top_10_anime = df_anime.dropna(subset=["rating"]).sort_values(by="rating", ascending=False).head(10)
    # Extract the unique anime names from the top 10
    anime_list = top_10_anime["name"].unique()
    # User Input 
    selected_anime = st.selectbox("🔍 Select an Anime:", anime_list)
    
    
    # Recommendation Button
    if st.button("Get Recommendations 🎬"):
        recommendations = recommend_anime(selected_anime)
        
        if recommendations is not None:
            st.write("### 🎯 Recommended Anime for You:")
            st.table(recommendations)
        else:
            st.error("Anime not found in the dataset. Try another!")
    
        # Footer
    st.markdown("---")
    st.write("💡 Built with Streamlit | Anime Recommender Prototype")

# Load Anime Dataset (Replace with actual dataset path)
#@st.cache_data
def load_data():
    return pd.read_csv("anime.csv")  # Update with the actual dataset that will be used

    

# Recommendation Function (To be replaced with actual model - for collaborative and content based)
def recommend_anime(anime_name, top_n=5):
    if anime_name in df_anime["name"].values:
        recommendations = df_anime.sample(top_n)[["name", "genre", "rating"]]  # Replace with actual model logic
        return recommendations
    else:
        return None

main()
