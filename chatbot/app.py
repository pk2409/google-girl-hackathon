import streamlit as st
import gemini
from PIL import Image

# Page configuration with a medical theme
st.set_page_config(
    page_title="💬 MediChat AI Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS styling
st.markdown(
    """
    <style>
        /* Global styles */
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f9ff;
            color: #1e3a8a;
        }
        
        /* Header styling */
        .main-header {
            background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .main-header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        /* Chat container */
        .chat-container {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            max-height: 500px;
            overflow-y: auto;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
            margin-bottom: 1.5rem;
            border: 1px solid #e5e7eb;
        }
        
        /* Message bubbles */
        .user-msg {
            background-color: #dbeafe;
            color: #1e40af;
            padding: 12px 16px;
            border-radius: 18px 18px 0 18px;
            margin-bottom: 15px;
            max-width: 75%;
            float: right;
            clear: both;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            font-weight: 500;
        }
        
        .assistant-msg {
            background-color: #eff6ff;
            color: #1e3a8a;
            padding: 12px 16px;
            border-radius: 18px 18px 18px 0;
            margin-bottom: 15px;
            max-width: 75%;
            float: left;
            clear: both;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            border-left: 4px solid #3b82f6;
        }
        
        /* Input field styling */
        .stTextInput>div>div>input {
            border: 2px solid #3b82f6 !important;
            border-radius: 25px !important;
            padding: 15px 20px !important;
            font-size: 16px !important;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #1d4ed8 !important;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3) !important;
        }
        
        /* Button styling */
        .stButton button {
            background-color: #3b82f6 !important;
            color: white !important;
            border-radius: 25px !important;
            padding: 10px 25px !important;
            font-weight: 500 !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            background-color: #2563eb !important;
            transform: translateY(-2px);
        }
        
        /* File uploader styling */
        .uploadedFile {
            border: 2px dashed #3b82f6 !important;
            border-radius: 10px !important;
            padding: 20px !important;
        }
        
        /* Card styling for sections */
        .card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #e5e7eb;
        }
        
        .card-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #1e3a8a;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #dbeafe;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f1f5f9;
        }
        
        /* Status indicator */
        .status-online {
            display: inline-block;
            width: 10px;
            height: 10px;
            background-color: #10b981;
            border-radius: 50%;
            margin-right: 6px;
        }
        
        /* Footer styling */
        footer {
            text-align: center;
            padding: 15px;
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Custom header
st.markdown(
    """
    <div class="main-header">
        <h1>🩺 MediChat AI Assistant</h1>
        <p>Your intelligent medical companion for health insights and diagnosis assistance</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Create two columns for chat and image analysis
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card-header">Chat Consultation</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-online"></div> AI Assistant Online', unsafe_allow_html=True)
    
    # Chat container
    chat_container = st.container()
    if "history" in st.session_state and st.session_state.history:
        with chat_container:
            chat_html = '<div class="chat-container">'
            for msg in st.session_state.history:
                if msg["role"] == "user":
                    chat_html += f'<div class="user-msg">{msg["content"]}</div>'
                else:
                    chat_html += f'<div class="assistant-msg">{msg["content"]}</div>'
            chat_html += '<div style="clear: both;"></div></div>'
            st.markdown(chat_html, unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div class="chat-container">
                <div class="assistant-msg">Hello! I'm your medical AI assistant. How can I help you today? You can ask me about symptoms, conditions, or upload an image for analysis.</div>
                <div style="clear: both;"></div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Message input and send button
    def submit_message():
        if st.session_state.user_input:
            user_message = st.session_state.user_input
            
            # In a real app, you would get a response from your model
            try:
                assistant_reply = gemini.get_response(user_message)
            except:
                # Fallback response if gemini module fails
                assistant_reply = "I understand your concern. Based on the information you've provided, I recommend discussing these symptoms with a healthcare professional. Would you like me to provide some general information on this topic?"
            
            st.session_state.history.append({"role": "user", "content": user_message})
            st.session_state.history.append({"role": "assistant", "content": assistant_reply})
            st.session_state.user_input = ""

    # Input area with columns for better layout
    input_col1, input_col2 = st.columns([5, 1])
    with input_col1:
        st.text_input(
            "Type your message here...",
            key="user_input",
            on_change=submit_message,
            placeholder="Describe your symptoms or ask a medical question..."
        )
    with input_col2:
        if st.button("Send 📤"):
            submit_message()

with col2:
    st.markdown('<div class="card-header">Visual Diagnosis</div>', unsafe_allow_html=True)
    
    # Image upload section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload a medical image",
        type=["png", "jpg", "jpeg"],
        help="Upload X-rays, MRIs, CT scans, skin photos, etc."
    )
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        with st.spinner("Analyzing image..."):
            # Placeholder for model selection and prediction
            # In a real implementation, you would connect this to your models
            st.markdown("#### Analysis Results")
            
            # Simulated results - in real app these would come from your ML model
            st.markdown("""
            <div style="background-color: #f0f9ff; padding: 15px; border-radius: 10px; border-left: 4px solid #3b82f6;">
                <h4 style="margin-top: 0; color: #1e40af;">Preliminary Assessment</h4>
                <p>The image analysis suggests further evaluation may be needed. Please consult with a healthcare professional for an accurate diagnosis.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div style="text-align: center; padding: 30px; color: #64748b;">
                <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <circle cx="8.5" cy="8.5" r="1.5"></circle>
                    <polyline points="21 15 16 10 5 21"></polyline>
                </svg>
                <p>Upload a medical image for AI-assisted analysis</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <footer>
        <p>MediChat AI Assistant | For informational purposes only | Not a substitute for professional medical advice</p>
    </footer>
    """, 
    unsafe_allow_html=True
)