
from shlex import split

from flask import Flask, render_template, request
from summarizer import get_video_summary

app = Flask(__name__)


# -------- Home Page --------
@app.route("/")
def home():
    return render_template("index.html")


# -------- Helper Function --------
def extract_video_id(url):
    if "youtu.be/" in url:
        # Example: https://youtu.be/abc123?si=xyz
        return url.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com" in url:
        return url.split("v=")[1].split("&")[0]


    else:
        return None


# -------- Summarize Route --------
@app.route("/summarize", methods=["POST"])
def summarize_video():
    youtube_url = request.form.get("video_url")
    language = request.form.get("language")

    if not youtube_url:
        return render_template(
            "index.html",
            summary="Error: No URL provided"
        )

    video_id = extract_video_id(youtube_url)

    if not video_id:
        return render_template(
            "index.html",
            summary="Error: Invalid YouTube URL"
        )

    summary = get_video_summary(video_id)

    return render_template(
        "index.html",
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)
