from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt


def plot_top_words():
    # Read the text file
    with open('un_declaration_hr_text_data.txt', 'r') as file:
        text = file.read()

    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Remove punctuation and convert to lowercase
    table = str.maketrans('', '', string.punctuation)
    tokens = [word.translate(table).lower() for word in tokens]

    # Remove stop words
    stop_words = stopwords.words('english')
    new_stopwords = ["'s", "10", "'", "–", "still", "mr", "6", "5", "news24", "watch", "n't", "`", "’", "‘", "...",
                     "250", "3", "1.", "2.", "3", "4", "7", "8", "", "1", "2"]
    stop_words.extend(new_stopwords)
    tokens = [word for word in tokens if word not in stop_words]

    # Count the frequency of words
    fdist = FreqDist(tokens)
    top_words = fdist.most_common(25)

    # Extract the words and frequencies
    words = [word[0] for word in top_words]
    frequencies = [word[1] for word in top_words]

    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 25 Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('Top_25_bar_chart')