import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Sample dataset
data = {
    "greetings": ["Hello! 👋", "Hi there! 😊", "Greetings! 🎉", "Hey! How can I help? 💡"],
    "questions": {
        "weather": ["The weather is sunny today! ☀️", "It looks like rain tomorrow ☔", "Perfect beach weather! �"],
        "time": [f"The current time is {datetime.now().strftime('%H:%M')} ⏰"],
        "date": [f"Today is {datetime.now().strftime('%B %d, %Y')} 📅"],
        "help": ["I can tell you about weather, time, or date! 🌈", "Ask me anything! Well, almost anything... 😅"]
    },
    "goodbyes": ["Goodbye! 👋", "See you later! 😊", "Bye! Come back soon! 🌟"],
    "jokes": [
        "Why don't scientists trust atoms? Because they make up everything! 🤣",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them! 😆",
        "Why don't skeletons fight each other? They don't have the guts! 💀"
    ]
}

# CSS for colorful background and black chat
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .chat-message {
            color: black !important;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            font-size: 16px;
        }
        .user-message {
            background-color: rgba(255, 255, 255, 0.8);
            text-align: right;
        }
        .bot-message {
            background-color: rgba(255, 255, 255, 0.6);
            text-align: left;
        }
        .stTextInput > div > div > input {
            color: black !important;
            background-color: rgba(255, 255, 255, 0.8) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome_msg = random.choice(data["greetings"])
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

# Display chat messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    css_class = "bot-message" if role == "assistant" else "user-message"
    st.markdown(f'<div class="chat-message {css_class}">{content}</div>', unsafe_allow_html=True)

# User input
prompt = st.chat_input("Say something")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="chat-message user-message">{prompt}</div>', unsafe_allow_html=True)
    
    # Bot response logic
    response = ""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ["hi", "hello", "hey"]):
        response = random.choice(data["greetings"])
    elif "weather" in prompt_lower:
        response = random.choice(data["questions"]["weather"])
    elif "time" in prompt_lower:
        response = random.choice(data["questions"]["time"])
    elif "date" in prompt_lower:
        response = random.choice(data["questions"]["date"])
    elif "joke" in prompt_lower:
        response = random.choice(data["jokes"])
    elif "bye" in prompt_lower or "goodbye" in prompt_lower:
        response = random.choice(data["goodbyes"])
    elif "help" in prompt_lower:
        response = random.choice(data["questions"]["help"])
    else:
        responses = [
            "I'm not sure I understand. Can you rephrase that? 🤔",
            "Interesting question! Let me think about that... 🧠",
            "I'm still learning! Ask me something else. 📚",
            "Hmm, I don't have an answer for that right now. 😅"
        ]
        response = random.choice(responses)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'<div class="chat-message bot-message">{response}</div>', unsafe_allow_html=True)