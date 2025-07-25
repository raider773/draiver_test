import anthropic
from app.conf.settings import Settings

settings = Settings()

class QuestionAnswerAgent:
    def __init__(self,api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = settings.question_answer__agent_model
        self.max_tokens = settings.question_answer__agent_max_tokens
        self.temperature = settings.question_answer__agent_temperature
        self.knowledge_prompt = settings.question_answer__agent_prompt

        

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

    def answer_user(self, query: str, tool_output: str, context: str, user_chat_history: str) -> str:
        llm_input = self.knowledge_prompt.format(query=query, tool_output=tool_output, context=context, user_chat_history = user_chat_history)
        response = self._call_anthropic(llm_input)
        return response
        