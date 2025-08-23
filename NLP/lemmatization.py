import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources (only first time)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')   # WordNet data for lemmatizer

paragraph = """I have three visions for India. In 3000 years of our history, people from all over
the world have come and invaded us, captured our lands, conquered our minds.
From Alexander onwards, the Greeks, the Turks, the Mughals, the Portuguese, the British,
the French, the Dutch, all of them came and looted us, took over what was ours.
Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture,
their history and tried to enforce our way of life on them."""

# Sentence tokenization
sentences = nltk.sent_tokenize(paragraph)

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Process each sentence
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    # Remove stopwords and apply lemmatization
    words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)
