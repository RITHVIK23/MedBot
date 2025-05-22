import streamlit as st
from app import MedicalQASystem

USER_ICON = "assets/user.png"
BOT_ICON = "assets/chatbot.png"

qa_system = MedicalQASystem(
    openai_key="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",
    vector_store_file="vector_store"
)

def main():
    # Set the title in the middle of the page
    st.set_page_config(page_title="MediBot", page_icon=":robot_face:", layout="centered")
    col1, col2, col3,col4,col5 = st.columns([1,1.4,1, 1, 1])
    with col3:
        st.image("assets/MedBot logo.png", width=60)
    st.markdown("<h1 style='text-align: center;'>MediBot - Your Medical Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Ask me any medical question!</p>", unsafe_allow_html=True)

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        if message['role'] == 'user':
            cols = st.columns([10, 1])
            with cols[0]:
               st.markdown(
            f"""
            <div style='width: 100%; text-align: right;'>
                <div style='border: 2px solid #800000; border-radius: 10px; padding: 10px; margin-bottom: 5px; display: inline-block;'>
                    {message['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
            with cols[1]:
                st.image(USER_ICON, width=40)

        else:
            cols = st.columns([1, 10])
            with cols[0]:
                st.image(BOT_ICON, width=40)
            with cols[1]:
                if isinstance(message['content'], dict):
                    sources_md = ""
                    # Only build sources_md if there are sources and the answer is not empty
                    if message['content']['answer'].strip() and message['content']['sources']:
                        for idx, src in enumerate(reversed(message['content']['sources']), 1):
                            if isinstance(src, dict) and 'source' in src and 'url' in src:
                                scr = src.get('score', 0) 
                                sources_md += (
                                    f'{idx}) <a href="{src["url"]}" target="_blank">{src["source"]}</a> '
                                    f'- DocID:{src.get("document_id", "")} ({scr:.2f})<br>'
                                )
                            elif isinstance(src, str):
                                sources_md += f"{idx}) {src}<br>"
                    st.markdown(
                        f"""
                        <div style='border: 2px solid #006666; border-radius: 10px; padding: 10px; margin-bottom: 5px; display: inline-block; text-align: left;'>
                            {message['content']['answer']}
                            {"<br><b>Sources:</b><br>" + sources_md if sources_md else ""}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div style='border: 2px solid #006666; border-radius: 10px; padding: 10px; margin-bottom: 5px; display: inline-block; text-align: left;'>
                            {message['content']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    prompt = st.chat_input("Enter your question:")
    if prompt:
        response = qa_system.get_answer(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

if __name__ == "__main__":
    main()