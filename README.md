# RAG-LLM-PROJECT

# GreenGuard Techno-Bot

Welcome to GreenGuard Techno-Bot, an intelligent chatbot designed to help visitors and staff navigate the rules and regulations of our public park. This project is part of the IBM SkillsBuild Internship for AICTE EduNet.

## Overview

GreenGuard Techno-Bot is an AI-powered FAQ system that provides quick and accurate answers to questions about park policies, rules, and regulations. Leveraging the power of Google Palm LLM, HuggingFace embeddings, and FAISS vector stores, GreenGuard Techno-Bot ensures that users have access to reliable information at their fingertips.

<img width="981" alt="image" src="https://github.com/user-attachments/assets/03da3db8-5cbb-45a3-98f6-7bc5f3ef4394">



## Features

- **Intelligent Query Handling:** Uses advanced language models to understand and respond to user queries.
- **Comprehensive Knowledge Base:** Covers a wide range of topics related to campus rules and regulations.
- **Interactive Interface:** Built with Streamlit for an engaging user experience.
- **Scalable and Extendable:** Designed to be easily extendable with additional documents and data sources.

## Project Structure

- `Helper.py`: Contains functions for creating the vector database and setting up the QA chain.
- `Main.py`: The main entry point for the Streamlit application.
- `rules.txt`: Contains the rules and regulations document used for creating the vector database.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- HuggingFace Transformers
- FAISS
- Google API Key

Note: Use .env file to store your API Key.
