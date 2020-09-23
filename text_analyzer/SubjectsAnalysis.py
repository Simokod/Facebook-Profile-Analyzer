import Subjects
from googletrans import Translator

def analyze_profile_subjects(posts):
    # get total posts num
    postsNum = len(posts)
    if postsNum==0:
        return "User doesn't have any posts."
    
    # check what is the rate of posts of each subject
    # create dict of results: <subject, subjectPostsRate>
    subjects = Subjects.subjects
    subjectsPostsCount = {}
    
    # count how may posts are there for each subject
    for post in posts:
        subjectsPostsCount = detect_post_subjects(post, subjectsPostsCount)

    # calculate subjects rates
    subjectsPostsRates = {}
    for subject in subjectsPostsCount.keys():
        subjectsPostsRates[subject] = subjectsPostsCount[subject] / postsNum  # calculate rate of posts in this subject
    
    #convert to text result
    subjectsResultText = convert_subjects_rates_to_text(subjectsPostsRates)
    return subjectsResultText

# calculate post's subject and add to counter dictionary
# improve - currently returns only one subject per post
def detect_post_subjects(post, counterDictionary):
    subjects_word_count = {}    # holds word count per subject
    postWords = post.split()
    postWordsNum = len(postWords)

    threshold = 0.05*postWordsNum   # threshold!

    for word in postWords:
        wordSubjcet = find_word_in_subjects(word)
        increase_count(subjects_word_count, wordSubjcet)
    
    # increase post subject in counter dict
    for subject in subjects_word_count:
        if subjects_word_count[subject] >= threshold:
            increase_count(counterDictionary, subject)
            
    return counterDictionary

def increase_count(dictionary, subject):
    if subject in dictionary.keys():
        dictionary[subject] += 1
    else:
        dictionary.update({subject : 1})
    return

# check if word exist in each subject
# improve - currently returns only one subject per word
def find_word_in_subjects(word):
    subjects = Subjects.subjects
    for subject in subjects:
        if word in subjects[subject]:  
            return subject
    return

def convert_subjects_rates_to_text(subjectsPostsRates):
    textResult = "Posts of user according to subjects: "

    for subject in subjectsPostsRates.keys():
        textResult += subject + ": " + str(subjectsPostsRates[subject]) + ","
    
    return textResult[:-1]  # trim the last ","


result = analyze_profile_subjects(["פוליטיקה", "לסביות"])
print(result)