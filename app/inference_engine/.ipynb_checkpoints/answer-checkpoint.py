from app.agents.toolSelectorAgent import ToolSelectorAgent
from app.utils.utils import get_france_weather, make_reservation

API_KEY = "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".strip() 
tool_agent = ToolSelectorAgent(api_key=API_KEY)

#user_query = "What will the weather be in july?"
user_query = "Book me a place in effeil tower in august"


#Tool Agent
tool_information = "No extra information needed"
tool_response = tool_agent.decide_tool(user_query)   

if tool_response["tool"] == "get_weather":
    tool_information = get_france_weather(tool_response["parameters"]["date"])

elif tool_response["tool"] == "make_reservation":
    tool_information = make_reservation(tool_response["parameters"]["activity"],tool_response["parameters"]["date"])

