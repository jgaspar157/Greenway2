import streamlit as st
import nltk
from nltk import pos_tag

# Download necessary resources only if not already present
if not nltk.data.find('tokenizers/punkt'):
    nltk.download('punkt', quiet=True)  # Tokenizer
if not nltk.data.find('taggers/averaged_perceptron_tagger'):
    nltk.download('averaged_perceptron_tagger', quiet=True)  # POS tagger

# Streamlit interface
st.title("Word Category Identifier using NLTK")

# Text input for the user
word_input = st.text_input("Enter a word:")

def get_word_category(word):
    # Custom tokenization by splitting the input string into words
    tokens = word.split()  # Simple space-based tokenization
    tagged_words = pos_tag(tokens)  # POS tagging

    if tagged_words:
        word_tag = tagged_words[0][1]  # Get POS tag for the first token
        # Return the category based on POS tag
        if word_tag.startswith("NN"):
            return "Noun"
        elif word_tag.startswith("VB"):
            return "Verb"
        elif word_tag.startswith("JJ"):
            return "Adjective"
        elif word_tag.startswith("RB"):
            return "Adverb"
        elif word_tag.startswith("PRP"):
            return "Pronoun"
        elif word_tag.startswith("IN"):
            return "Preposition"
        elif word_tag.startswith("CC"):
            return "Conjunction"
        elif word_tag.startswith("UH"):
            return "Interjection"
        else:
            return "Unknown"
    return "Unknown"

if word_input:
    category = get_word_category(word_input)
    st.write(f"The word '{word_input}' is categorized as: {category}")


        
    
        
        
    
