from typing import Any, Callable

import dotenv
from langchain import agents, memory, prompts
from langchain_community.chat_models import openai

from langchain_sandbox import tools, templates


class Chat:
    def __init__(self, api_key: str = None, temperature: float = 0.0) -> None:
        dotenv.load_dotenv()

        llm: openai.ChatOpenAI = openai.ChatOpenAI(api_key=api_key, temperature=temperature)
        custom_tools: list[Callable] = [tools.get_total_cost_and_summary]
        prompt: prompts.BaseChatPromptTemplate = prompts.ChatPromptTemplate.from_messages(
            [
                ("system", templates.SYSTEM),
                prompts.MessagesPlaceholder("chat_history", optional=True),
                ("human", templates.HUMAN),
            ]
        )

        self.memory: memory.ConversationBufferMemory = memory.ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        self.agent_executor: agents.AgentExecutor = agents.AgentExecutor(
            agent=agents.create_structured_chat_agent(llm, custom_tools, prompt),
            tools=custom_tools,
            memory=self.memory,
            handle_parsing_errors=True,
            verbose=True,
        )

    def run(self, user_input: str) -> None:
        response: dict[str, Any] = self.agent_executor.invoke(
            {"input": user_input, "chat_history": self.memory.buffer_as_str}
        )
        print("AI:", response["output"])
