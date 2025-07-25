from app.agents.toolSelectorAgent import ToolSelectorAgent

API_KEY = "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".strip() 
tool_agent = ToolSelectorAgent(api_key=API_KEY)

user_query = "What will the weather be in july?"
response = tool_agent.decide_tool(user_query)


print(response)