import streamlit as st
import nltk
from nltk import pos_tag

# Streamlit interface
st.title("Word Category Identifier using NLTK")

# Text input for the user
word_input = st.text_input("Enter a word:")

def get_word_category(word):
    # Simple space-based tokenization: split the input string into words
    tokens = word.split()  # This works without needing any external resources
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
    
        
    
        
        
    
