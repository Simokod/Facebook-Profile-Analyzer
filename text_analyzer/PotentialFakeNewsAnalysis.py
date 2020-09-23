import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
translator = Translator()
sid = SentimentIntensityAnalyzer()

def analyze_profile_potential_fake_news(posts):
    # get total posts num
    postsNum = len(posts)
    if postsNum==0:
        return "User doesn't have any posts."

    potentialFakePostsNum = 0

    for post in posts:
        if is_post_might_be_fake(post):
            potentialFakePostsNum+=1

    # calculate rate
    potentialFakeRate = potentialFakePostsNum / postsNum

    #convert rate to text result
    fakeResultText = convert_potential_fake_rate_to_text(potentialFakeRate)
    return fakeResultText

# check if post might be fake by analyzeing its polarity
def is_post_might_be_fake(post):  
    fake_threshold = 0.7
    englishText = translator.translate(post).text   # translate text
    sentimentDict = sid.polarity_scores(englishText)  # get emotions of text

    if sentimentDict['neg'] >= 0.7 or sentimentDict['pos'] >= 0.7:
        return True

    return False

def convert_potential_fake_rate_to_text(potentialFakeRate):
    for rate in potentialFakeNewsAnalsisTextResult.keys():
        if potentialFakeRate <= rate:
            return potentialFakeNewsAnalsisTextResult[rate]
    return ""

# dictinary of <offensive_rate, text_result>.
# used to convert offensive rate to text result.
# important! keep the rates going up from 0 to 1.
potentialFakeNewsAnalsisTextResult = {
    0.0 : "User is clean of potential fake news!",
    0.1 : "User is ok.",
    0.2 : "User rarely post potential fake news.",
    0.4 : "User often post potential fake news, pay attention!",
    0.6 : "User is problematic, most posts are potential fake news.",
    0.8 : "User is problematic, the vast majority of posts are potential fake news!",
    1 : "USER IS DANGEROUS! All posts are potential fake news!"
}

result = analyze_profile_potential_fake_news(["Idiot but realy realy good"])
print (result)