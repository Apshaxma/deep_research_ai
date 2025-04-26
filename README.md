# Deep Research AI Agentic System

This project implements a **Deep Research AI System** using **LangGraph**, **LangChain**, and **Tavily API** (web search).  
It is designed for the **Kairon Qualifying Assignment** — submitted by Ashutosh Sharma.

---

**Code Preview**-

-TO see the Demonstration of the code In an Streamlit App 
-Click On this Link : https://deepresearchai-01.streamlit.app/

---

## 🚀 Project Overview

- **Dual-Agent Architecture**:
  - **Research Agent**: Gathers and summarizes online information from Tavily search.
  - **Drafting Agent**: Structures the summary into a complete, final answer.

- **Frameworks Used**:
  - `LangGraph`: Manages multi-step workflows.
  - `LangChain`: Connects LLM models, chains, and tools.
  - `Tavily API`: Web crawling and search tool.
  - `Google Generative AI API`: Used for summarization and drafting.

- **User Interaction**:
  - Takes a user question as input.
  - Returns a deep-researched, drafted final answer.

---

## ⚙️ Project Structure

| File | Description |
|:----|:------------|
| `main.py` | Main code for the agent graph and user interaction |
| `requirements.txt` | All required libraries |
| `explanation.pdf` | Project explanation document |

---

## 🛠 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/apshaxma/deep-research-ai.git
cd deep-research-ai
