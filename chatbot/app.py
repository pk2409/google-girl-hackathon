import streamlit as st
import gemini_ai
from PIL import Image
import base64
import io

from flask import Flask, request, jsonify
from flask_cors import CORS
# import gemini
from gemini_ai import get_response  # Adjust based on your chatbot logic

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    message = data.get("message", "")
    # reply = get_response(message)  # Modify as per your chatbot logic
    # bot_response={
    #     "response":reply.text
    # }
    try:
        
        response = get_response(message)

        # Extracting the response text
        bot_response = response
    except Exception as e:
        bot_response = f"Error: {str(e)}"
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)


# # Page configuration with a medical theme
# st.set_page_config(
#     page_title="💬 MediChat AI Assistant",
#     page_icon="🩺",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Enhanced CSS styling
# st.markdown(
#     """
#     <style>
#         /* Global styles */
#         body {
#             font-family: 'Roboto', sans-serif;
#             background-color: #f0f9ff;
#             color: #1e3a8a;
#         }
        
#         /* Header styling */
#         .main-header {
#             background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
#             color: white;
#             padding: 1.5rem;
#             border-radius: 10px;
#             margin-bottom: 1.5rem;
#             text-align: center;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
        
#         .main-header h1 {
#             font-size: 2.5rem;
#             margin-bottom: 0.5rem;
#         }
        
#         .main-header p {
#             font-size: 1.1rem;
#             opacity: 0.9;
#         }
        
#         /* Chat container */
#         .chat-container {
#             background: white;
#             padding: 1.5rem;
#             border-radius: 12px;
#             max-height: 500px;
#             overflow-y: auto;
#             box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
#             margin-bottom: 1.5rem;
#             border: 1px solid #e5e7eb;
#         }
        
#         /* Message bubbles */
#         .user-msg {
#             background-color: #dbeafe;
#             color: #1e40af;
#             padding: 12px 16px;
#             border-radius: 18px 18px 0 18px;
#             margin-bottom: 15px;
#             max-width: 75%;
#             float: right;
#             clear: both;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#             font-weight: 500;
#         }
        
#         .assistant-msg {
#             background-color: #eff6ff;
#             color: #1e3a8a;
#             padding: 12px 16px;
#             border-radius: 18px 18px 18px 0;
#             margin-bottom: 15px;
#             max-width: 75%;
#             float: left;
#             clear: both;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#             border-left: 4px solid #3b82f6;
#         }
        
#         /* Input field styling */
#         .stTextInput>div>div>input {
#             border: 2px solid #3b82f6 !important;
#             border-radius: 25px !important;
#             padding: 15px 20px !important;
#             font-size: 16px !important;
#             transition: all 0.3s ease;
#             box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
#         }
        
#         .stTextInput>div>div>input:focus {
#             border-color: #1d4ed8 !important;
#             box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3) !important;
#         }
        
#         /* Button styling */
#         .stButton button {
#             background-color: #3b82f6 !important;
#             color: white !important;
#             border-radius: 25px !important;
#             padding: 10px 25px !important;
#             font-weight: 500 !important;
#             border: none !important;
#             box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3) !important;
#             transition: all 0.3s ease !important;
#         }
        
#         .stButton button:hover {
#             background-color: #2563eb !important;
#             transform: translateY(-2px);
#         }
        
#         /* File uploader styling - smaller and compact */
#         .stFileUploader>div>div {
#             padding: 5px !important;
#             display: flex !important;
#             align-items: center !important;
#         }
        
#         .stFileUploader>div>div>button {
#             padding: 0px 10px !important;
#             font-size: 0.8rem !important;
#             height: 35px !important;
#             margin-left: 5px !important;
#         }
        
#         .uploadedFile {
#             display: none !important;
#         }
        
#         /* Card styling for sections */
#         .card {
#             background: white;
#             border-radius: 12px;
#             padding: 20px;
#             margin-bottom: 20px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#             border: 1px solid #e5e7eb;
#         }
        
#         .card-header {
#             font-size: 1.2rem;
#             font-weight: 600;
#             color: #1e3a8a;
#             margin-bottom: 15px;
#             padding-bottom: 10px;
#             border-bottom: 2px solid #dbeafe;
#         }
        
#         /* Sidebar styling */
#         .css-1d391kg {
#             background-color: #f1f5f9;
#         }
        
#         /* Status indicator */
#         .status-online {
#             display: inline-block;
#             width: 10px;
#             height: 10px;
#             background-color: #10b981;
#             border-radius: 50%;
#             margin-right: 6px;
#         }
        
#         /* Footer styling */
#         footer {
#             text-align: center;
#             padding: 15px;
#             font-size: 0.8rem;
#             color: #64748b;
#             margin-top: 30px;
#         }
        
#         /* Health tips cards */
#         .health-tip-card {
#             background: linear-gradient(45deg, #EFF6FF 0%, #DBEAFE 100%);
#             border-radius: 10px;
#             padding: 15px;
#             margin-bottom: 15px;
#             border-left: 4px solid #3b82f6;
#         }
        
#         .tip-title {
#             color: #1e40af;
#             font-weight: 600;
#             margin-bottom: 8px;
#             font-size: 1rem;
#         }
        
#         /* Hide upload message */
#         .upload-message {
#             display: none !important;
#         }
        
#         /* Custom file upload button */
#         .custom-file-button {
#             background-color: #3b82f6;
#             color: white;
#             border-radius: 50%;
#             width: 40px;
#             height: 40px;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             cursor: pointer;
#             box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
#             transition: all 0.2s ease;
#         }
        
#         .custom-file-button:hover {
#             background-color: #2563eb;
#             transform: translateY(-2px);
#         }
        
#         /* Input row */
#         .input-row {
#             display: flex;
#             align-items: center;
#             gap: 10px;
#         }
        
#         /* Image display in chat */
#         .chat-image {
#             margin: 10px 0;
#             border-radius: 10px;
#             max-width: 250px;
#             box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Custom header
# st.markdown(
#     """
#     <div class="main-header">
#         <h1>🩺 MediChat AI Assistant</h1>
#         <p>Your intelligent medical companion for health insights and diagnosis assistance</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "image_data" not in st.session_state:
    st.session_state.image_data = {}

# Function to convert image to base64 for displaying in HTML
def get_image_base64(image):
    # Create a copy of the image
    img_copy = image.copy()
    
    # Convert RGBA to RGB if needed
    if img_copy.mode == 'RGBA':
        # Create a white background
        background = Image.new('RGB', img_copy.size, (255, 255, 255))
        # Paste the image on the background using alpha as mask
        background.paste(img_copy, mask=img_copy.split()[3])
        img_copy = background
    
    # Save as JPEG
    buffered = io.BytesIO()
    img_copy.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Function to handle image uploads - will add to chat
def process_uploaded_image():
    if st.session_state.uploaded_file is not None:
        # Process the image
        image = Image.open(st.session_state.uploaded_file)
        
        # Convert image to base64 for display in HTML
        img_base64 = get_image_base64(image)
        
        # Generate a unique image ID
        image_id = f"img_{len(st.session_state.image_data) + 1}"
        
        # Store the image data
        st.session_state.image_data[image_id] = img_base64
        
        # Add a user message showing the image was uploaded
        user_message = f"I've uploaded an image for analysis."
        
        # In a real app, you would get a response from your model
        try:
            # Here you would analyze the image using your model
            assistant_reply = "I've analyzed your uploaded image. Based on what I can see, this appears to be a medical scan. For a proper diagnosis, I recommend consulting with a healthcare professional. Would you like me to provide some general information about what this type of image typically shows?"
        except:
            assistant_reply = "I've received your image. For accurate analysis of medical images, please consult with a healthcare professional. Would you like some general information about interpreting these types of images?"
        
        # Add to chat history with image reference
        st.session_state.history.append({"role": "user", "content": user_message, "image": True, "image_id": image_id})
        st.session_state.history.append({"role": "assistant", "content": assistant_reply})
        
        # Clear the file uploader
        # st.session_state.uploaded_file = None

# Main column layout - now simpler
col1, col2 = st.columns([3, 1])

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
                    if "image" in msg and msg["image"] and "image_id" in msg:
                        # For messages with an image uploaded
                        chat_html += f'<div class="user-msg">{msg["content"]}'
                        image_id = msg["image_id"]
                        if image_id in st.session_state.image_data:
                            img_base64 = st.session_state.image_data[image_id]
                            chat_html += f'<br><img src="data:image/jpeg;base64,{img_base64}" class="chat-image" alt="Uploaded medical image">'
                        chat_html += '</div>'
                    else:
                        # Regular text messages
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

    # Message input and buttons in a row
    def submit_message():
        if st.session_state.user_input:
            user_message = st.session_state.user_input
            
            # In a real app, you would get a response from your model
            try:
                assistant_reply = gemini.get_response(user_message)
            except:
                # Fallback response if gemini module fails
                assistant_reply = "error"
            
            st.session_state.history.append({"role": "user", "content": user_message})
            st.session_state.history.append({"role": "assistant", "content": assistant_reply})
            st.session_state.user_input = ""

    # Input area with columns for better layout
    input_col1, input_col2, input_col3 = st.columns([10, 1, 1])
    
    with input_col1:
        st.text_input(
            "Type your message here...",
            key="user_input",
            on_change=submit_message,
            placeholder="Describe your symptoms or ask a medical question..."
        )
    
    with input_col2:
        if st.button("Send"):
            submit_message()
            
    # with input_col3:
        # File uploader (styled to be small)
    uploaded_file = st.file_uploader(
        "",
        type=["png", "jpg", "jpeg"],
        key="uploaded_file",
        on_change=process_uploaded_image,
        label_visibility="collapsed"
    )
        
with col2:
    st.markdown('<div class="card-header">Health Tips</div>', unsafe_allow_html=True)
    
    # Health tips cards instead of visual diagnosis
    st.markdown(
        """
        <div class="health-tip-card">
            <div class="tip-title">🔍 When to Seek Help</div>
            <p>Persistent symptoms, severe pain, difficulty breathing, or sudden changes require immediate medical attention.</p>
        </div>
        
        <div class="health-tip-card">
            <div class="tip-title">🧠 Mental Health Matters</div>
            <p>Your mental wellbeing is as important as physical health. Speak to a professional if you're struggling.</p>
        </div>
        
        <div class="health-tip-card">
            <div class="tip-title">💊 Medication Safety</div>
            <p>Always take medications as prescribed. Don't stop without consulting your doctor.</p>
        </div>
        
        <div class="health-tip-card">
            <div class="tip-title">⚠️ AI Limitations</div>
            <p>This assistant provides information only. Always consult healthcare professionals for diagnosis and treatment.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <footer>
        <p>MediChat AI Assistant | For informational purposes only | Not a substitute for professional medical advice</p>
    </footer>
    """, 
    unsafe_allow_html=True
)

