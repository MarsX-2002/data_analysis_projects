# STEP 1: Importing libraries
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# corpus - collection of text
# tokenizers (words, sentences, regex) - split text into tokens 

# input text
text = """There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar."""

# tokenize text
stopwords = set(stopwords.words("english"))
words = word_tokenize(text)
freqTable = dict()

# frequency table, to keep score of each word
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopwords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# dict to keep score of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq


sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

#  average value of a sentence from original text
average = int(sumValues / len(sentenceValue)) 

# storing sentences into summary
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

print(f'INPUT: {text}')
print('#' * 50)
print(f'SUMMARY: {summary}')         










