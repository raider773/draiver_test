# draiver_test

# Chatbot with RAG and Tool Use

This project allows users to interact with a chatbot that combines **retrieval-augmented generation (RAG)** and external tool use (such as weather or reservation tools) to provide accurate and useful responses.

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

  