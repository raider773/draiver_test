import os
import pickle
from app.agents.toolSelectorAgent import ToolSelectorAgent
from app.agents.questionAnswerAgent import QuestionAnswerAgent
from app.utils.utils import get_france_weather, make_reservation, format_history, search_similar_docs

API_KEY = ""
tool_agent = ToolSelectorAgent(api_key=API_KEY)
qa_agent = QuestionAnswerAgent(api_key=API_KEY)

#user_query = "What will the weather be in july?"
#user_query = "Book me a place in effeil tower in august"
user_query = "Where can I get a coffee in Paris?"
session_id = 1

#Get user chat
session_file = f"app/knowledge_base/chat_user_{session_id}.pkl"
if os.path.exists(session_file):
    with open(session_file, "rb") as f:
        history = pickle.load(f)
else:
    history = []
formatted_history = format_history(history) if history else "User has no chat history."

print(formatted_history)

#Tool Agent
tool_information = "No extra information needed"
tool_response = tool_agent.decide_tool(user_query)   

if tool_response["tool"] == "get_weather":
    tool_information = get_france_weather(tool_response["parameters"]["date"])

elif tool_response["tool"] == "make_reservation":
    tool_information = make_reservation(tool_response["parameters"]["activity"],tool_response["parameters"]["date"])


#Context 
docs = search_similar_docs(user_query)
context = "\n\n".join(docs)


#QA Agent
answer = qa_agent.answer_user(query = user_query, tool_output = tool_information, context = context, user_chat_history = formatted_history)

# Save history
history.append({"role": "user", "content": user_query})
history.append({"role": "assistant", "content": answer})
os.makedirs(os.path.dirname(session_file), exist_ok=True)
with open(session_file, "wb") as f:
    pickle.dump(history, f)

print(answer)



