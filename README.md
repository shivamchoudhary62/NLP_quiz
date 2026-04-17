# 📉 Time Series NPTL Quiz Dashboard

An interactive quiz application for the **NPTEL Time Series Analysis** course, built with Streamlit. Test and reinforce your understanding of time series concepts — from stationarity basics to machine learning forecasting.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivamchoudhary62-nlp-quiz.streamlit.app)

---

## ✨ Features

- **12 Weeks** of curated questions covering the full NPTEL syllabus
- **121 Questions** with detailed explanations for every answer
- **Practice Mode** — instant feedback after each question
- **Test Mode** — submit all answers at once, then review
- **🔀 Mixed Quiz** — shuffled questions from selected weeks with configurable question count
- **📊 Performance Dashboard** — track scores, attempts, and best results
- **Premium UI** — white theme with smooth animations, gradient accents, and responsive design

---

## 📚 Weekly Topics

| Week | Topic | Questions |
|------|-------|:---------:|
| 1 | Introduction to Time Series Data | 10 |
| 2 | White Noise, AR, MA Models & Decomposition | 10 |
| 3 | ARIMA, Seasonality & Stationarity Tests | 10 |
| 4 | Model Selection, Estimation & Diagnostics | 10 |
| 5 | Forecasting & Exponential Smoothing | 10 |
| 6 | Long Memory, ARFIMA & Hurst Exponent | 10 |
| 7 | Multivariate Time Series & VAR/VMA Models | 10 |
| 8 | Cointegration, ECM & Granger Causality | 10 |
| 9 | Spectral Analysis & Frequency Domain | 10 |
| 10 | Volatility Modelling: ARCH & GARCH | 10 |
| 11 | Nonlinear Models: TAR, STAR & MSM | 10 |
| 12 | Machine Learning for Time Series | 11 |

---

## 🚀 Quick Start

### Run Locally

```bash
# Clone the repository
git clone https://github.com/shivamchoudhary62/NLP_quiz.git
cd NLP_quiz

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Deploy on Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repo → Branch: `main` → Main file: `app.py`
5. Click **Deploy**

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** — Web framework
- **Python 3.8+** — Backend logic
- **Custom CSS** — Premium white theme with Inter font

---

## 📂 Project Structure

```
NLP_quiz/
├── app.py              # Main Streamlit application
├── questions.py        # Question bank (12 weeks, 121 questions)
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🤝 Contributing

Want to add more questions or improve the UI? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b add-week-13`)
3. Add your questions to `questions.py` following the existing format
4. Commit and push
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational purposes.

---

<p align="center">
  Built with ❤️ for NPTEL Time Series Analysis students
</p>
