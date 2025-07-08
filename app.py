import streamlit as st
from chatbot import get_chatty_response

# Page config with wider layout
st.set_page_config(
    page_title="Chatty AI Assistant", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple CSS styling
st.markdown("""
<style>
    /* Hide defaults and setup */
    #MainMenu, footer, header, .stDeployButton {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main .block-container {
        padding-top: 2rem;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* Header */
    .header-container {
        text-align: center;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Chat messages */
    .stChatMessage {
        margin: 1rem 0;
    }
    
    /* User messages */
    .stChatMessage[data-testid="user-message"] {
        flex-direction: row-reverse;
    }
    
    .stChatMessage[data-testid="user-message"] > div {
        background: #007bff !important;
        border-radius: 18px 18px 5px 18px !important;
        margin-left: 10% !important;
        max-width: 85% !important;
        padding: 1.5rem 2rem !important;
    }
    
    /* Assistant messages */
    .stChatMessage[data-testid="assistant-message"] > div {
        background: #f8f9fa !important;
        border-radius: 18px 18px 18px 5px !important;
        margin-right: 10% !important;
        max-width: 85% !important;
        padding: 1.5rem 2rem !important;
        border-left: 4px solid #667eea !important;
    }
    
    /* White text for all chat messages */
    .stChatMessage * {
        color: white !important;
    }
    
    /* Input styling */
    .stChatInput input {
        border-radius: 25px !important;
        background: rgba(255,255,255,0.9) !important;
        padding: 12px 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# Beautiful header with animation
st.markdown("""
<div class="header-container">
    <div class="header-title">🤖 Chatty</div>
    <div class="header-subtitle">Your Intelligent AI Assistant • Created by Himanshu Singh</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for i in range(0, len(st.session_state.chat_history), 2):
    # User message
    with st.chat_message("user", avatar="👤"):
        st.write(st.session_state.chat_history[i])
    
    # Assistant message
    if i + 1 < len(st.session_state.chat_history):
        with st.chat_message("assistant", avatar="🤖"):
            st.write(st.session_state.chat_history[i + 1])

# Chat input
prompt = st.chat_input("Type your message here...", key="chat_input")

if prompt:
    st.session_state.chat_history.append(prompt)
    
    # Show user message immediately
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    
    # Get and show assistant response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = get_chatty_response(prompt, st.session_state.chat_history)
            st.write(response)
            st.session_state.chat_history.append(response)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)