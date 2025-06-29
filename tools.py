# tools.py
from langchain.agents import Tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper, WikipediaAPIWrapper

# DuckDuckGo search tool
search = DuckDuckGoSearchAPIWrapper()
search_tool = Tool(
    name="search_tool",
    func=search.run,
    description="Useful for questions about current events or the internet. Input should be a search query."
)

# Wikipedia tool
wiki = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="wiki_tool",
    func=wiki.run,
    description="Useful for general knowledge. Input should be a topic."
)

# Fake save tool
def fake_save(text):
    print(f"Saving: {text}")

save_tool = Tool(
    name="save_tool",
    func=fake_save,
    description="Pretend to save some input text. Input should be plain text."
)

# List of tools
all_tools = [search_tool, wiki_tool, save_tool]
