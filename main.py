from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_MODEL")
    )
    
    prompt = "What is today's date?"
    response = llm.invoke(prompt)

    print(response.content)