# Customer Sentiment Analysis Tool 🎭

An AI-powered sentiment analysis tool that analyzes customer feedback and determines whether the sentiment is positive or negative. Built with Flask, NLTK, and machine learning.

## 🌟 Features

- Real-time sentiment analysis of text input
- Pre-trained machine learning model (XGBoost)
- Interactive web interface
- Example suggestions for quick testing
- RESTful API endpoint for integration
- Support for both web UI and Streamlit interface

## 🛠️ Tech Stack

- **Backend**: Python, Flask, NLTK
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn, XGBoost
- **Data Processing**: pandas, numpy

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 📁 Project Structure

```
├── api.py                 # Flask server and API endpoints
├── main.py               # Streamlit interface
├── requirements.txt      # Project dependencies
├── Data/
│   ├── amazon_alexa.tsv  # Training data
│   └── Predictions.csv   # Model predictions
├── Models/
│   ├── model_xgb.pkl     # Trained XGBoost model
│   ├── scaler.pkl        # Feature scaler
│   └── countVectorizer.pkl # Text vectorizer
└── templates/
    ├── index.html        # Main web interface
    └── landing.html      # Alternative landing page
```

## 🧪 Model Details

The sentiment analysis model uses:
- XGBoost classifier
- NLTK for text preprocessing
- Custom stopwords handling (preserves negation words)
- Rule-based enhancements for common sentiment patterns
- Conservative threshold for positive classification (0.7)

## 📝 Development Notes

- The web interface is responsive and works on mobile devices
- CORS is enabled for API access from different origins
- The model handles negations specially (e.g., "not good" → negative)
- Examples are provided in the UI for quick testing

## 📝 Future scope of work 

- Analyze large-scale data from CSV or text files for efficient sentiment analysis.
- Visualizing results using interactive graphs and charts for easier interpretation.
- Enable multilingual sentiment detection to serve diverse user bases.
