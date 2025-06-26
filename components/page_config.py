import streamlit as st


def set_page_config():
    st.set_page_config(
        page_title="VaultRAG",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state=st.session_state["sidebar_state"],
        menu_items={
            "Get Help": "https://github.com/honey1205/VaultRAG/discussions",
            "Report a bug": "https://github.com/honey1205/VaultRAG/issues",
        },
    )

    # Remove the Streamlit `Deploy` button from the Header
    st.markdown(
        r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
