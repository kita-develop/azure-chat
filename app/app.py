import streamlit as st

USER_NAME = "user"
ASSISTANT_NAME = "assistant"

def main():
    st.title('Azure Chat Stocks')

    # チャットログを保存したセッション情報を初期化
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []
            
    # ユーザのメッセージ入力
    user_msg = st.chat_input('メッセージを入力してください')
    
    if user_msg:
        
        # 以前のチャットログを表示
        for chat in st.session_state.chat_log:
            if chat["name"] == ASSISTANT_NAME:
                with st.chat_message(ASSISTANT_NAME):
                    st.write(chat["msg"])
            else:
                with st.chat_message(USER_NAME):
                    st.write(chat["msg"])
                    
        with st.chat_message(USER_NAME):
            st.write(user_msg)

        # 質問の回答を表示
        with st.chat_message(ASSISTANT_NAME):
            st.write('回答')
        
        # セッションにチャットログを追加
        st.session_state.chat_log.extend([
            {"name": USER_NAME, "msg": user_msg},
            {"name": ASSISTANT_NAME, "msg": "回答"}
        ])
    
if __name__ == '__main__':
    main()
