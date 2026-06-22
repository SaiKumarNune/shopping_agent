import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except ImportError:
    st = None


def get_secret(key: str, default=None):
    if os.getenv(key):
        return os.getenv(key)

    if st is not None:
        try:
            return st.secrets.get(key, default)
        except Exception:
            return default

    return default


GROQ_API_KEY = get_secret("GROQ_API_KEY")
GROQ_MODEL = get_secret("GROQ_MODEL", "llama-3.1-8b-instant")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Add it to .env locally or Streamlit Secrets in cloud.")