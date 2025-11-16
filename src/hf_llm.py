from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


load_dotenv()
llm = AzureChatOpenAI(azure_deployment="gpt-5-mini")