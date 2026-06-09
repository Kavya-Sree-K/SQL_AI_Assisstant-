from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent

from database import db

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

def ask_database(question):

    response = agent_executor.invoke(
        {
            "input": question
        }
    )

    return response