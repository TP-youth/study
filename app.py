import streamlit as st
from openai import OpenAI

# Initialize your client
client = OpenAI(api_key="sk-c3da3134ec684372b9feb3be4052dea3", base_url="https://api.deepseek.com")

# Cache the API call to improve performance
@st.cache_data
def get_response(question):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    return response.choices[0].message.content

# Streamlit app interface
st.title("问答平台")
user_input = st.text_input("请输入您的问题")

if st.button("提问"):
    if user_input:
        with st.spinner("获取答案中..."):
            answer = get_response(user_input)
            st.success(answer)
    else:
        st.warning("请先输入一个问题。")
