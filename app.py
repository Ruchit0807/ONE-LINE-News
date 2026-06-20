import streamlit as st
from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.set_page_config(
page_title="ONE-LINE News",
page_icon="📰",
layout="wide"
)


st.markdown("""

""", unsafe_allow_html=True)


search_tool = TavilySearch(
max_result=5,
topic="news"
)

llm = ChatMistralAI(
model="mistral-small-2506"
)

prompt = ChatPromptTemplate.from_template(
"""
You are an AI-powered news summarization assistant.

Convert the provided news into ONE concise sentence.

Rules:

Maximum 50 words.
Mention key entities.
Explain significance.
No bullet points.
No extra text.
One sentence only.

News:
{news}
"""
)

chain = prompt | llm | StrOutputParser()



st.sidebar.title("📜 Search History")

if "history" not in st.session_state:
    st.session_state.history = []

for item in st.session_state.history[::-1]:
    st.sidebar.write("• " + item)



st.markdown(
"ONE-LINE NEWS",
unsafe_allow_html=True
)

st.markdown(
"Understand the world's biggest stories in under 10 seconds.",
unsafe_allow_html=True
)



st.markdown("### 🔥 Trending Topics")

col1,col2,col3,col4,col5,col6 = st.columns(6)

topics = [
"AI",
"Tesla",
"India",
"Cricket",
"Startups",
"Finance"
]

selected_topic = None

cols = [col1, col2, col3, col4, col5, col6]
for i, topic_name in enumerate(topics):
    if cols[i].button(topic_name):
        selected_topic = topic_name



user_topic = st.text_input(
"Search any topic",
placeholder="AI, Tesla, SpaceX, Cricket, India..."
)

if selected_topic:
    user_topic = selected_topic



if st.button("🚀 Generate One-Liner", use_container_width=True):
    if user_topic:
        st.session_state.history.append(user_topic)

        with st.spinner("Scanning latest news..."):
            query = f"latest breaking news today about {user_topic}"
            news_data = search_tool.run(query)
            summary = chain.invoke({"news": news_data})

        st.markdown("## 📰 One-Line Summary")
        st.markdown(
            f"""
            <div class="summary-card">
            {summary}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.code(summary)
    else:
        st.warning("Please enter a topic.")


st.markdown("", unsafe_allow_html=True)

st.markdown(
"""


Built with LangChain + Tavily + Mistral AI


""",
unsafe_allow_html=True
)
