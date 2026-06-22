import streamlit as st
from openai import OpenAI

# Configure client
client = OpenAI(
    api_key=st.secrets["HF_API_KEY"],  # or use your key directly
    base_url="https://router.huggingface.co/v1"
)

st.title("🤖 GLM Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        response = client.chat.completions.create(
            model="zai-org/GLM-4.5",  # replace with GLM-5.2 if supported
            messages=st.session_state.messages,
            max_tokens=1024,
        )

        answer = response.choices[0].message.content
        response_placeholder.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
