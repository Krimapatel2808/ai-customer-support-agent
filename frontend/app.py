import streamlit as st
import requests
from datetime import datetime


API_URL = "http://127.0.0.1:8000/chat"


# --------------------------------------------------
# API
# --------------------------------------------------

def get_ai_response(message: str) -> str:
    try:
        response = requests.post(
            API_URL,
            json={"message": message},
            timeout=60,
        )

        if response.status_code == 200:
            return response.json()["answer"]

        return "Sorry, the support service returned an error."

    except requests.RequestException:
        return "Sorry, I couldn't connect to the support service."


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="SupportAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background: #0f1117;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background: #151821;
        border-right: 1px solid #262a35;
    }

    .sidebar-logo {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .sidebar-subtitle {
        color: #8b93a7;
        font-size: 13px;
        margin-bottom: 28px;
    }

    .status-card {
        background: #1c202b;
        border: 1px solid #292e3b;
        border-radius: 12px;
        padding: 14px;
        margin-top: 20px;
    }

    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #35d07f;
        border-radius: 50%;
        margin-right: 7px;
    }

    .status-text {
        color: #c9cfdb;
        font-size: 13px;
    }

    .header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 8px;
    }

    .header-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: #242938;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 25px;
    }

    .header-title {
        font-size: 30px;
        font-weight: 700;
        line-height: 1.1;
    }

    .header-subtitle {
        color: #8b93a7;
        margin-top: 5px;
        font-size: 14px;
    }

    .welcome {
        margin-top: 70px;
        margin-bottom: 30px;
        text-align: center;
    }

    .welcome-icon {
        font-size: 44px;
        margin-bottom: 10px;
    }

    .welcome-title {
        font-size: 28px;
        font-weight: 650;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #8b93a7;
        font-size: 15px;
    }

    .info-card {
        background: #171a22;
        border: 1px solid #292e3b;
        border-radius: 12px;
        padding: 17px;
        height: 100%;
    }

    .info-card-title {
        font-weight: 600;
        margin-bottom: 7px;
    }

    .info-card-text {
        color: #8b93a7;
        font-size: 13px;
        line-height: 1.5;
    }

    [data-testid="stChatMessage"] {
        background: transparent;
        border: none;
        padding-top: 8px;
        padding-bottom: 8px;
    }

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #2b3040;
        background: #181b24;
        color: #d8dce6;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #596176;
        color: white;
    }

    [data-testid="stChatInput"] {
        border-color: #2b3040;
    }

    .footer {
        text-align: center;
        color: #656d80;
        font-size: 12px;
        margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">🤖 SupportAI</div>
        <div class="sidebar-subtitle">
            AI-powered customer support
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### What can I help with?")

    st.markdown(
        """
        - 📦 Order cancellation
        - 🔄 Product returns
        - 💳 Refunds
        - 🚚 Shipping
        - 🕐 Support hours
        """
    )

    st.markdown(
        """
        <div class="status-card">
            <div>
                <span class="status-dot"></span>
                <span class="status-text">AI system online</span>
            </div>
            <div style="color:#656d80; font-size:11px; margin-top:7px;">
                Semantic retrieval + LLM
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="header">
        <div class="header-icon">🤖</div>
        <div>
            <div class="header-title">Customer Support</div>
            <div class="header-subtitle">
                Get fast answers about your orders and products
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# WELCOME SCREEN
# --------------------------------------------------

if not st.session_state.messages:

    st.markdown(
        """
        <div class="welcome">
            <div class="welcome-icon">👋</div>
            <div class="welcome-title">How can I help you today?</div>
            <div class="welcome-text">
                Ask me anything about returns, refunds, shipping,
                cancellations, or support.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-title">📦 Orders & Shipping</div>
                <div class="info-card-text">
                    Ask about delivery times, tracking, or cancelling
                    an order before it ships.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-title">💳 Returns & Refunds</div>
                <div class="info-card-text">
                    Get information about return eligibility and
                    when refunds are processed.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    st.markdown("**Try asking:**")

    suggestions = [
        "Can I cancel my order?",
        "How long does a refund take?",
        "How long does shipping take?",
        "What are your support hours?",
    ]

    cols = st.columns(2)

    for index, suggestion in enumerate(suggestions):

        with cols[index % 2]:

            if st.button(
                suggestion,
                key=f"suggestion_{index}",
                use_container_width=True,
            ):

                timestamp = datetime.now().strftime("%H:%M")

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": suggestion,
                        "timestamp": timestamp,
                    }
                )

                with st.spinner("Thinking..."):
                    answer = get_ai_response(suggestion)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "timestamp": datetime.now().strftime("%H:%M"),
                    }
                )

                st.rerun()


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if "timestamp" in message:
            st.caption(message["timestamp"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

if prompt := st.chat_input("Ask your question..."):

    timestamp = datetime.now().strftime("%H:%M")

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
            "timestamp": timestamp,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)
        st.caption(timestamp)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            answer = get_ai_response(prompt)

        st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "timestamp": datetime.now().strftime("%H:%M"),
            }
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        SupportAI · Powered by semantic retrieval and large language models
    </div>
    """,
    unsafe_allow_html=True,
)

