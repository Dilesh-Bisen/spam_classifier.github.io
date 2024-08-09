import pickle
import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import time

ps = PorterStemmer()


def convert(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    temp = [ps.stem(i) for i in text if i.isalnum() and i not in stopwords.words('english')]
    return " ".join(temp)


tfidf_vector = pickle.load(open('03_SMS_SPAM/Output_file/tfidf_vectorizer.pkl', 'rb'))
mnb_model = pickle.load(open('03_SMS_SPAM/Output_file/mnb_model.pkl', 'rb'))

st.set_page_config(page_title="SMS Spam Classifier", page_icon="🚨", layout="centered", initial_sidebar_state="expanded")

with st.sidebar:
    st.image('03_SMS_SPAM/Output_file/spam_logo.jpeg', use_column_width=True)
    st.markdown('## Welcome to the Spam Classifier')
    st.markdown('This tool uses Machine Learning to detect whether an SMS message is spam or not.')
    st.markdown('### Features:')
    st.markdown('* **Fast and Accurate Predictions**')
    st.markdown('* **Simple and Intuitive Interface**')
    st.markdown('---')
    st.markdown('**Instructions:**')
    st.markdown('1. Enter the SMS message in the text area below.')
    st.markdown('2. Click on the "Predict" button.')
    st.markdown('3. See the result instantly!')
    st.markdown('---')

# Main content
st.markdown('<h1 style="color:#39FF14;">SMS Spam Classifier</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#00FFFF;">Classify your messages with the power of Machine Learning.</p>',
            unsafe_allow_html=True)

# Input section
input_msg = st.text_area("Enter a message")

# Prediction section
if st.button('Predict'):
    if input_msg:
        with st.spinner('Analyzing...'):
            time.sleep(1)  # Simulate processing time
        transformed_msg = convert(input_msg)
        input_vector = tfidf_vector.transform([transformed_msg])
        predict = mnb_model.predict(input_vector)[0]

        # Display result
        if predict == 1:
            st.markdown('<h2 style="color:#FF0000;">🚨 Spam Message 🚨</h2>', unsafe_allow_html=True)
            st.markdown('<p style="color:#FF6347;">This message has been flagged as spam.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<h2 style="color:#00FF00;">✔️ Not a Spam Message ✔️</h2>', unsafe_allow_html=True)
            st.markdown('<p style="color:#32CD32;">This message is safe and not classified as spam.</p>',
                        unsafe_allow_html=True)
    else:
        st.warning("Please enter a message to classify.")

st.markdown("""
    <style>
        .stButton>button {
            background: linear-gradient(45deg, #1e90ff, #00buff);
            color: white;
            border-radius: 50px;
            border: none;
            padding: 10px 25px;
            font-size: 16px;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease, transform 0.2s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #00buff, #1e90ff);
            transform: scale(1.05);
        }
        .stButton>button:active {
            background: linear-gradient(45deg, #1e90ff, #00buff);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transform: scale(0.98);
        }
        .css-1d391kg { 
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)
