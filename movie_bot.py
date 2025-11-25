import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# --- SETUP ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
omdb_key = os.getenv("OMDB_API_KEY")

# --- THE HANDS & FILTER ---
def get_movie_data(movie_title: str):
    """
    Retrieves the Director, Year, and IMDB Rating of a movie.
    """
    print(f"\n[System] 🤖 Using Tool: Searching for '{movie_title}'...") # Debug logic
    
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={omdb_key}"
    data = requests.get(url).json()

    if data.get("Response") == "False":
        return {"error": "Movie not found"}

    # The Filter
    return {
        "Title": data.get("Title"),
        "Director": data.get("Director"),
        "Rating": data.get("imdbRating"),
        "Year": data.get("Year")
    }

# --- THE BRAIN ---
# We pack our tool into a toolbox (list)
my_toolbox = [get_movie_data]

model = genai.GenerativeModel(
    'gemini-2.0-flash-001',
    tools=my_toolbox # <--- We hand the toolbox to the brain
)

# We enable "Automatic Function Calling"
# Logic: This allows the code to loop: Gemini asks -> Python runs -> Gemini answers
chat = model.start_chat(enable_automatic_function_calling=True)

# --- THE INTERFACE ---
while True:
    user = input("You: ")
    if user == "quit": break
    

    response = chat.send_message(user)
    print("Bot:", response.text)