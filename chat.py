import streamlit as st
import time
import pandas as pd
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM 
from PIL import Image
from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)

try:
    from transformers import AutoModelWithLMHead
except ImportError:
    print("cannot import name 'AutoModelWithLMHead' from 'transformers'")

  
if "loading" not in st.session_state:
    st.session_state.loading = False

if "tq_avatar" not in st.session_state:
    st.session_state["tq_avatar"] = Image.open("images/minthara.png")
    
if "user_avatar" not in st.session_state:
    st.session_state["user_avatar"] = Image.open("images/user_logo.jpg")
    
    
st.set_page_config(
    page_title="Baldur's Gate Chatbot",
    page_icon= st.session_state["tq_avatar"],
    layout="centered",
    initial_sidebar_state="expanded",
)

# INSERTE MODELO ENTRENADO DEL DIALOGPT
if "llm_model" not in st.session_state:
    st.session_state["llm_model"] = AutoModelForCausalLM.from_pretrained('output-medium')

#if "vs_client" not in st.session_state:
#    st.session_state["vs_client"] = VSClient(st.session_state["llm_model"].get_openai_embeddings())
st.title("Baldur's Gate Chatbot")

if "messages" not in st.session_state:
    TQ_AVATAR = st.session_state["tq_avatar"]
    st.session_state.messages = [{"role": "assistant", "content": "Welcome","avatar":TQ_AVATAR}]

# Display chat messages from history on app rerun
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"],avatar=message["avatar"]):
        st.write(message["content"])
    
    
tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')

if not st.session_state.loading:
    # React to user input
    if prompt := st.chat_input("Enter a question", disabled=st.session_state.loading):
        USER_AVATAR = st.session_state["user_avatar"]
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt,"avatar":USER_AVATAR})
        st.session_state.loading = True
        st.rerun()
else:
    st.chat_input("Enter a question", disabled=st.session_state.loading)
    TQ_AVATAR = st.session_state["tq_avatar"]

    with st.spinner(text="Generating answer..."):
        full_response = ""
        llm_model = st.session_state["llm_model"]
        #vs_client = st.session_state["vs_client"]
        prompt = st.session_state.messages[-1]["content"]
        
        new_user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
        #bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) 
        chat_history_ids = llm_model.generate(
                #bot_input_ids, max_length=200,
                new_user_input_ids, max_length=200,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                do_sample=True,
                top_k=100,
                top_p=0.7,
                temperature=0.8
            )
        
        # pretty print last ouput tokens from bot
        #print("Minthara: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
        
        data = tokenizer.decode(chat_history_ids, skip_special_tokens=True)

        full_response = data
    # Add assistant response to chat history
    if not data:
        st.session_state.messages.append({"role": "assistant", "content": data, "prompt":prompt, "response":data, "avatar":TQ_AVATAR})
    else:
        # Simulate stream of response with milliseconds delay
        with st.chat_message("assistant", avatar=TQ_AVATAR):
            message_placeholder = st.empty()
        
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": data, "prompt":prompt, "response":data, "avatar":TQ_AVATAR})

    st.session_state.loading = False

    st.rerun()
