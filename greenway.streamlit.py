import streamlit as st

# Basic categorization logic based on word endings and patterns
def categorize_word(word):
    if word.endswith("ing") or word.endswith("ed"):  # Example: walking, played
        return "Verb"
    elif word.endswith("ly"):  # Example: quickly, slowly
        return "Adverb"
    elif word.endswith("ous") or word.endswith("ful") or word.endswith("ive"):  # Example: cautious, beautiful
        return "Adjective"
    elif word.isalpha() and word[0].isupper():  # Example: Proper nouns like John
        return "Proper Noun"
    elif word.isalpha():  # Default for simple words
        return "Noun"
    else:  # Fallback for unrecognized words
        return "Unknown"

# Streamlit app
st.title("Dynamic Word Categorizer")
st.write("Enter a word, and I'll try to identify its category dynamically!")

# User input
word_input = st.text_input("Enter a word:")

# Process the input and categorize
if word_input:
    category = categorize_word(word_input.strip())
    st.write(f"The word '{word_input}' is categorized as: {category}")
    
        
    
        
        
    
