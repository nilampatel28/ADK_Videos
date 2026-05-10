import os
import sys
sys.path.append("..")
import google.cloud.logging

from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool # import

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv

load_dotenv()
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

root_agent = Agent(
    name="External_lanchgain_tool_agent",
    model=os.getenv("MODEL"),
    description="Answers questions using Wikipedia.",
    instruction="""You are a helpful AI research assistant.

Your responsibilities:
1. Use the Wikipedia tool to research the user's query.
2. Provide accurate and concise summaries.
3. Highlight important facts, achievements, or historical relevance.
4. Keep responses easy to understand.
5. If information is unavailable, clearly say so.
Always provide professional and informative answers.""",
    tools = [
        LangchainTool(
            tool=WikipediaQueryRun(
              api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)
