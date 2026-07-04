# Streamlit_basics
# 📝 AI Text Summarizer using Streamlit & Groq

An AI-powered text summarization web application built with **Streamlit** and the **Groq API**. Users can securely provide their own Groq API key, upload or paste text, and instantly receive a concise summary in **three key bullet points**.

---

## 🚀 Features

- 🔑 Bring Your Own Groq API Key
- 📄 Upload or paste text for summarization
- 🤖 AI-powered summarization using Groq
- 📌 Generates exactly **3 concise bullet points**
- ⚡ Fast and efficient inference
- 🎨 Clean and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- python-dotenv

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
└── .env (optional)
```

> Update the structure above if your project contains additional files.

---

## ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

---

## 🔑 How to Use

1. Launch the application.
2. Enter your **Groq API Key**.
3. Upload or paste your text.
4. Click the **Summarize** button.
5. Receive a clean summary in **3 concise bullet points**.

---

## 📷 Workflow

```text
User Input
     │
     ▼
Enter Groq API Key
     │
     ▼
Upload/Paste Text
     │
     ▼
Groq AI Model
     │
     ▼
3-Point Summary
```

---

## 💡 Example

### Input

> Artificial Intelligence has transformed industries by automating repetitive tasks, improving decision-making through data analysis, and enabling innovative applications across healthcare, finance, education, and transportation.

### Output

- AI automates repetitive tasks, increasing efficiency.
- It improves decision-making through data analysis.
- AI is driving innovation across multiple industries.

---

## 🔒 Security

The application uses the Groq API key supplied by the user during runtime. The key is **not stored** by the application.

---

## 🌟 Future Enhancements

- PDF and DOCX document support
- Adjustable summary length
- Download summary as PDF or TXT
- Copy summary to clipboard
- Multi-language summarization
- Improved UI/UX

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ using **Python**, **Streamlit**, and **Groq**.
