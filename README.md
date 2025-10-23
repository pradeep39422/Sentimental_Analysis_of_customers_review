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
- **Alternative Interface**: Streamlit

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd qqqqSentimental_Analysis_of_customers
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Unix/MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💫 Running the Application

### Web Interface (Flask)

1. Start the Flask server:
   ```bash
   python api.py
   ```
   The server will start on http://127.0.0.1:5000

2. Access the web interface:
   - Open your browser and visit http://127.0.0.1:5000
   - Or http://127.0.0.1:5000/templates/landing.html

### Streamlit Interface (Alternative)

1. Make sure the Flask server is running (see above)
2. In a new terminal, run:
   ```bash
   streamlit run main.py
   ```

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

## 🔄 API Endpoints

### Sentiment Analysis
- **URL**: `/predict`
- **Method**: POST
- **Body**:
  ```json
  {
    "text": "Your text to analyze"
  }
  ```
- **Response**:
  ```json
  {
    "prediction": "Positive"
  }
  ```

### Test Endpoint
- **URL**: `/test`
- **Method**: GET
- **Response**: Server status message

## 🎯 Usage Examples

```python
# Using requests library
import requests
import json

# Local development
url = "http://127.0.0.1:5000/predict"
text = "I love this product! It's amazing!"

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps({"text": text})
)

print(response.json())  # {"prediction": "Positive"}
```

## 🔧 Configuration

The application can be configured using environment variables:

- `PORT`: Change the Flask server port (default: 5000)
- `PREDICTION_ENDPOINT`: Configure Streamlit client API endpoint

Example:
```bash
# Windows
set PORT=3000
python api.py

# Unix/MacOS
export PORT=3000
python api.py
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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.