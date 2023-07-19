import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# Replicate Credentials
with st.sidebar:
    st.title('🦙💬 Llama 2 Chatbot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not replicate_api.startswith('r8_'):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('📖 Learn how to build this app in this [blog](#link-to-blog)!')
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
# Pre-Prompt from https://github.com/a16z-infra/llama2-chatbot
def generate_response(prompt_input, api_token):
    llm='a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    pre_prompt="You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as Assistant."
    output=replicate.run(llm, 
                         input={"prompt": pre_prompt + 'User: ' + prompt_input + 'Assistant: '})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    #with st.chat_message("assistant"):
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            #string_dialogue = 
            #for dict_message in st.session_state.messages:
            #if dict_message["role"] == "user":
            #    string_dialogue = string_dialogue + "User: " + dict_message["content"] + "\n\n"
            #else:
            #    string_dialogue = string_dialogue + "Assistant: " + dict_message["content"] + "\n\n"
            
            response = generate_response(prompt, replicate_api)
            full_response = ''
            #placeholder = st.empty()
            for item in response:
                full_response += item
                #st.markdown(full_response + "|")
            st.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
