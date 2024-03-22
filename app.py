from fastapi import FastAPI
from langchain.prompts import ChatMessagePromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
# load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title='Langchain Server',
    version='3.6.9',
    description='API Langserver'
)

add_routes(
           app,
           ChatOpenAI(),
           path="/openai")

model=ChatOpenAI()
prompt1=ChatPromptTemplate.from_template('provide me essay about topic {topic}')
prompt2=ChatPromptTemplate.from_template('provide me poem about topic {topic}')

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost",port=8000)