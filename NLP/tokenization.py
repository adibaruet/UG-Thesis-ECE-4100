import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK data (only once)
nltk.download('punkt')

paragraph = """I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, and conquered our minds. From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why..."""

# Tokenizing sentences
sentences = sent_tokenize(paragraph)

# Tokenizing words
words = word_tokenize(paragraph)

print("Sentences:\n", sentences)
print("\nWords:\n", words)
