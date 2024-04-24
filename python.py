import sys
import subprocess
# install nltk, pandas, matplotlib using pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib",'pandas','nltk'])
import nltk
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
file = open("paragraphs.txt")
data =file.read()
data
data_cleaned = data.replace(",", "").replace(".", "").replace("-","").replace("'s","").strip()
data_cleaned
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
words = data_cleaned.split()
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_words
word_counts = Counter(filtered_words)
word_counts
for word, count in word_counts.most_common():
    print(f"{word}: {count}")
    top_words = word_counts.most_common(15)
words, counts = zip(*top_words)
# Create a bar graph
plt.bar(words, counts , color="green" , alpha=0.5)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Frequency Count')
plt.xticks(rotation=60)
# Display the graph
plt.show()