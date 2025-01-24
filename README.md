# **Fitness and Wellness Assistant**

## **Overview**
The **Fitness and Wellness Assistant** is a personalized tool designed to help users enhance their well-being by providing tailored mental wellness advice and fitness recommendations. It dynamically adjusts its suggestions based on factors such as mood, energy levels, fitness goals, and personal preferences, ensuring that each user receives a custom experience that evolves with their needs.

This project integrates cutting-edge technologies such as **Generative AI (RAG)** for real-time data retrieval, **Sentiment Analysis (NLP)** to assess user mood, and a robust **Personalization Engine** that adapts suggestions over time. With a user-friendly interface powered by **Streamlit** and real-time integration of weather data, the assistant makes personalized fitness recommendations that improve health and encourage regular activity.

## **Key Features**
1. **Dynamic Recommendation Engine**:
   - **Personalized Fitness Plans**: Tailored workout plans based on user mood, energy levels, fitness goals, and preferences (e.g., cardio, yoga, HIIT).
   - **Wellness Tips**: Offers hydration, nutrition, and mental wellness advice to promote overall health.
   - **Weather-Based Activity Suggestions**: Integrates real-time weather data (via OpenWeatherMap) to recommend outdoor exercises if the weather is favorable.

2. **User Input & Personalization**:
   - **Mood & Energy Level**: Users can input their emotional state and energy level, which adjusts the intensity of workout suggestions.
   - **Fitness Goals**: Users set personal goals (e.g., weight loss, strength building) to receive customized exercise routines.
   - **Exercise Preferences**: Users can specify preferred workout types (e.g., running, pilates, stretching) for more relevant recommendations.

3. **AI-Driven Insights**:
   - **Sentiment Analysis**: Analyzes user inputs (text or speech) to understand mood and adjust advice accordingly.
   - **Real-Time Content Retrieval (RAG)**: Uses **RAG** to pull the latest workout tutorials, health tips, and wellness content from trusted sources, keeping users engaged with fresh recommendations.

4. **Interactive UI**:
   - **Streamlit Interface**: Provides a simple yet interactive user interface that displays personalized recommendations, workout routines, and tips in an easy-to-understand format.
   - **Voice Recognition (Future)**: Planned feature for voice-based input in multiple languages, making the app more accessible and user-friendly.

## **Technologies Used**
- **LangChain**: For integrating RAG-based real-time content retrieval.
- **FastAPI**: For building the backend API to serve user requests efficiently.
- **Streamlit**: For building an interactive and responsive front-end.
- **SQLite3**: For storing user preferences, mood logs, and fitness data.
- **Sentiment Analysis (NLP)**: TextBlob/VADER for interpreting user mood based on input.
- **OpenWeatherMap API**: For fetching real-time weather data to dynamically suggest outdoor activities.
  
## **How It Works**
1. **User Interaction**: Users provide input about their mood, energy levels, fitness goals, and exercise preferences.
2. **Data Analysis**: Sentiment analysis interprets the user's mood and adjusts the intensity and type of suggested activities.
3. **Dynamic Suggestions**: Based on user data, weather conditions, and real-time content from trusted sources, the assistant recommends customized workout routines, wellness tips, and activities.
4. **Adaptability**: The system evolves based on user feedback and progress, continuously providing fresh, context-relevant recommendations.

## **Installation & Setup**
To run the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/fitness-wellness-assistant.git
   cd fitness-wellness-assistant
   pip install -r requirements.txt
   ```
2. Run the followign Commnads:
   ```
   uvicorn main:frontend --reload --port 8081
   streamlit run frontend/streamlit_app.py
   ```
3. Access the app through the browser at http://localhost:8501
