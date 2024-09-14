# YouTube Transcript Summarizer and Q&A

This Streamlit app allows users to input a YouTube video URL, fetch the transcript, summarize it, and ask specific questions based on the transcript.

## Features
- Fetches the transcript of a YouTube video.
- Summarizes the transcript using OpenAI's GPT-4 model.
- Allows users to ask specific questions about the transcript and get answers.

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up the environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

2. **Enter the YouTube URL:**
   - Input the URL of the YouTube video you want to summarize.

3. **Get the Transcript and Summary:**
   - Click the "Get Transcript and Summarize" button to fetch and summarize the transcript.

4. **Ask Questions:**
   - Enter your question about the transcript and click the "Get Answer" button to receive an answer.

## Note

This app was created using aider commands to facilitate the development process. Aider is a tool that helps in automating code changes and managing tasks efficiently.
