import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

# load env
load_dotenv()

# page config
st.set_page_config(page_title="AI Chef", page_icon="👨‍🍳")

st.title("👨‍🍳 AI Chef Chat")

# init model
llm = init_chat_model(
    "google_genai:gemini-2.5-flash-lite",
    temperature=0.7
)

# create agent (once)
if "agent" not in st.session_state:
    st.session_state.agent = create_agent(
        llm,
        system_prompt="""
You are a professional chef.

- Talk like a chef
- Be friendly and confident
- Give cooking tips
- Remember conversation
- If user asks for short → be concise
- If detailed → explain step by step
""",
        checkpointer=InMemorySaver()
    )

# session id
THREAD_ID = "chef-thread-1"

# chat history UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# input
user_input = st.chat_input("Ask the Chef...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # call AI
    res = st.session_state.agent.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config={"configurable": {"thread_id": THREAD_ID}}
    )

    reply = res["messages"][-1].content

    # show AI reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

# Bye button
if st.button("👋 Bye"):
    st.session_state.messages = []
    st.success("Session ended. Bye Chef 👨‍🍳")
    st.stop()