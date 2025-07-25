# draiver_test

# Chatbot with RAG and Tool Use

This project allows users to interact with a chatbot that combines **retrieval-augmented generation (RAG)** and external tool usage (such as weather and reservation tools) to provide accurate and helpful responses for tourists visiting France. The `knowledge_base` contains summaries of activities and attractions to explore in France.


### Specific Scenarios Handled:
- **Weather Queries**: The agent can fetch weather data based on user requests (e.g., "What is the weather in Paris this August?").
- **Reservation Assistance**: The agent can assist with booking places for activities or events (e.g., "Book me a place at the Eiffel Tower").
- **General Information**: The agent can answer general queries based on its knowledge base and retrieved documents (e.g., "Where can I get a coffee in Paris?").


## 🛠 How to Set Up the Project

1. **Clone or Download the Project**  
   Ensure you have the project files on your local machine.

2. **Install Dependencies**  
   Inside the project folder, create a virtual environment and install the required dependencies:

   ```bash
   # Create virtual environment (if not done already)
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```
    
3. **Load data**

   
   If you need to load data

   
   ```bash
   python app/utils/data_loader.py

   ```

5. **Run API**

   To run the local server for the API, execute:

   ```bash   
   
   uvicorn main:app --reload

   ```

   You will need to provide an ANTHROPIC_API_KEY inside main.py

6. **Example Queries**

 Example 1: Weather Information
 User Query: "What is the weather like in Paris this August?"

 Explanation:
 This query will trigger the weather tool, and the system will return an answer with the relevant weather details for Paris in August.

 ```bash
    
 curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{
    "user_query": "What is the weather like in Paris this August?",
    "session_id": 1
  }'

  ```


  Example 2: Making a Reservation
  User Query: "Book me a place in the Eiffel Tower in August."

  Explanation:
  The agent will use the make_reservation tool to return booking details for the Eiffel Tower in the requested month.

  ```bash
  curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{
    "user_query": "Book me a place in the Eiffel Tower in August",
    "session_id": 1
  }'

  ```


  Example 3: General Query (Coffee in Paris)
  User Query: "Where can I get a coffee in Paris?"

  Explanation:
  This query may trigger the agent to search for relevant documents about coffee spots in Paris and provide a general response based on the knowledge base.

  ```bash

  curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{
    "user_query": "Where can I get a coffee in Paris?",
    "session_id": 1
  }

  ```

  