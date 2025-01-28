import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import os

# Check if the necessary NLTK resources are already downloaded
nltk_data_path = os.path.expanduser('~') + '/nltk_data/tokenizers/punkt'

# Only download if the resources are not already present
if not os.path.exists(nltk_data_path):
    nltk.download('punkt', quiet=True)  # Tokenizer
    nltk.download('averaged_perceptron_tagger', quiet=True)  # POS tagger

# Streamlit interface
st.title("Word Category Identifier using NLTK")

# Text input for the user
word_input = st.text_input("Enter a word:")

def get_word_category(word):
    # Tokenize and POS tagging
    tokens = word_tokenize(word)
    tagged = pos_tag(tokens)  # POS tagging

    if tagged:
        pos_tag = tagged[0][1]  # Get POS tag for the first token
        # Return the category based on POS tag
        if pos_tag.startswith("NN"):
            return "Noun"
        elif pos_tag.startswith("VB"):
            return "Verb"
        elif pos_tag.startswith("JJ"):
            return "Adjective"
        elif pos_tag.startswith("RB"):
            return "Adverb"
        elif pos_tag.startswith("PRP"):
            return "Pronoun"
        elif pos_tag.startswith("IN"):
            return "Preposition"
        elif pos_tag.startswith("CC"):
            return "Conjunction"
        elif pos_tag.startswith("UH"):
            return "Interjection"
        else:
            return "Unknown"
    return "Unknown"

if word_input:
    category = get_word_category(word_input)
    st.write(f"The word '{word_input}' is categorized as: {category}")
        
    
