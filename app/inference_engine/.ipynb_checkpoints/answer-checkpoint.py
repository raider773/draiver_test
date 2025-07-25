from app.agents.toolSelectorAgent import ToolSelectorAgent

API_KEY = "".strip() 
tool_agent = ToolSelectorAgent(api_key=API_KEY)

user_query = "What will the weather be in july?"
response = tool_agent.decide_tool(user_query)


print(response)