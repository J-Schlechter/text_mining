
from wordcloud import WordCloud
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
new_stopwords = ["'s", "10", "'", "–", "still", "mr", "6", "5", "news24", "watch", "n't", "`", "’", "‘", "...", "250",
                 "3", "1.", "2.", "3", "4", "7", "8"]
stop_words.extend(new_stopwords)

# Read a text file and calculate frequency of words in it
with open("un_declaration_hr_text_data.txt", "r") as f:
    words = f.read().split()

data = dict()

for word in words:
    word = word.lower()
    if word in stop_words:
        continue

    data[word] = data.get(word, 0) + 1

word_cloud = WordCloud()

word_cloud.generate_from_frequencies(data)
word_cloud.to_file('image.png')