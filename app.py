"""
ローカル環境での実行時はコメント化を解除する。
# .envに記述した環境変数を読み込むためのコード
from dotenv import load_dotenv
load_dotenv()
"""

import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

st.title("専門家がお答えします")

st.write("専門家を選んで入力フォームに質問を入力し「実行」ボタンを押すと、選んだ専門家が質問にお答えします。")
st.write("ABどちらの専門家がお答えしましょうか？")
selected_item = st.radio(
    "専門家の選択",
    ("A：健康の専門家", "B：お笑いの専門家")
)

st.divider()

input_text = st.text_input("質問を入力してください")

def get_expert_answer(input_text, selected_item):
    if not input_text:
        return "質問を入力してください。"
    if selected_item == "A：健康の専門家":
        messages = [
            SystemMessage(content="あなたは健康の知識が豊富な専門家です。その知識を活かして質問に具体的に答えてください。"),
            HumanMessage(content=input_text),
        ]
    else:
        messages = [
            SystemMessage(content="あなたは沢山の人を笑わせてきたお笑い芸人です。その経験を活かして質問に面白い答えを返してください。"),
            HumanMessage(content=input_text),
        ]
    result = llm.invoke(messages)
    return result.content

if st.button("実行"):
    answer = get_expert_answer(input_text, selected_item)
    if answer == "質問を入力してください。":
        st.warning(answer)
    else:
        st.write("専門家が回答を考えています...")
        st.write(answer)