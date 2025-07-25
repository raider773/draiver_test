class Settings:
    def __init__(self):


        self.chunk_size = 100
        self.chunk_overlap = 50

        #Tool Agent        
        self.tool__agent_model: str = "claude-sonnet-4-20250514"
        self.tool__agent_max_tokens: int = 1024
        self.tool__agent_temperature: float = 0.2
        self.tool__agent_prompt : str =  """                                                               
                                        You are a tool selector agent.
                                                                
                                        Given a user query, decide whether a tool should be used.
                                                                
                                         You have access to two tools:
                                                                
                                        1. `get_france_weather(date: str)`  
                                           - Use this if the user asks about the weather.
                                           - Extract the date or month mentioned by the user.
                                        
                                        2. `make_reservation(activity: str, date: str)`  
                                           - Use this if the user wants to book or reserve a visit to an attraction or activity.
                                           - Extract both the activity and the date or month.
                                        
                                        If the user query does not require using a tool, respond with:
                                        {{
                                          "tool": "none"
                                        }}
                                        
                                        Your output **must** be a valid JSON object in this format:
                                        
                                        - For weather:
                                        {{
                                          "tool": "get_weather",
                                          "parameters": {{
                                            "date": "..."  // e.g. "August" or "2025-08"
                                          }}
                                        }}
                                        
                                        - For reservations:
                                        {{
                                          "tool": "make_reservation",
                                          "parameters": {{
                                            "activity": "...",  // e.g. "Eiffel Tower"
                                            "date": "..."       // e.g. "September" or "next weekend"
                                          }}
                                        }}
                                        
                                        - For no tool:
                                        {{
                                          "tool": "none"
                                        }}
                                        
                                        Only respond with JSON. Do not add any explanation.
                                        
                                        User query: {query}
                                        """
        #QA Agent
        self.question_answer__agent_model: str = "claude-sonnet-4-20250514"
        self.question_answer__agent_max_tokens: int = 1024
        self.question_answer__agent_temperature: float = 0.2
        self.question_answer__agent_prompt : str =  """
                                                    You are a helpful assistant.
                                                    
                                                    Here is the ongoing conversation history between you and the user:
                                                    {user_chat_history}
                                                    
                                                    You are given:
                                                    - A user query
                                                    - Retrieved knowledge documents (if any)
                                                    - Tool output (if any tools were used)
                                                    
                                                    Use all relevant information to answer the user's query clearly and helpfully.
                                                    
                                                    If the tool output provides a direct answer, you can use it. If the context helps clarify or expand on the answer, include it. If neither helps, use your own reasoning.
                                                    
                                                    User Query:
                                                    {query}
                                                    
                                                    Tool Output:
                                                    {tool_output}
                                                    
                                                    Retrieved Context:
                                                    {context}
                                                    
                                                    Answer the user's query:
                                                    """






        