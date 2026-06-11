# 🤖 SQL AI Assistant

An AI-powered database assistant that enables users to interact with a MySQL database using natural language. The application leverages Google Gemini, LangChain, SQLAlchemy, and Streamlit to automatically convert user questions into SQL queries, execute them on the database, and return meaningful results through an intuitive chat interface.

---

## 📌 Project Overview

SQL AI Assistant eliminates the need for users to write SQL queries manually. Users can simply ask questions in plain English, and the system automatically:

* Understands the user's intent
* Generates SQL queries using Gemini AI
* Executes queries on a MySQL database
* Retrieves and displays results
* Maintains query logs and analytics

This project demonstrates the integration of Generative AI with relational databases to create intelligent data retrieval systems.

---

## 🚀 Features

### Natural Language to SQL Conversion

Ask questions in plain English and automatically generate SQL queries.

### AI-Powered Query Processing

Uses Google Gemini and LangChain SQL Agent to understand and process user requests.

### MySQL Database Integration

Securely connects to MySQL databases using SQLAlchemy.

### Interactive Chat Interface

Provides a conversational experience through Streamlit.

### Database Schema Viewer

Displays table structures and schema information.

### Query Logging

Stores user questions and AI responses for auditing and analytics.

### Analytics Dashboard

Tracks:

* Total Queries
* Query History
* User Interaction Data

### Download Query Logs

Allows users to export query history as CSV files.

### Secure Configuration

Uses environment variables to protect API keys and database credentials.

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
LangChain SQL Agent
  │
  ▼
Google Gemini
  │
  ▼
SQL Query Generation
  │
  ▼
SQLAlchemy
  │
  ▼
MySQL Database
  │
  ▼
Query Results
  │
  ▼
Streamlit Dashboard
```

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM

* Google Gemini 2.5 Flash
* LangChain

### Database

* MySQL

### Database Connectivity

* SQLAlchemy
* PyMySQL

### Data Processing

* Pandas

### Configuration Management

* Python Dotenv

---

## 📂 Project Structure

```text
SQL_AI_Assistant/
│
├── app.py
├── database.py
├── sql_agent.py
├── query_logger.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── logs/
│   └── queries.csv
│
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Kavya-Sree-K/SQL_AI_Assisstant-.git
cd SQL_AI_Assisstant-
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GOOGLE_API_KEY=your_gemini_api_key

DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=CSV_DB
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will launch in your browser:

```text
http://localhost:8501
```

---

## 💬 Example Queries

Try asking:

```text
List comedy movies
```

```text
Show top rated movies
```

```text
Count movies by genre
```

```text
Movies released after 2020
```

```text
Show movies with rating greater than 8
```

---

## 📊 Analytics & Logging

The system automatically records:

* User Questions
* AI Responses
* Timestamp Information

Logs are stored in:

```text
logs/queries.csv
```

Users can view analytics directly from the dashboard and download query history as CSV.

---

## 🔒 Security Features

* API Keys stored using environment variables
* Database credentials protected via `.env`
* Sensitive files excluded using `.gitignore`
* Query logs separated from source code

---

## 🎯 Use Cases

* Business Intelligence Reporting
* Sales Analytics
* Inventory Management
* Educational Database Systems
* Healthcare Data Analysis
* Human Resource Analytics
* Customer Relationship Management

---

## 📈 Future Enhancements

* Multi-Database Support
* Role-Based Access Control
* Voice-Based Querying
* Query Visualization and Charts
* Query History Search
* Export Results to Excel and PDF
* User Authentication and Authorization

---

## 📄 License

This project is developed for educational and learning purposes.
