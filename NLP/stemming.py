import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required data (run only once)
nltk.download('stopwords')
nltk.download('punkt')

paragraph = """I have three visions for India. In 3000 years of our history, people from all over
the world have come and invaded us, captured our lands, conquered our minds.
From Alexander onwards, the Greeks, the Turks, the Mughals, the Portuguese, the British,
the French, the Dutch, all of them came and looted us, took over what was ours.
Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture,
their history and tried to enforce our way of life on them."""

# Sentence tokenization
sentences = nltk.sent_tokenize(paragraph)

# Create stemmer
stemmer = PorterStemmer()

# Process each sentence
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)
