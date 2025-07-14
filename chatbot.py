import streamlit as st
from datetime import datetime

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate bot response based on rules
def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"
    
    # Time questions
    elif "time" in user_input:
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M')}"
    
    # Date questions
    elif "date" in user_input or "day" in user_input:
        now = datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}"
    
    # Help
    elif "help" in user_input:
        return "I can answer questions about time, date, weather (just basic info), and general greetings. Try asking me things like 'What time is it?' or 'Hello!'"
    
    # Weather
    elif "weather" in user_input:
        return "I'm a simple bot and don't have real-time weather data. But I can tell you that weather is usually nice somewhere!"
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"
    
    # Default response
    else:
        return "I'm not sure I understand. Could you rephrase that or ask something else?"

# Streamlit app layout
st.title("🤖 Rule-Based Chatbot")
st.write("This is a simple chatbot that responds based on predefined rules. Try saying hello!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    response = get_bot_response(prompt)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)