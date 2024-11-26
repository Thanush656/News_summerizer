import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.environ["google_api_key"])

# Create the model with desired generation settings
generation_config = {
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Function to generate a news summary
def generate_news_summary(news_article):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Summarize the following news article:",
                ],
            },
        ]
    )
    
    response = chat_session.send_message(news_article)
    return response.text

# Streamlit app
def main():
    st.title("News Summarizer")

    # Collect news article details
    st.subheader("Paste News Article")
    news_article = st.text_area("Enter the news article text")

    # Generate news summary
    if st.button("Summarize"):
        with st.spinner("Summarizing the news article..."):
            news_summary = generate_news_summary(news_article)
            st.subheader("News Summary")
            st.write(news_summary)

if __name__ == "__main__":
    main()
