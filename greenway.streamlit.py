import streamlit as st

# Simplified POS categorization based on a basic dictionary
def get_word_category(word):
    word_categories = {
        "run": "Verb",
        "dog": "Noun",
        "beautiful": "Adjective",
        "quickly": "Adverb",
        "he": "Pronoun",
        "with": "Preposition",
        "and": "Conjunction",
    }
    return word_categories.get(word.lower(), "Unknown")

# Streamlit app
st.title("Simple Word Category Identifier")
word_input = st.text_input("Enter a word:")
if word_input:
    category = get_word_category(word_input)
    st.write(f"The word '{word_input}' is categorized as: {category}")
    
        
    
        
        
    
