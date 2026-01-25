# To install: pip install tavily-python
from tavily import TavilyClient
client = TavilyClient("")
response = client.crawl(
    url="",
    extract_depth="advanced"
)
print(response)