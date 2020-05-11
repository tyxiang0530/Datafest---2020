from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from nltk.tokenize import word_tokenize
import string
import os
import pickle
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer
import io
import re
import numpy as np
import csv


# preprocess_reviews removes non-alphabetical characters, stop words, and lemmatizes dataset
def preprocess_text(reviews):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(reviews)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining non-alphabetic words
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words('english')+list(punctuation))
    cleaned = [w for w in words if w not in stop_words]
    super_clean = [lemmatizer.lemmatize(word) for word in cleaned]
    return super_clean
    
def write_to_file(transcript_in, country, category):
    output = open("/home/txaa2019/free_gourds/Youtube Grab/text_files/" + country + "/" + 
                  category + ".txt", "a")
    output.write(transcript_in)
    output.write('\n')
    output.close()
   
def get_transcripts(video_id, country_in, category_in):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    trans_all = []
    trans_str = ''
    try:
        transcript = transcript_list.find_transcript(['en', 'en-US'])
        text = transcript.fetch()
        for t in text:
            clean = preprocess_text(t.get('text'))
            trans_all.append(clean)
        for i in trans_all:
            for x in i:
                trans_str += x + ' '
    except:
        try: 
            transcript = transcript_list.find_transcript([
                'de', 'zh_Hans', 'fr', 'zh-Hant', 'es',
                'ar', 'hi', 'it', 'ru', 'vi', 'th', 'sv',
                'fa', 'pt', 'cs', 'na', 'nl', 'el', 'fil', 'zh-TW'
            ])
            translated_transcript = transcript.translate('en')
            text = translated_transcript.fetch()
            for t in text:
                clean = preprocess_text(t.get('text'))
                trans_all.append(clean)
            for i in trans_all:
                for x in i:
                    trans_str += x + ' '
        except:
            trans_str = ''
    write_to_file(trans_str, country_in, category_in)

file = open('/home/txaa2019/free_gourds/Youtube Grab/Categories/United States/10.csv')
csv_f = csv.reader(file)
links_in = []
for column in csv_f:
    links_in.append(column[1][32:])
for x in links_in:
    get_transcripts(x, 'United States', '10')
