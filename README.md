Project Link: [https://spam-or-not-dilesh-bisen.streamlit.app/](https://spam-or-not-dilesh-bisen.streamlit.app/)

# <b>SMS Spam Classifier</b>

## <b>Overview</b>
The SMS Spam Classifier is a web application built using Streamlit, designed to detect whether an SMS message is spam or not. Leveraging machine learning algorithms, this tool provides fast and accurate predictions, offering a user-friendly interface for classifying messages.

## <b>Features</b>
- Real-time SMS Classification: Detect spam messages instantly with machine learning.
- Intuitive Interface: Easy-to-use design for seamless interaction.
- Accurate Predictions: Powered by a trained machine learning model.

## <b>Installation</b>
To set up and run the SMS Spam Classifier, follow these steps:
1. Clone the Repository:
   - git clone [https://github.com/Dilesh-Bisen/spam_classifier.github.io.git](https://github.com/Dilesh-Bisen/spam_classifier.github.io.git)
   - cd spam_classifier
2. Create a Virtual Environment:
   - python -m venv venv
   - source `venv\Scripts\activate` # On Windows
3. Install Dependencies:
   - Ensure you have the required libraries by running: pip install -r requirements.txt
4. Download NLTK Resources:
   Run the following script to download necessary NLTK resources:
   - import nltk
   - nltk.download('punkt')
   - nltk.download('stopwords')
5. Run the Application:
   - Start the Streamlit app with: streamlit run sms_spam.py

## <b>Usage</b>
- Enter your SMS message into the text area.
- Click the "Predict" button to classify the message.
- View the result indicating whether the message is spam or not.

## <b>Project Structure</b>
- sms_spam.py: Main Streamlit application script.
- requirements.txt: List of Python dependencies.
- tfidf_vectorizer.pkl: Pickled TF-IDF vectorizer.
- mnb_model.pkl: Pickled Multinomial Naive Bayes model.
- spam_logo.jpeg: Logo image for the sidebar.

## <b>Contributing</b>
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## <b>Contact</b>
For questions or support, please contact [2dileshbisen@gmail.com].
