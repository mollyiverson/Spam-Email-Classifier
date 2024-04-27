import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Data Pre-processing
# Remove all puncuation and any common english word (such as pronouns and articles). 
# A list of these words can be found in the nltk.corpus library.

def contains_letter(word):
    return any(char.isalpha() for char in word)

def is_not_stopword(word):
  stop_words = set(stopwords.words('english'))
  return word.lower() not in stop_words

def preprocess_data(email):
  array = email.split(" ")
  filtered_words = [word for word in array if contains_letter(word)]
  filtered_no_stop_words = [word for word in filtered_words if is_not_stopword(word)]
  return " ".join(filtered_no_stop_words)