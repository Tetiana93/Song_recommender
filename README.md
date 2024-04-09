Song Recommender App

Overview
The Song Recommender App is a web application built using Streamlit that recommends similar songs based on the input song provided by the user. It utilizes the Spotify API to fetch audio features of songs and a machine learning model to determine similar songs.

How to Use
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd song-recommender-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain Spotify API credentials:
   - Sign up for a Spotify Developer account and create a new app.
   - Obtain your Client ID and Client Secret.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Enter your Spotify Client ID and Client Secret in the provided input fields.
   
6. Enter the name of a song and its artist in the input field.
   
7. Click the "Recommend" button to get similar song recommendations.

File Structure
- app.py: Contains the Streamlit application code for the user interface.
- helpers.py: Contains helper functions for fetching song recommendations using the Spotify API and machine learning models.
- data/: Directory containing preprocessed data and model files.
  - scaled_songs.csv: CSV file containing scaled audio features of songs.
  - scaler.pkl: Pickle file containing the scaler used for scaling audio features.
  - kmeans.pkl: Pickle file containing the KMeans clustering model for song recommendation.

Technologies Used
- Python
- Streamlit
- Spotipy (Spotify API wrapper)
- Scikit-learn (for machine learning)

Acknowledgements
This project was built as a part of Ironhack Data Analitics cource.

License
[MIT License](LICENSE)
