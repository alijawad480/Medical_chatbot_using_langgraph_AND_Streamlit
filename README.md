# Medical_chatbot_using_langgraph_AND_Streamlit
Medical AI Assistant
This repository contains a simple Medical AI Assistant powered by a HuggingFace large language model, built using langgraph and deployed with streamlit.
# Overview
The Medical AI Assistant allows users to interact with a chatbot that can answer medical queries. The backend handles the conversational logic and interaction with the LLM, while the frontend provides an intuitive chat interface.
# Features
Medical Q&A: Get responses to your medical questions from an AI model.
Conversational Memory: The chatbot maintains context within a session to provide more relevant answers.
Streamlit Interface: Easy-to-use web interface for interacting with the AI.
Getting Started
# Follow these steps to set up and run the Medical AI Assistant locally.
Prerequisites
Python 3.8+
pip (Python package installer)
Installation
Clone the repository:
Bash code
git clone https://github.com/your-username/medical-ai-assistant.git
cd medical-ai-assistant
Create a virtual environment (recommended):
python -m venv venv
On Windows: `venv\Scripts\activate`
Install dependencies:
# Create a requirements.txt file with the following content:

langgraph
langchain-core
langchain-community
langchain-huggingface
python-dotenv
streamlit
Then install:
pip install -r requirements.txt
Set up HuggingFace Token:
Create a .env file in the root of your project directory and add your HuggingFace API token. You can obtain one from the HuggingFace website.

HF_TOKEN="your_huggingface_api_token"
Ensure your token has permissions to access the GanjinZero/biollm-chat model.
Running the Application
# Start the Streamlit application:
streamlit run medical_chatbot-app.py
Open your web browser and navigate to the address provided by Streamlit (usually http://localhost:8501).
Architecture
The application is split into two main components:
madical_chatbot_backend.py:
Defines the core AI logic using langgraph.
Integrates with the GanjinZero/biollm-chat HuggingFace model.
Manages conversational state and message flow.
# medical_chatbot-app.py:
Implements the user interface using streamlit.
Handles user input and displays chatbot responses.
Connects to the backend logic to process queries.
Technologies Used
langgraph: For building robust, stateful multi-actor applications with LLMs.
langchain: For integrating with various LLMs and managing conversational components.
HuggingFace: Provides access to the GanjinZero/biollm-chat medical language model.
Streamlit: For creating interactive web applications with Python.
python-dotenv: For managing environment variables (HuggingFace API token).
# Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.
