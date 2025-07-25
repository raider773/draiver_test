import anthropic
from app.conf.settings import Settings
import json

settings = Settings()


class ToolSelectorAgent:
    def __init__(self,api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = settings.tool__agent_model
        self.max_tokens = settings.tool__agent_max_tokens
        self.temperature = settings.tool__agent_temperature
        self.knowledge_prompt = settings.tool__agent_prompt

        

    def _call_anthropic(self, query: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        return response.content[0].text

    def decide_tool(self, query: str) -> str:
        llm_input = self.knowledge_prompt.format(query=query)
        raw = self._call_anthropic(llm_input)
        try:
            data = json.loads(raw)        
            return data
        except json.JSONDecodeError:
            print("[WARN] Failed to parse tool selection response:", raw)
            return "none"