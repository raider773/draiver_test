from app.agents.toolSelectorAgent import ToolSelectorAgent
from app.agents.questionAnswerAgent import QuestionAnswerAgent
from app.utils.utils import get_france_weather, make_reservation
from app.utils.utils import search_similar_docs

API_KEY = "".strip() 
tool_agent = ToolSelectorAgent(api_key=API_KEY)
qa_agent = QuestionAnswerAgent(api_key=API_KEY)

#user_query = "What will the weather be in july?"
#user_query = "Book me a place in effeil tower in august"
user_query = "Where can I get a coffee in Paris?"


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
answer = qa_agent.answer_user(query = user_query, tool_output = tool_information, context = context)
print(answer)