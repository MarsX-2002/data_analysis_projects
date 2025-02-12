import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data (if not already installed)
nltk.download('stopwords')
nltk.download('punkt')

# Function to summarize text
def summarize_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Frequency table for scoring words
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    # Scoring sentences
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = sum(sentenceValue.values())
    average = int(sumValues / len(sentenceValue))

    # Create summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

# Streamlit UI
st.title("Text Summarizer")
st.write("Enter text to generate a summary.")

# Text input area
input_text = st.text_area("Input Text", height=200)

# Summarize button
if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
