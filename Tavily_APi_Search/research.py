from tavily import TavilyClient

tavily_client = TavilyClient(api_key="")

# Start a research task
response = tavily_client.research("What are the latest developments in AI?")

# Get the request ID
request_id = response.get("request_id")

# Poll for results
while True:
    result = tavily_client.get_research_result(request_id)
    if result.get("status") == "completed":
        print(result.get("content"))  # The research report
        print(result.get("sources"))  # List of sources
        break
    elif result.get("status") == "failed":
        print("Research failed")
        break