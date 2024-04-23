import nltk
import re
nltk.download('stopwords')
from collections import Counter
from nltk.corpus import stopwords
# Function to remove punctuation and convert text to lowercase
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert text to lowercase
    return text
    # Function to remove stop words
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
    # Read the contents of the file
with open("paragraphs.txt", "r") as file:
    text = file.read()
# Preprocess the text
text = preprocess_text(text)
# Remove stop words
text = remove_stopwords(text)
# Count the frequency of each word
word_count = Counter(text.split())
# Display word frequency count
for word, count in word_count.items():
    print(f"{word}: {count}")