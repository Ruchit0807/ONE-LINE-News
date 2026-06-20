# 📰 ONE-LINE NEWS

**Understand the world's biggest stories in under 10 seconds.**

ONE-LINE NEWS is an AI-powered news summarization platform that transforms lengthy breaking news articles into a single informative sentence. By leveraging real-time web search and Large Language Models (LLMs), the application helps users stay updated without spending time reading full articles.

---

# https://onelinenews.streamlit.app/

## 🚀 Features

* 🔍 Real-time news retrieval using Tavily Search
* 🤖 AI-powered news summarization using Mistral AI
* ⚡ One-line summaries generated in seconds
* 📰 Latest and breaking news coverage
* 🎨 Modern Streamlit user interface
* 📜 Search history tracking
* 📱 Responsive and user-friendly design
* 🌐 Topic-based news exploration

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM

* Mistral AI
* LangChain

### Search & Retrieval

* Tavily Search API

### Environment Management

* Python Dotenv

---

## 📂 Project Structure

```bash
ONE-LINE-NEWS/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/one-line-news.git
cd one-line-news
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys Setup

This project requires:

* Tavily API Key
* Mistral AI API Key

Create a `.env` file in the root directory:

```env
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

After launching, open:

```text
http://localhost:8501
```

---

## 💡 How It Works

1. User enters a topic of interest.
2. Tavily Search retrieves the latest breaking news related to the topic.
3. LangChain orchestrates the workflow.
4. Mistral AI analyzes the retrieved content.
5. The system generates a concise one-line summary.
6. The summary is displayed through a modern Streamlit interface.

---

## 📸 Example

### User Input

```text
Artificial Intelligence
```

### Generated Summary

```text
Major AI companies unveiled advanced multimodal models, accelerating enterprise adoption while intensifying discussions around regulation, safety, and workforce impact.
```

---

## 🎯 Use Cases

* Daily news consumption
* Market monitoring
* Technology trend tracking
* Research and quick information gathering
* Students and professionals seeking rapid updates

---

## 🔮 Future Enhancements

* Multi-language summaries
* Voice-based search
* Trending news dashboard
* News sentiment analysis
* Personalized news recommendations
* Social media sharing integration
* Summary length customization
* News category filtering

---

## 📈 Resume Project Description

**ONE-LINE NEWS | LangChain, Mistral AI, Tavily Search, Streamlit**

Developed an AI-powered news summarization platform that retrieves real-time breaking news and generates concise one-line summaries using Retrieval-Augmented Generation (RAG), LangChain, Tavily Search, and Mistral AI, enabling users to consume news significantly faster through an intuitive Streamlit interface.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ruchit Sonawane**

Chemical Engineering Undergraduate | AI & Data Analytics Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
