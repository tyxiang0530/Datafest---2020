'''
FREE GOURDS
TAI XIANG
GUY THAMPAKKUL
SAM MILLETTE

get_results converts our text data to uniform numpy arrays mapped through a word to integer dictionary.
This data is then fed into our loaded sentiment analysis model and the results of analysis is outputted
to a csv file.
'''
from keras.preprocessing import sequence
import pickle
import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

# load in our word to integer dictionary
vocab_to_word_dict = pickle.load(open("vocab_to_word_dict", "rb"))

# helper method that convert words in the text to integers
def create_ints(str_in):
    tokens = word_tokenize(str_in)
    test_ints = []
    for line in tokens:
        try:
            test_ints.append(vocab_to_word_dict[line])
        except:
            test_ints.append(0)
    return test_ints

# helper method that create vectors of 500 integers so model can read them
def split_word_vectors(text_in):
    length = 500
    chunks = []
    padded = []
    if len(text_in) > length:
        # divides text that is too long into chunks that are 500 characters in length
        chunks = [text_in[x: x + 500] for x in range(0, len(text_in), 500)]
    else:
        chunks.append(text_in)
    # pad our text to length of 500 if it is too short
    chunks = sequence.pad_sequences(chunks, maxlen=500)
    return chunks

# calculate sentiment of a given piece of text
def calculate_sentiment(text_in):
    loaded_model = tf.keras.models.load_model("youtube_runner.h5")
    unsplit_vector = create_ints(text_in)
    if len(unsplit_vector) == 1 and unsplit_vector[0] == 0:
        print('none')
        return ''
    vectors_in = split_word_vectors(unsplit_vector)
    polarities = loaded_model.predict(vectors_in)
    if len(polarities) > 1:
        sum_pol = 0
        for polarity in polarities:
            sum_pol += polarity[0]
        averaged_polarity = sum_pol / len(polarities)
        print(averaged_polarity)
        return averaged_polarity
    if len(polarities) == 1:
        print(polarities[0][0])
        return polarities[0][0]

# outputs calculated sentiment into a csv file
def output_sentiment(country_in, category_num):
    file = open('/home/txaa2019/free_gourds/Youtube Grab/text_files/' + country_in + '/' + category_num + '-text.csv')
#     file = open('/home/txaa2019/free_gourds/Youtube Grab/text_files/All/' + country_in + '_all_text.csv')
#     file = open('/home/txaa2019/free_gourds/Youtube Grab/text_files/All/global_all_text.csv')
    csv_f = csv.reader(file)
    dates = []
    transcripts = []
    for column in csv_f:
        if len(column[0]) > 0:
            dates.append(column[0])
            transcripts.append(column[2])
        else:
            break
    for period, text in zip(dates, transcripts):
         with open('/home/txaa2019/free_gourds/Results/' + country_in + '/' + category_num + '-result.csv', 'a') as csvfile:
#         with open('/home/txaa2019/free_gourds/Results/All/' + country_in + '-result.csv', 'a') as csvfile:
#         with open('/home/txaa2019/free_gourds/Results/All/global-result.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([period, calculate_sentiment(text)])
            
countries = ['Australia', 'Canada', 'India', 'United Kingdom', 'United States']
categories = ['10', '19', '22', '24', '25', '26', '27', '28']
csv.field_size_limit(sys.maxsize)
for country in countries:
    for category in categories:
        output_sentiment(country, category)
        print('done')
