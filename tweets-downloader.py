import twitter


def auth():
        # fill with your keys/secrets:
        api = twitter.Api(consumer_key='', 
                    consumer_secret='', 
                    access_token_key='', 
                    access_token_secret='')
        return api

def format_date(dateString):
        monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return dateString.split(" ")[2] + "/" + str(monthNames.index(dateString.split(" ")[1]) + 1) + "/" + dateString.split(" ")[5] + " " + dateString.split(" ")[3]

def number_of_hashtags(tweetText):
        number = 0
        for i in range(len(tweetText)):
            if tweetText[i] == '#':
                number += 1
        return number

def isRetweet(tweetText):
        return 'RT @' in tweetText

def get_msg():
        api = auth()
        response = api.GetSearch(term='Trump',count=100,since='2018-11-22')
        
        # place the address of the output file that will receive DML commands
        fileAddress = 'C:\\Users\Gustavo\Desktop\Projeto - BD\Oficial\populate.dml'
        f = open(fileAddress,'w')
        for r in response:       
                f.write('INSERT INTO TWEET (CREATED_AT, FAVORITE_COUNT, TWEET_ID, LANG, RETWEET_COUNT, IS_RETWEET, HASHTAG_COUNT, TEXT) VALUES (' \
                + "\'" + format_date(r.__getattribute__("created_at")) + "\'" + ', ' \
                + str(r.__getattribute__("favorite_count")) + ', ' \
                + str(r.__getattribute__("id")) + ', ' \
                + "\'" + r.__getattribute__("lang") + "\'" + ', ' \
                + str(r.__getattribute__("retweet_count")) + ', ' \
                + str(isRetweet(str(r.__getattribute__("text").replace("\n","\\n").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'"))) + ', ' \
                + str(number_of_hashtags(str(r.__getattribute__("text").replace("\n","\\n").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'"))) + ', ' \
                + "\'" + str(r.__getattribute__("text").replace("\n","\\n").encode("utf-8")).replace("\'", "\'\'").replace("\"", "\\\"").replace("\\'", "'") + "\'" + ");\n")
        
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