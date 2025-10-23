from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

STOPWORDS = set(stopwords.words("english"))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Serve templates at /templates/<name> to match editor preview URLs like /templates/index.html
@app.route('/templates/<path:tpl>', methods=['GET'])
def serve_template(tpl):
    # Only allow simple filenames from the templates folder (no directory traversal)
    import os
    safe_name = os.path.basename(tpl)
    # Only allow these templates to be rendered (whitelist)
    allowed = {'index.html', 'landing.html'}
    if safe_name not in allowed:
        return ("Template not found", 404)
    return render_template(safe_name)


@app.route("/test", methods=["GET"])
def test():
    return "Test request received successfully. Service is running."


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("landing.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Select the predictor to be loaded from Models folder
        predictor = pickle.load(open(r"Models/model_xgb.pkl", "rb"))
        scaler = pickle.load(open(r"Models/scaler.pkl", "rb"))
        cv = pickle.load(open(r"Models/countVectorizer.pkl", "rb"))
    except FileNotFoundError as e:
        return jsonify({"error": f"Model file not found: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error loading models: {str(e)}"}), 500
    
    try:
        # Single string prediction
        if "text" in request.json:
            text_input = request.json["text"]
            predicted_sentiment = single_prediction(predictor, scaler, cv, text_input)
            return jsonify({"prediction": predicted_sentiment})
        else:
            return jsonify({"error": "No text provided"}), 400

    except Exception as e:
        return jsonify({"error": str(e)})


def single_prediction(predictor, scaler, cv, text_input):
    # Rule-based checks for obvious negative sentiment
    negative_keywords = ['not', 'no', 'never', 'disappointing', 'terrible', 'awful', 'bad', 'horrible', 'worst', 'hate', 'dislike', 'disappoint', 'disappointed', 'poor', 'worst', 'useless', 'waste', 'regret']
    text_lower = text_input.lower()
    
    # Check for negative keywords
    negative_count = sum(1 for word in negative_keywords if word in text_lower)
    
    # If we find any negative indicators, classify as negative
    if negative_count >= 1:
        return "Negative"
    
    # If we find "not" with positive words, classify as negative
    if 'not' in text_lower and any(word in text_lower for word in ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic']):
        return "Negative"
    
    # Use the ML model for other cases
    corpus = []
    stemmer = PorterStemmer()
    
    # Create a custom stopwords set that excludes negation words
    negation_words = {'not', 'no', 'never', 'none', 'nothing', 'nowhere', 'neither', 'nor'}
    custom_stopwords = STOPWORDS - negation_words
    
    review = re.sub("[^a-zA-Z]", " ", text_input)
    review = review.lower().split()
    review = [stemmer.stem(word) for word in review if not word in custom_stopwords]
    review = " ".join(review)
    corpus.append(review)
    X_prediction = cv.transform(corpus).toarray()
    X_prediction_scl = scaler.transform(X_prediction)
    y_predictions = predictor.predict_proba(X_prediction_scl)
    
    # Get the probability for positive class (index 1)
    positive_prob = y_predictions[0][1]
    negative_prob = y_predictions[0][0]
    
    # Use a more conservative threshold for positive classification
    return "Positive" if positive_prob > 0.7 else "Negative"


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # bind to 0.0.0.0 so the server is reachable from other hosts if needed
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
