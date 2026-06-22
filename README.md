# 🛒 Multi-Agent Shopping Assistant

A production-style AI shopping assistant built using LangGraph, Streamlit, Groq, and SQLite.

The application uses a multi-agent workflow to search product data, retrieve relevant products, and generate intelligent recommendations based on user preferences.

---

## Features

### Search Agent

* Extracts product intent from user queries
* Detects price constraints
* Searches product database
* Supports follow-up conversations

### Recommendation Agent

* Analyzes retrieved products
* Considers price, rating, stock availability, and product details
* Generates personalized recommendations using LLM reasoning

### Conversation Support

* ChatGPT-style interface
* Maintains previous product context
* Handles follow-up questions such as:

  * Which one has the highest rating?
  * Why do you recommend that product?
  * Which option is cheaper?

---

## Architecture

User Question

↓

Search Agent

↓

SQLite Product Database

↓

Recommendation Agent

↓

Groq LLM

↓

Final Recommendation

---

## Tech Stack

### AI & Orchestration

* LangGraph
* LangChain
* Groq LLM

### Frontend

* Streamlit

### Database

* SQLite

### Backend

* Python

---

## Project Structure

shopping_agent/

├── agents/

│ ├── search_agent.py

│ └── recommendation_agent.py

├── database/

│ ├── store.db

│ └── set_up.py

├── prompts/

│ ├── search_agent_prompt.txt

│ └── recommendation_agent_prompt.txt

├── tools/

│ └── product_tools.py

├── utils/

│ └── config.py

├── workflows/

│ └── shopping_graph.py

├── app.py

├── main.py

├── requirements.txt

└── README.md

---

## Installation

Clone repository

```bash
git clone https://github.com/SaiKumarNune/shopping_agent.git

cd shopping_agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

Run application

```bash
streamlit run app.py
```

---

## Example Queries

```text
Find organic honey under $15
```

```text
Show tea products under $12
```

```text
Which one has the highest rating?
```

```text
Compare the available options
```

---

## Future Enhancements

* Memory-based conversations
* Vector database integration
* RAG-powered product knowledge retrieval
* Multi-store inventory support
* Agent routing and planning
* Order placement workflow
* MCP integration

---

## Author

Sai Kumar Nune

MS Computer Science

AI Engineer

GitHub: https://github.com/SaiKumarNune
