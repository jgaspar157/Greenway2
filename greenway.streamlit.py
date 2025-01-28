import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Make sure to download necessary nltk resources if they aren't present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

# Define a mapping for POS tag abbreviations to full definitions
pos_tags_full = {
    'CC': 'Coordinating conjunction',
    'CD': 'Cardinal number',
    'DT': 'Determiner',
    'EX': 'Existential there',
    'FW': 'Foreign word',
    'IN': 'Preposition or subordinating conjunction',
    'JJ': 'Adjective',
    'JJR': 'Adjective, comparative',
    'JJS': 'Adjective, superlative',
    'LS': 'List item marker',
    'MD': 'Modal',
    'NN': 'Noun, singular or mass',
    'NNS': 'Noun, plural',
    'NNP': 'Proper noun, singular',
    'NNPS': 'Proper noun, plural',
    'PDT': 'Predeterminer',
    'POS': 'Possessive ending',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun',
    'RB': 'Adverb',
    'RBR': 'Adverb, comparative',
    'RBS': 'Adverb, superlative',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': 'To',
    'UH': 'Interjection',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non-3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun',
    'WP$': 'Possessive wh-pronoun',
    'WRB': 'Wh-adverb'
}

# Function to determine the POS category of a word
def get_word_category(word):
    # Tokenize the input word
    tokens = word_tokenize(word)
    # Perform POS tagging
    tagged = pos_tag(tokens)

    # Retrieve the POS tag for the first word (since it's a single word input)
    tag = tagged[0][1]  # 'tagged[0][1]' is the POS tag of the word
    
    # Get the full description from the mapping
    pos_description = pos_tags_full.get(tag, "Unknown POS tag")
    
    return pos_description

# Streamlit input and output
st.title("Word POS Categorizer")
word_input = st.text_input("Enter a word:", "")

if word_input:
    category = get_word_category(word_input)
    st.write(f"The word '{word_input}' is categorized as: {category}")
