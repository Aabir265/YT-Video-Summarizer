from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent / ".env"
env_path = Path(__file__)
load_dotenv(env_path)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def get_video_summary(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=["en", "hi", "pa", "en-IN"])

        transcript_text = " ".join(
            snippet.text for snippet in transcript
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are an expert multilingual video summarizer.
Kindly keep in mind these things while generating the AI summarizer of the video, when you generated the summary text
- Do NOT use markdown
- Do NOT use **bold**
- Do NOT use ###
- Use plain clean text only

The transcript may be in Hindi, Punjabi, Hinglish, or English.

Understand the transcript regardless of language and provide the summary ONLY in English.
Please provide the following sections in your summary:
1. Short Summary
2. Important Insights


Transcript:
{transcript_text[:6000]}
"""
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"