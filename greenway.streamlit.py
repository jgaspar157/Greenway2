import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import streamlit as st

# Dynamically download required NLTK data
nltk.download('punkt', quiet=True)  # Tokenizer
nltk.download('averaged_perceptron_tagger', quiet=True)  # POS Tagger

# Function to determine the category of a word
def get_word_category(word):
    tokens = word_tokenize(word)  # Tokenize the word
    tagged = pos_tag(tokens)  # POS tagging
    # Extract the POS tag for the first token (if exists)
    if tagged:
        _, tag = tagged[0]
        return tag
    return "Unknown"

# Streamlit App
st.title("Dynamic Word Categorizer")
st.write("Enter a word to categorize it (e.g., noun, verb, adjective).")

word_input = st.text_input("Enter a word:")

if word_input:
    category = get_word_category(word_input)
    st.write(f"The word '{word_input}' is categorized as: {category}")
        
    
