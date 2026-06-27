````md
# 🎥 YouTube Video Summarizer

A web application that summarizes YouTube videos into concise, easy-to-read insights using **Google Gemini AI**.

Instead of watching an entire video to extract the important points, simply paste a YouTube link and let the app generate a structured summary for you.

---

## 🚀 Features

- 🔗 Accepts YouTube video URLs
- 📝 Extracts video transcript/captions
- 🤖 Uses Gemini AI to generate summaries
- 🌍 Supports multiple languages (English, Hindi, Spanish, etc.)
- 📌 Provides:
  - Short Summary
  - Key Points
  - Important Insights
- 🎨 Clean UI built using HTML + CSS

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### AI / APIs
- Google Gemini API
- YouTube Transcript API

### Frontend
- HTML
- CSS

### Deployment
- Render / Railway (tested)

---

## 📷 Project Preview

The application allows users to:

1. Select the language of the video  
2. Paste a YouTube video link  
3. Click **Summarize**  
4. Get an AI-generated summary in seconds  

---

## ⚙️ How It Works

### Step 1: User enters YouTube URL
Example:

```text
https://www.youtube.com/watch?v=example
````

### Step 2: Extract video ID

The backend extracts the video ID from the URL.

### Step 3: Fetch transcript

The app retrieves video captions/transcripts using `youtube-transcript-api`.

### Step 4: Send transcript to Gemini

Transcript is sent to Gemini AI with a custom prompt.

### Step 5: Generate summary

Gemini returns a structured summary containing:

* Short Summary
* Key Points
* Important Insights

---

## 📂 Project Structure

```bash
youtube/
│ app.py
│ summarizer.py
│ .env
│ requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── assets/
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from:

https://ai.google.dev/

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/Aabir265/YT-Video-Summarizer.git
cd YT-Video-Summarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask app:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## ⚠️ Known Limitation

This project works well in local development.

However, during cloud deployment (Render/Railway), transcript fetching may fail because **YouTube blocks requests from cloud provider IP addresses**.

This affects the `youtube-transcript-api` library and is a known limitation.

In short:

* ✅ Works locally
* ⚠️ May fail on cloud deployments due to YouTube restrictions

This was a valuable lesson in understanding the difference between local development and production deployment.

---

## Challenges I Faced

Building this project taught me a lot, especially because I faced multiple real-world issues:

* Managing API keys using `.env`
* Connecting Flask backend with frontend templates
* Handling Git & GitHub deployment issues
* Styling UI with HTML/CSS
* Understanding why code can work locally but fail in production

This project helped me understand that software engineering is not just about writing code — debugging, deployment, and handling external service limitations are equally important.

---

## Future Improvements

Some improvements I plan to add:

* 🎙 Speech-to-text fallback when captions are unavailable
* 📄 Export summary as PDF
* 📌 Timestamp-based summaries
* 📚 Save summary history
* 🔊 Summarize videos without subtitles

---

## 🙌 Final Thoughts

This is one of my first end-to-end AI projects combining:

* Backend development
* Frontend design
* API integration
* Deployment
* Generative AI

It was challenging, frustrating, and exciting at the same time.

I learned far more from debugging this project than from just watching tutorials.

---

## 👨‍💻 Author

**Aabir Sharma**
Computer Engineering Student | AI/ML Enthusiast | Aspiring AI Engineer

GitHub: https://github.com/Aabir265

```
```
