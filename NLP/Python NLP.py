import textract
import docx2txt
import nltk
import nltk.corpus
import os
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def unicodetoascii(text):

    TEXT = (text.
    		replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")")

                 )
    return TEXT



#nltk.download('punkt')
text = textract.process(r"C:\Users\Cheng\OneDrive\桌面\WIN History Project\Argo Archive Word\converted word documents\1-28-1949 Leela Menon(scan)pdf_00001.docx")
text = str(text)
text = unicodetoascii(text.replace("\\n", "\n"))

#nltk.download("stopwords")

tokenized_word = word_tokenize(text)
year = re.findall(r'.*([1-3][0-9]{3})', text)

sorted_year = dict()
directory = r"C:\Users\Cheng\OneDrive\桌面\WIN History Project\Argo Archive Word\converted word documents"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    text = textract.process(f)
    text = str(text)
    text = unicodetoascii(text.replace("\\n", "\n"))
    years = re.findall(r'.*([1-2][0789]{3})', text)
    for year in years:
        if year not in sorted_year.keys():
            this_list = [str(f)]
            sorted_year[year] = this_list
        else:
            sorted_year[year].append(str(f))

print(sorted_year.keys())



filtered = []
stop_words = set(stopwords.words("english"))
for word in tokenized_word:
  if word.casefold() not in stop_words:
    filtered.append(word)




