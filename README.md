# 👨‍🍳 AI Chef Chatbot

An interactive AI-powered Chef chatbot built using **LangChain** and **Streamlit**.
The chatbot simulates a real chef with personality, memory, and controlled creativity.

---

## 🚀 Features

* 👨‍🍳 **Chef Personality**
  Talks like a real professional chef with a friendly and confident tone.

* 🧠 **Conversation Memory**
  Remembers previous interactions using session-based memory.

* 🎛️ **Controlled Creativity**
  Adjustable `temperature` for creative or precise responses.

* 💬 **Interactive Chat UI**
  Real-time chat interface built with Streamlit.

* 🔘 **Session Control**
  "Bye" button to end the conversation and reset chat history.

---

## 🛠️ Technologies Used

* Python
* LangChain
* LangGraph (Memory)
* Streamlit
* Google Gemini API (or OpenAI)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd <project-folder>
```

2. Create virtual environment:

```bash
python -m venv .venv
```

3. Activate environment:

* Windows (CMD):

```bash
.venv\Scripts\activate
```

* PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

### For Gemini:

```
GOOGLE_API_KEY=your_api_key_here
```

### For OpenAI:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run chef_app.py
```

Then open the browser link shown in terminal.

---

## 💡 How It Works

* Uses **LangChain Agent** to define chef behavior
* Uses **System Prompt** to enforce personality
* Uses **InMemorySaver** for conversation memory
* Uses **Streamlit** for chat interface

---

## 🎯 Example Prompts

* "I want a pasta recipe"
* "Give me a quick dinner idea"
* "Explain step by step how to cook rice"
* "Short recipe for omelette"

---

## 📌 Future Improvements

* 🎤 Voice interaction
* 🖼️ Food image generation
* 🥗 Diet-based recipes (Keto, Vegan, etc.)
* 📊 Recipe recommendation system

---

## 👩‍💻 Author

Shahd Abdulrahman

---

## ⭐ Notes

* Make sure your API key is valid
* Do not upload `.env` file to GitHub
* Add `.env` to `.gitignore`

---
