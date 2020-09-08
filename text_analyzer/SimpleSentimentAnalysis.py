import nltk
import Subjects
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
translator = Translator()
sid = SentimentIntensityAnalyzer()

def detect_language(post):
    language = translator.detect(HebrewText)
    if language.lang == 'iw' or language.lang == 'he':
        language = 'Hebrew'
    elif language == 'en': language = 'English'
    else: language = language.lang
    return language

# check if word exist in each subject
# improve - currently returns only one subject per word
def find_word_in_subjects(word):
    subjects = Subjects.subjects
    for subject in subjects:
        print(subject)
        if word in subjects[subject]:  
            return subject
    return

# calculate post's subject
# improve - currently returns only one subject per post
def detect_post_subject(post):
    subjects_word_count = {}    # holds word count per subject
    postWords = post.split()
    threshold = 0.5*len(postWords)  # super strict threshold!
    print (threshold)

    for word in postWords:
        wordSubjcet = find_word_in_subjects(word)
        if wordSubjcet in subjects_word_count.keys():
            subjects_word_count[wordSubjcet] += 1
        else:
            subjects_word_count.update({wordSubjcet : 1})
    
    for subject in subjects_word_count:
        if subjects_word_count[subject] >= threshold:
            return subject
    return

def analyze_post(post):
    # translate text
    englishText = translator.translate(post).text
    print(englishText)

    # calculate post's subject
    subject = detect_post_subject(post)
    print(subject)

    # get emotions of text
    sentimentDict=sid.polarity_scores(englishText)
    print(sentimentDict)

    return sentimentDict

analyze_post("בדיקה")