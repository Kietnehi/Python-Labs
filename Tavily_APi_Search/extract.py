# To install: pip install tavily-python
from tavily import TavilyClient
client = TavilyClient("")
response = client.extract(
    urls=[""]
)
print(response)