import twitter
import sentiment


def auth():
        # fill with your keys/secrets:
        api = twitter.Api(consumer_key='1Fh35OeccapZwbbMuM9cstovh', 
                    consumer_secret='NIdbKdMlyCD8DNv4IOPyreZCcoDySj1AVSfPPrHdLYmMDxdEIa', 
                    access_token_key='213832841-5b7nFkxL0obw1z03tsWlHT7wEHomZ4CXNunlQHxm', 
                    access_token_secret='YOHgVNHSoMkstsLPF4GAoVyreRfn8D7tDu2dy7ztyStlZ')
        return api

def fill(num):
    Str = str(num)
    if len(Str) == 2: return Str
    return "0" + Str

def format_date(dateString):
        monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return dateString.split(" ")[5] + "-" + fill(monthNames.index(dateString.split(" ")[1]) + 1) + "-" + dateString.split(" ")[2] + " " + dateString.split(" ")[3]

def number_of_hashtags(tweetText):
        number = 0
        for i in range(len(tweetText)):
            if tweetText[i] == '#':
                number += 1
        return number

def isRetweet(tweetText):
        return 'RT @' in tweetText

def get_tweet_sentiment(tweetText):
        return sentiment.tweet_sentiment(sentiment.tweet_polarity(tweetText))

def get_sentiment_value(tweetText):
        return sentiment.tweet_polarity(tweetText)

def get_msg():
        api = auth()
        response = api.GetSearch(term='Trump',lang='en',count=150,since='2018-11-22')
        
        # place the address of the output file that will receive DML commands
        fileAddress = 'C:\\Users\Gustavo\Desktop\Projeto - BD\Oficial\populate.dml'
        f = open(fileAddress,'w')
        for r in response:       
                u = r.__getattribute__("user")
                f.write('INSERT INTO TWEET (USER_NAME, VERIFIED, FAVOURITES_COUNT, FOLLOWERS_COUNT, FRIENDS_COUNT, TWEET_ID, CREATED_AT, LANG, RETWEET_COUNT, FAVORITE_COUNT, IS_RETWEET, HASHTAG_COUNT, TEXT, TWEET_SENTIMENT, SENTIMENT_VALUE, TWEET_LENGTH) VALUES (' \
                + "\'" + str(u.__getattribute__("name").replace("\n","\\n").replace("&","").encode('utf-8', errors='ignore')).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'")[3:-2] + "\'" + ', ' \
                + "\'" + str(u.__getattribute__("verified")) + "\'" + ', ' \
                + str(u.__getattribute__("favourites_count")) + ', ' \
                + str(u.__getattribute__("followers_count")) + ', ' \
                + str(u.__getattribute__("friends_count")) + ', ' \
                + str(r.__getattribute__("id")) + ', ' \
                + "\'" + format_date(r.__getattribute__("created_at")) + "\'" + ', ' \
                + "\'" + r.__getattribute__("lang") + "\'" + ', ' \
                + str(r.__getattribute__("retweet_count")) + ', ' \
                + str(r.__getattribute__("favorite_count")) + ', ' \
                + "\'" + str(isRetweet(str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'"))) + "\'" +  ', ' \
                + str(number_of_hashtags(str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'"))) + ', ' \
                + "\'" + str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'")[3:-2] + "\'" + ', ' \
                + "\'" + get_tweet_sentiment(str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'")) + "\'"  + ', '\
                + str(get_sentiment_value(str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'")))  + ', '\
                + str(len(str(r.__getattribute__("text").replace("\n","\\n").replace("&","").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'")[3:-2])) + ");\n")
        
                """u = r.__getattribute__("user")
                f.write('INSERT INTO USER (CREATED_AT, DESCRIPTION, FAVOURITES_COUNT, FOLLOWERS_COUNT, FRIENDS_COUNT, ' \
                + 'ID, LANG, LISTED_COUNT, LOCATION, NAME, SCREEN_NAME, STATUSES_COUNT, URL, VERIFIED) VALUES (' \
                + "\'" + format_date(u.__getattribute__("created_at")) + "\'" + ', ' \
                + "\'" + str(u.__getattribute__("description").encode('utf-8', errors='ignore')).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'") + "\'" + ', ' \
                + str(u.__getattribute__("favourites_count")) + ', ' \
                + str(u.__getattribute__("followers_count")) + ', ' \
                + str(u.__getattribute__("friends_count")) + ', ' \
                + str(u.__getattribute__("id")) + ', ' \
                + "\'" + u.__getattribute__("lang") + "\'" + ', ' \
                + str(u.__getattribute__("listed_count")) + ', ' \
                + "\'" + str(u.__getattribute__("location").encode('utf-8', errors='ignore')).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'") + "\'" + ', ' \
                + "\'" + str(u.__getattribute__("name").encode('utf-8', errors='ignore')).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'") + "\'" + ', ' \
                + "\'" + str(u.__getattribute__("screen_name").encode('utf-8', errors='ignore')).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'") + "\'" + ', ' \
                + str(u.__getattribute__("statuses_count")) + ', ' \
                + "\'" + str(u.__getattribute__("url")) + "\'" + ', ' \
                + str(u.__getattribute__("verified")) + ');\n')"""
        f.close()


if __name__ == '__main__':
        get_msg()