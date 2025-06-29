"""
AI Research Agent using LangChain and Ollama 🚀

📌 Description:
This is a basic AI-powered agent that takes a user query and responds using tools like:
- Wikipedia lookup
- DuckDuckGo web search
- A mock "save" action

The agent is powered by a local language model (e.g., `mistral`) via Ollama, and uses LangChain's tool-based agent framework.

⚙️ How to Run:
1. Install Ollama from https://ollama.com
2. Pull a model (example: `ollama run mistral`)
3. Create a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate
4. Install dependencies:
   pip install langchain langchain-community langchain-ollama wikipedia duckduckgo-search
5. Run the program:
   python main.py

💡 Tip:
If your system has low memory, you may switch to a lighter model like `llama2:7b`.

📝 Submitted by: MUFEEDHA ALIYAR | MAR ATHANASIUS COLLEGE OF ENGINEERING,KOTHAMANGALAM 
"""



# main.py
from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from tools import all_tools  # our tools from tools.py

# Load Ollama model
llm = OllamaLLM(model="mistral")  # or use "llama2:7b" if you face memory issues

# Initialize the agent
agent = initialize_agent(
    tools=all_tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # ✅ compatible with classic Tool
    verbose=True,
    handle_parsing_errors=True
)

# Ask user for input
query = input("🔎 What can I help you research? ")

# Run the agent
response = agent.invoke({"input": query})
print("\n🤖 Answer:", response["output"])
