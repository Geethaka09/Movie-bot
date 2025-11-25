#  Gemini Movie Buff Agent

This project demonstrates how to connect **Google's Gemini 1.5 Flash** to real-world data sources using **Function Calling (Tool Use)**.

Unlike a standard chatbot that creates fiction, this agent retrieves factual, real-time data from the **OMDb API**, filters it for relevance, and synthesizes a natural language response.

##  Features

* **Autonomous Tool Use:** The AI detects when it needs external information (e.g., "Who is the director?") and automatically triggers a Python function.
* **Data Filtering Logic:** Implements a middleware layer that parses raw JSON from the API and extracts only relevant fields (Title, Director, Rating) to save token costs and improve accuracy.
* **Contextual Awareness:** Uses Gemini 1.5 Flash to understand natural language queries like *"Is Inception highly rated?"* and answer based on fetched data.
* **Secure Configuration:** Uses environment variables (`.env`) for API key management.

##  Tech Stack

* **Language:** Python 3.x
* **AI Model:** Google Gemini 1.5 Flash (via `google-generativeai`)
* **Data Source:** OMDb API (Open Movie Database)
* **Utilities:** `requests` (HTTP calls), `python-dotenv` (Security)

##  Architecture

The agent follows a "Brain, Hands, Filter" architecture:

1.  **The Brain (Gemini):** Receives the user prompt. If facts are needed, it pauses generation and requests a tool execution.
2.  **The Hands (Python Function):** Connects to the OMDb API endpoint.
3.  **The Filter:** Cleans the massive JSON response, removing noise (like Plot, Writer, BoxOffice) and returning only the requested data points to the Brain.

##  Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/movie-buff-agent.git](https://github.com/your-username/movie-buff-agent.git)
    cd movie-buff-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Keys:**
    Create a `.env` file in the root directory and add your keys:
    ```env
    GEMINI_API_KEY=your_google_api_key_here
    OMDB_API_KEY=your_omdb_key_here
    ```

4.  **Run the Agent:**
    ```bash
    python movie_bot.py
    ```

##  Example Interaction

```text
User: Who directed Interstellar and what year was it released?

[System Log] 🤖 Using Tool: Searching for 'Interstellar'...

Bot: Interstellar was directed by Christopher Nolan and released in 2014.
