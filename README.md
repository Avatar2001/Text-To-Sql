Excellent — I’ll draft you a clean, professional `README.md` for a GitHub repository to showcase this **Text-to-SQL Generator using LangChain, Ollama, and Streamlit** project.

---

## 📂 Repository Structure Suggestion

You might want to organize your repo like this:

```
text-to-sql-ollama/
├── app.py                  # your Streamlit app (the code you posted)
├── testdb.sqlite           # your SQLite database (or .gitignore it if sensitive)
├── requirements.txt        # Python dependencies
└── README.md               # project documentation
```

---

## 📄 README.md

````markdown
# 📝 Text-to-SQL Generator with LangChain, Ollama, and Streamlit

A lightweight web app that converts natural language questions into executable SQL queries using LangChain, DeepSeek R1 via Ollama, and Streamlit. This enables non-technical users to interact with a database intuitively, without writing SQL code.

## 📸 Demo

![App Screenshot](link-to-screenshot-or-demo.gif)

---

## 📌 Features

- ✅ Extracts live database schema using SQLAlchemy.
- ✅ Converts natural language to SQL with a LangChain-Ollama integration.
- ✅ Clean, interactive Streamlit interface.
- ✅ Custom prompt template enforcing SQL-only output.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — for the web UI
- **LangChain** — to build LLM pipelines
- **Ollama** — running the `deepseek-r1:8b` model locally
- **SQLAlchemy** — to extract database schema
- **SQLite** — lightweight embedded database for demo

---

## 📦 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/yourusername/text-to-sql-ollama.git
cd text-to-sql-ollama
````

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Make sure [Ollama](https://ollama.com/) is installed and the `deepseek-r1:8b` model is pulled:

```bash
ollama pull deepseek-r1:8b
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

---

## 📝 How It Works

* **Schema Extraction:** SQLAlchemy inspects the SQLite database and extracts table and column names.
* **Prompt Template:** A strict LangChain prompt template ensures the model outputs *only SQL*.
* **LLM Chain:** Natural language query and schema are passed to the DeepSeek R1 model through LangChain and Ollama.
* **Streamlit UI:** Provides a simple text input area and displays the generated SQL query.

---

## 📂 Example Database Schema

```json
{
  "users": ["id", "name", "email"],
  "orders": ["id", "user_id", "product", "price"]
}
```

---

## 📑 Example Usage

**Input:**

> "Get the names of all users who placed an order over \$100"

**Generated SQL:**

```sql
SELECT u.name
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.price > 100;
```

---

## 🙌 Credits

* **[LangChain](https://python.langchain.com)**
* **[Ollama](https://ollama.com)**
* **[DeepSeek-R1](https://huggingface.co/deepseek-ai)**
* Special thanks to the open-source community ❤️

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

**Mohamed Sherif**
[LinkedIn](https://www.linkedin.com/in/mohamed-sherif-35a488195/) | [GitHub](https://github.com/Avatar2001)

---

## 🌟 Give this repo a ⭐ if you found it helpful!

````

---

## 📄 requirements.txt example

```text
streamlit
sqlalchemy
langchain
langchain-ollama
deepseek
ollama
````

---

## ✅ Final Step

If you’d like, I can bundle this whole thing into a `.zip` structure or generate the LICENSE file as well — just let me know. Would you like me to?
