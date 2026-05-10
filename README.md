# Google ADK External Tools Agent

A Google Agent Development Kit (ADK) project demonstrating how to integrate third-party tools using LangChain and Wikipedia with Gemini models running on Vertex AI.

---

## Project Overview

This project showcases:

* Google ADK (Agent Development Kit)
* Gemini model integration using Vertex AI
* LangChain tool integration
* Wikipedia external knowledge retrieval
* Local ADK Web UI execution
* Tool calling and agent orchestration
* Google Cloud logging integration

The agent acts as an AI-powered research assistant capable of answering user questions by fetching information from Wikipedia and generating concise summaries using Gemini.

---

# Architecture

User Query
↓
Google ADK Agent
↓
LangChain Tool Wrapper
↓
Wikipedia API
↓
Retrieved Context
↓
Gemini Model (Vertex AI)
↓
Final Response

---

# Technologies Used

* Python 3.11
* Google ADK
* Vertex AI
* Gemini 2.0 Flash
* LangChain
* Wikipedia API Wrapper
* Google Cloud Logging
* dotenv

---

# Project Structure

```text
ADK_Videos/
│
├── Ext_Tools/
│   ├── __init__.py
│   ├── agent.py
│   ├── requirements.txt
│   └── .env
│
├── .gitignore
└── README.md
```

---

# Why the .env File Does Not Appear in GitHub

The `.env` file is intentionally excluded from Git tracking using `.gitignore`.

This is done for security reasons because `.env` files usually contain:

* API keys
* Cloud project IDs
* Authentication configuration
* Secrets and credentials

Your `.gitignore` contains:

```gitignore
.env
```

Because of this, Git will not upload the file to GitHub.

This is the recommended and professional practice.

---

# Environment Variables

Create a `.env` file inside the `Ext_Tools` directory.

Example:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=prj
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

# Installation Steps

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ADK_Videos
```

---

## 2. Create Virtual Environment

```bash
python3.11 -m venv venv
```

Activate:

macOS/Linux:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Authenticate with Google Cloud

```bash
gcloud auth application-default login
```

Set project:

```bash
gcloud config set project my-project1
```

Enable Vertex AI:

```bash
gcloud services enable aiplatform.googleapis.com
```

---

# Requirements

Example `requirements.txt`:

```txt
google-adk
langchain-community==0.3.28
wikipedia==1.4.0
python-dotenv
google-cloud-logging
```

---

# Agent Code

The agent:

* Loads environment variables
* Configures Google Cloud logging
* Initializes a Wikipedia LangChain tool
* Creates a Google ADK Agent
* Uses Gemini via Vertex AI

Main capabilities:

* Tool calling
* External knowledge retrieval
* Conversational interaction
* AI-generated summaries

---

# Running the Agent

Run the ADK Web UI:

```bash
adk web
```

Open:

```text
http://127.0.0.1:8000
```

---

# Example Prompts

Try asking:

```text
Who is Elon Musk?
```

```text
Who is Bill Gates?
```

```text
What is Kubernetes?
```

```text
Who founded Google?
```

---

# Features Demonstrated

* Google ADK Agent creation
* LangChain tool integration
* Wikipedia API integration
* Vertex AI model usage
* Gemini model invocation
* Cloud logging
* Tool orchestration
* Session execution tracing

---

# Common Issues Faced

## Python Version Compatibility

Python 3.14 caused dependency issues with several libraries.

Solution:

Use Python 3.11.

---

## Missing MODEL Variable

Error:

```text
ValidationError: model.str
```

Solution:

Add:

```env
MODEL=gemini-2.0-flash
```

inside `.env`.

---

## Vertex AI Authentication Issues

Solution:

Run:

```bash
gcloud auth application-default login
```

---

# Future Enhancements

Possible extensions:

* Web search tools
* Calculator tools
* Weather APIs
* Multi-agent orchestration
* Memory support
* Database integration
* DevOps automation tools
* RAG pipelines
* GCP operational assistants

---

# Learning Outcomes

This project demonstrates:

* Building AI agents using Google ADK
* Integrating third-party tools
* Using Gemini with Vertex AI
* Managing Python environments
* Handling cloud authentication
* Tool orchestration and execution tracing

---

# Author

Nilam Patel

DevOps | SRE | AI Engineering | GCP | Agentic AI

