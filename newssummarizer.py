from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

search_tool = TavilySearch(max_result = 5, topic="news")

llm = ChatMistralAI(model = "mistral-small-2506")

prompt = ChatPromptTemplate.from_template(
    """

    You are an AI-powered news summarization assistant.
    Your task is to convert lengthy breaking news articles into a single informative line that allows users to understand the complete story in under 10 seconds.
    Guidelines:
    - Maximum 50 words.
    - Include the main event.
    - Mention important entities if relevant.
    - Explain the impact or significance.
    - No bullet points.
    - No extra text.
    - Output only one sentence.
    
    News :
    {news}

    """
)

chain = prompt | llm | StrOutputParser()

topic = input("Add your topic to get ONE-LINER News Summary! : ")

search_query = f"latest breaking news today about {topic}"

news_data = search_tool.run(search_query)

summary = chain.invoke({"news": news_data})

print("\nOne-Liner News:")
print(summary)