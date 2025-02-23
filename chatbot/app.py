import streamlit as st
import gemini 

st.set_page_config(page_title="💬 Medical AI Chatbot", page_icon="🩺", layout="wide")

st.markdown(
    """
    <style>
        /* Set background color */
        body {
            background-color: #dbeafe; /* Light Blue */
        }

        /* Chat history box */
        .chat-container {
            background: #f8fafc; /* Light Gray */
            padding: 15px;
            border-radius: 10px;
            max-height: 400px;
            overflow-y: auto;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* User message (align right) */
        .user-msg {
            background-color: #dcf8c6;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            max-width: 70%;
            text-align: right;
            float: right;
            clear: both;
            display: inline-block;
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
        }

        /* Assistant message (align left) */
        .assistant-msg {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            max-width: 70%;
            text-align: left;
            float: left;
            clear: both;
            display: inline-block;
            border: 1px solid #ccc;
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
        }

        /* Styled input box */
        .stTextInput>div>div>input {
            border: 2px solid #3b82f6 !important; /* Blue border */
            border-radius: 8px !important;
            padding: 10px !important;
            font-size: 16px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🩺 Medical AI Chatbot")
st.subheader("Your AI-powered assistant for medical diagnosis")

if "history" not in st.session_state:
    st.session_state.history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

chat_container = st.container()
if "history" in st.session_state and st.session_state.history:  # Check if history exists and is not empty
    with chat_container:
        chat_html = '<div class="chat-container">'
        for msg in st.session_state.history:
            if msg["role"] == "user":
                chat_html += f'<div class="user-msg">{msg["content"]}</div>'
            else:
                chat_html += f'<div class="assistant-msg">{msg["content"]}</div>'
        chat_html += '</div>'
        st.markdown(chat_html, unsafe_allow_html=True)  # Render only if messages exist


def submit_message():
    if st.session_state.user_input:
        assistant_reply = gemini.get_response(st.session_state.user_input)

        st.session_state.history.append({"role": "user", "content": st.session_state.user_input})
        st.session_state.history.append({"role": "assistant", "content": assistant_reply})

        st.session_state.user_input = ""


st.text_input("Type your message here...", key="user_input", on_change=submit_message, help="Press Enter to send.")
