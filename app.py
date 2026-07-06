import streamlit as st
from answer import answer

st.set_page_config(
    page_title="Ahmet's CV Analyzer",
    layout="wide"
)

st.markdown("""
<style>
.user-message{
    display:flex;
    justify-content:flex-end;
    margin:8px 0;
}
.user-bubble{
    background:#DCF2FF;
    color:black;
    padding:10px 16px;
    border-radius:16px;
    max-width:70%;
}
.assistant-message{
    display:flex;
    justify-content:flex-start;
    margin:8px 0;
}
.assistant-bubble{
    background:#F0F0F0;
    color:black;
    padding:10px 16px;
    border-radius:16px;
    max-width:70%;
}
</style>
""", unsafe_allow_html=True)

st.title("Ahmet's CV Analyzer")
st.caption("Ask anything about Ahmet's CV")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Conversation
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f"""
            <div class="user-message">
                <div class="user-bubble">{message["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="assistant-message">
                <div class="assistant-bubble">{message["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

prompt = st.chat_input("Ask something about Ahmet's CV")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    history = [
        {
            "role": m["role"],
            "content": m["content"]
        }
        for m in st.session_state.messages[:-1]
    ]

    with st.spinner("AI is thinking..."):
        response = answer(prompt, history)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()

if st.button("🗑 Clear conversation"):
    st.session_state.messages = []
    st.rerun()