import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables from .env file
load_dotenv()
from openai import OpenAI
openai_api_key = os.getenv('OPENAI_API_KEY')

def get_youtube_transcript(video_url):
    video_id = video_url.split('v=')[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([entry['text'] for entry in transcript])
    return transcript_text

@st.cache_data
def summarize_text(text):
    client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide a detailed summary of the following transcript:\n\n{text}"}
        ],
        max_tokens=2000,
        temperature=0.3,
    )
    summary = response.choices[0].message.content
    return summary

def answer_question(transcript, question):
    client = OpenAI(
        api_key=openai_api_key
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following transcript, answer the question:\n\nTranscript: {transcript}\n\nQuestion: {question}"}
        ],
        max_tokens=2000,
        temperature=0.3,
    )
    answer = response.choices[0].message.content
    return answer

# Streamlit app logic
st.title("YouTube Transcript Summarizer and Q&A")

video_url = st.text_input("Enter YouTube URL:")

if 'transcript' not in st.session_state:
    st.session_state.transcript = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""

if st.button("Get Transcript and Summarize"):
    if video_url:
        with st.spinner("Fetching transcript..."):
            st.session_state.transcript = get_youtube_transcript(video_url)
        with st.spinner("Summarizing transcript..."):
            st.session_state.summary = summarize_text(st.session_state.transcript)
        st.subheader("Transcript Summary:")
        st.write(st.session_state.summary)
    else:
        st.error("Please enter a valid YouTube URL.")

if st.session_state.transcript:
    question = st.text_input("Enter your question about the transcript:")
    if st.button("Get Answer"):
        if question:
            with st.spinner("Getting answer..."):
                answer = answer_question(st.session_state.transcript, question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.error("Please enter a question.")

# Set your OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

def get_youtube_transcript(video_url):
    video_id = video_url.split('v=')[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([entry['text'] for entry in transcript])
    return transcript_text

def summarize_text(text):
    client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide a detailed summary of the following transcript:\n\n{text}"}
        ],
        max_tokens=2000,
        temperature=0.3,
    )
    summary = response.choices[0].message.content
    return summary

def answer_question(transcript, question):
    client = OpenAI(
        api_key=openai_api_key
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following transcript, answer the question:\n\nTranscript: {transcript}\n\nQuestion: {question}"}
        ],
        max_tokens=2000,
        temperature=0.3,
    )
    answer = response.choices[0].message.content
    return answer
