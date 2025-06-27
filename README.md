


## 📄 Text-to-SQL Query Generator

An intelligent AI-powered tool built with **LangChain**, **Ollama**, and **Streamlit** to dynamically convert natural language queries into SQL statements based on a live database schema. This enables non-technical users to interact with relational databases intuitively through plain language prompts.

---

## 📖 Project Overview

**Text-to-SQL Query Generator** bridges the gap between natural language and structured query languages. By leveraging a local LLM via Ollama and real-time schema extraction with SQLAlchemy, this tool generates accurate, executable SQL queries from plain-text descriptions, displayed through a clean Streamlit interface.

---

## 🚀 Features

✅ Extract live database schema via SQLAlchemy
✅ Generate context-aware, SQL-only queries using DeepSeek-R1 LLM via Ollama
✅ Enforce clean, reliable prompt templates to avoid irrelevant responses
✅ Provide an intuitive, interactive frontend with Streamlit
✅ Clean the generated query output for safety and usability

---

## 🛠️ Tech Stack

* **Python**
* **LangChain** (Prompt management and LLM chaining)
* **Ollama** (Local LLM inference)
* **DeepSeek R1 8B** (LLM for query generation)
* **Streamlit** (Interactive web frontend)
* **SQLAlchemy** (Database schema inspection)
* **SQLite** (Demo relational database)

---

## 📝 System Architecture

**Components:**

* 📖 `Schema Extraction Module`: Inspects the connected SQLite database and retrieves table/column structure.
* 📝 `Prompt Template`: Defines strict instructions for SQL-only outputs from the model, based on the current schema and user question.
* 🧠 `LLM Query Generator`: Runs DeepSeek-R1 via Ollama with LangChain to produce SQL queries dynamically.
* 🖥️ `Streamlit UI`: Collects user questions and displays generated SQL queries interactively.
* 🧹 `Output Cleaner`: Removes unnecessary model artifacts (like `<think>` tags) from LLM outputs before displaying SQL.

---

## 📂 Project Structure

```
text-to-sql-ollama/
├── app.py                   # Streamlit web app
├── testdb.sqlite            # Demo SQLite database
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
```

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/text-to-sql-ollama.git
cd text-to-sql-ollama
```

2️⃣ **Install Python dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Install Ollama and Pull the LLM Model**

Download Ollama: [https://ollama.com](https://ollama.com)
Then pull the DeepSeek-R1 model:

```bash
ollama pull deepseek-r1:8b
```

4️⃣ **Run the application**

```bash
streamlit run app.py
```

---

## 📊 Example Use Case

Convert a plain-text request like:

> *“Get the names of all users who placed an order over \$100.”*

**Into an executable SQL query:**

```sql
SELECT u.name
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.price > 100;
```

Using the live schema from your connected database.

---

## 📄 Output

* **Generated SQL query**: Clean, ready-to-execute SQL displayed interactively via Streamlit
* **Database Schema**: Real-time schema extraction visible within the system
* **Prompt logs (optional)**: Can be extended to log prompts and responses

---

## 📃 Dependencies

Listed in `requirements.txt`

```
streamlit
sqlalchemy
langchain
langchain-ollama
ollama
deepseek
```

---

## 📬 Contact

**Mohamed Sherif**
[LinkedIn](https://www.linkedin.com/in/mohamed-sherif-35a488195/)
[GitHub](https://github.com/Avatar2001)

---

## 📖 License

This project is open-sourced under the MIT License. See the `LICENSE` file for details.

---

