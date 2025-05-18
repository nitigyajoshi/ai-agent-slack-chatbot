# from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOpenAI
# # load environment variables from .env file
# load_dotenv()
# # Define which LLM to use
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# # Define the agent
# output=llm.invoke("what would be the ai equivalent of hellow world")
# print(output)

# pip install openai

# from openai import OpenAI

# client = OpenAI(
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a haiku about ai"}
#   ]
# )

# print(completion.choices[0].message);
# 

# import os
# import google.generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import initialize_agent, AgentType
# from langchain.memory import ConversationBufferMemory
# # os.environ.get("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# model = genai.GenerativeModel('gemini-2.0-flash')
# response = model.generate_content("Tell me a short story about a cat who goes on an adventure.")
# print(response.text)

# # Step 2: Memory (Optional but recommended)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# # Step 3: Tools (empty for now)
# tools = []
# # Step 4: Create the agent
# agent = initialize_agent(
#     tools=tools,
#     llm=model,
#     agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
#     memory=memory,
#     verbose=True,
# )
# # Step 5: Run the agent
# response = agent.run("What is the AI equivalent of 'Hello World'?")
# print(response)


import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory

# Set your Gemini API Key
os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY")

# Use the correct LangChain-compatible LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

# Optional memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Tools (can add later)
tools = []

# Create the agent
# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
#     memory=memory,
#     verbose=True,
# )

# Run the agent
# response = agent.invoke({"input": "What is the AI equivalent of 'Hello World'?"})
# print(response)
def get_agent_response(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content
