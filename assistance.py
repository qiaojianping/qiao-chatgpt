from utils import get_chat_res
import streamlit as sl
from langchain.memory import ConversationBufferMemory

sl.title("小平智能聊天助手")

if "messages" not in sl.session_state:
    sl.session_state["messages"] = [{"role": "ai", "content": "你好，我是小平，是你的AI聊天助手，请问有什么可以帮你的吗？"}]
    sl.session_state["memory"] = ConversationBufferMemory(return_messages=True)

for message in sl.session_state["messages"]:
    sl.chat_message(message["role"]).write(message["content"])

prompt = sl.chat_input()
if prompt:
    sl.session_state["messages"].append({"role": "human", "content": prompt})
    sl.chat_message("human").write(prompt)
    with sl.spinner("小平正在思考中，请稍等..."):
        res = get_chat_res(prompt, sl.session_state["memory"])
        sl.session_state["messages"].append({"role": "ai", "content": res})
        sl.chat_message("ai").write(res)