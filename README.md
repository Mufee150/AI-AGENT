# 🧠 AI Research Agent

This is a basic AI research assistant built using **LangChain** and **Ollama**. It allows users to input natural language questions and receive answers powered by open-source LLMs (like Mistral or LLaMA) with the ability to fetch data from the internet or Wikipedia.



---

## 🔧 Features

- 🧠 Powered by Ollama's local LLM (like `mistral` or `llama2`)
- 🌐 Internet search using DuckDuckGo
- 📚 General knowledge lookup using Wikipedia
- 📝 Save functionality simulation (fake save)
- 🗨️ Natural question-answer format using LangChain's Agent


## 🚀 How to Run

> 📌 Make sure you have Python, Git, and Ollama installed on your system.

### 

1. Clone the Repository

```bash
git clone https://github.com/Mufee150/AI-AGENT.git
cd AI-AGENT

2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
.\venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux

3. Install Required Packages

pip install -r requirements.txt

    If requirements.txt is missing, install manually:

pip install langchain langchain-community langchain-ollama duckduckgo-search wikipedia

4. Start Ollama (if not running already)

ollama run mistral

Or replace mistral with a smaller model like llama2 if you face memory issues.
5. Run the Agent

python main.py

Then type your question and hit Enter.


---

## 📁 Project Structure

AIAGENT/
├── main.py # The main Python file to run the agent
├── tools.py # Tool definitions like search and Wikipedia
├── README.md # Project documentation
└── requirements.txt # Python dependencies (create if needed)

---


---------------------------------------------------------------------------------------------------------------------------------------------------
👩‍💻 Author:
Mufeedha Aliyar
Mar Athanasius College of Engineering
GitHub: @Mufee150
