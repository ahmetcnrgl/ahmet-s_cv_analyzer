import streamlit as st
from native_implement.answer import answer as answer_native
from langchain_implement.answer import answer_cv_question as answer_langchain

st.set_page_config(page_title="Ahmet's CV Analyzer", layout="wide")

st.markdown(
    """
    <style>
    .user-message {
        display: flex;
        justify-content: flex-end;
        margin: 8px 0;
    }
    .user-bubble {
        background-color: #DCF2FF;
        color: #000000;
        padding: 10px 16px;
        border-radius: 16px;
        max-width: 70%;
        text-align: left;
    }
    .assistant-message {
        display: flex;
        justify-content: flex-start;
        margin: 8px 0;
    }
    .assistant-bubble {
        background-color: #F0F0F0;
        color: #000000;
        padding: 10px 16px;
        border-radius: 16px;
        max-width: 70%;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Ahmet's CV Analyzer")
st.caption("Ask anything about Ahmet's CV")

implementation = st.sidebar.radio(
    "Implementation",
    ["Native Python", "LangChain"],
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f'<div class="user-message"><div class="user-bubble">{message["content"]}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="assistant-message"><div class="assistant-bubble">{message["content"]}</div></div>',
            unsafe_allow_html=True,
        )

prompt = st.chat_input("Ask something about Ahmet's CV")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages[:-1]
    ]

    with st.spinner("AI is thinking..."):
        if implementation.startswith("Native"):
            response = answer_native(prompt, history)
        else:
            response = answer_langchain(prompt, history)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()