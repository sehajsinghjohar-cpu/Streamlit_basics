import os
import streamlit as st
from groq import Groq

st.set_page_config(page_title="Smart Summariser", page_icon="📝", layout="centered")

# ── Light theme styling ───────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background: #f8f9fb; }
[data-testid="stHeader"] { background: transparent; }
.title-block { text-align: center; padding: 2rem 0 1.5rem; }
.title-block h1 { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin: 0; }
.title-block p  { color: #6b7280; font-size: 0.95rem; margin-top: 0.4rem; }
.card {
    background: #ffffff; border: 1px solid #e5e7eb;
    border-radius: 12px; padding: 1.25rem 1.5rem; margin-top: 1.25rem;
}
.bullet { display: flex; gap: 10px; padding: 8px 0; border-bottom: 1px solid #f3f4f6; }
.bullet:last-child { border-bottom: none; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: #6366f1;
       flex-shrink: 0; margin-top: 6px; }
.bullet-text { font-size: 0.93rem; color: #374151; line-height: 1.6; }
.word-count { font-size: 0.78rem; color: #9ca3af; text-align: right; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-block">
  <h1>📝 Smart Summariser</h1>
  <p>Paste any text and get a clean 3-bullet summary powered by Groq</p>
</div>
""", unsafe_allow_html=True)

# ── API Key ───────────────────────────────────────────────────────────────────
api_key = os.environ.get("GROQ_API_KEY", "")
if not api_key:
    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    if not api_key:
        st.info("Enter your Groq API key above to get started.")
        st.stop()

client = Groq(api_key=api_key)

# ── Input ─────────────────────────────────────────────────────────────────────
text = st.text_area(
    "Paste your text here",
    height=220,
    placeholder="Paste any article, paragraph, or notes here...",
)

word_count = len(text.split()) if text.strip() else 0
st.markdown(f'<div class="word-count">{word_count} words</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col2:
    summarise = st.button("Summarise →", use_container_width=True)

# ── Summarise ─────────────────────────────────────────────────────────────────
if summarise:
    if not text.strip():
        st.warning("Please paste some text first.")
    elif word_count < 20:
        st.warning("Text is too short. Please paste at least 20 words.")
    else:
        with st.spinner("Summarising..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a summarisation assistant. "
                                "Always respond with exactly 3 bullet points. "
                                "Each bullet point must start with '- ' and be on its own line. "
                                "Be concise — each bullet should be one clear sentence. "
                                "Do not add any introduction or closing remarks."
                            ),
                        },
                        {
                            "role": "user",
                            "content": f"Summarise this text in 3 bullet points:\n\n{text}",
                        },
                    ],
                    temperature=0.4,
                    max_tokens=300,
                )

                raw = response.choices[0].message.content.strip()
                bullets = [
                    line.lstrip("-• ").strip()
                    for line in raw.splitlines()
                    if line.strip().startswith("-") or line.strip().startswith("•")
                ]

                if bullets:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("**Summary**")
                    for b in bullets:
                        st.markdown(
                            f'<div class="bullet"><div class="dot"></div>'
                            f'<div class="bullet-text">{b}</div></div>',
                            unsafe_allow_html=True,
                        )
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="card">{raw}</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:0.8rem;'>"
    "Powered by Groq LPU · llama-3.3-70b-versatile</p>",
    unsafe_allow_html=True,
)