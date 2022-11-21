import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt
from twitter import *
import sys
import csv
import time
import os
class SentimentAnalysis:
    def __init__(self):
        self.tweets = []
        self.tweetText = []
    def DownloadData(self):
        consumerKey="928XAZNTAphdsa46XcBq5lw0N"
        consumerSecret="8wzjnVlIOTFQZ4kdWRCCNKxhw1IlP459eYPsYf5OtmLpsEj71x"
        accessToken="1073938747811655681-N4QtBmlUnXbS9SKfrtdcgh6iMAT6kI"
        accessTokenSecret="PxTp190G45Pq75nTsFNMs45B20wEUgIvLX6rnMATaKLVI"
        auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
        auth.set_access_token(accessToken,accessTokenSecret)
        api = tweepy.API(auth)
        searchTerm = raw_input("Enter Keyword/Tag to search about: ")
        global NoOfTerms
        NoOfTerms = int(raw_input("Enter how many tweets to search: "))
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)
        csvFile = open('result.csv', 'a')
        csvWriter = csv.writer(csvFile)
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0


        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity
            if (analysis.sentiment.polarity == 0):
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1


        csvWriter.writerow(self.tweetText)
        csvFile.close()

        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        polarity = polarity / NoOfTerms

        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(wpositive) + "% people thought it was weakly positive")
        print(str(spositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(wnegative) + "% people thought it was weakly negative")
        print(str(snegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")
        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)


    def cleanTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
        print("yes")
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
try:
	from twitter import *
	import sys
	import csv
	import time
	import os

	class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	#latitude = float(input(bcolors.OKGREEN +  'Enter the Latitude: ' + bcolors.ENDC))
	#longitude = float(input(bcolors.OKGREEN + 'Enter the Longitude: ' + bcolors.ENDC))
	latitude=51.474144
	longitude=-0.035401
	con=raw_input(bcolors.OKGREEN +  'Enter the con: ' + bcolors.ENDC)
	#max_range = float(input(bcolors.OKGREEN + 'Enter the Range: ' + bcolors.ENDC))
	max_range=1
	global NoOfTerms
	#num_results = input(bcolors.OKGREEN +     'Enter the Number of results: ' + bcolors.ENDC)
	num_results=NoOfTerms
	outfile = "output.csv"

	config = {}
	execfile("config.txt", config)

	# create twitter API object
	twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

	# open a file to write (mode "w"), and create a CSV writer object
	csvfile = file(outfile, 'w')
	csvwriter = csv.writer(csvfile)

	row = ["Username", "Profile URL", "Latitude", "Longitude","Google Maps","Tweet"]
	csvwriter.writerow(row)
	result_count = 0
	last_id = None
	while result_count < num_results:

		query = twitter.search.tweets(q="", geocode="%f,%f,%dkm" % (latitude, longitude, max_range), num_results=100, max_id=last_id)
		for result in query["statuses"]:
			if result["geo"]:
				user = result["user"]["screen_name"]
				text = result["text"]
				text = text.encode('ascii', 'replace')
				latitude = result["geo"]["coordinates"][0]
				longitude = result["geo"]["coordinates"][1]
				url = 'https://twitter.com/%s' % user
				gurl = 'https://maps.google.com/?q=' + str(latitude) + ',' + str(longitude)

				row = [user, url, latitude, longitude,gurl, text]
				print '-----------------------------------------------------------------'
				print  ' '
				print bcolors.OKGREEN +'Username:    '+ bcolors.ENDC, user
				print bcolors.OKGREEN +'Profile URL: '+ bcolors.ENDC, url
				print bcolors.OKGREEN +'Latitude:    '+ bcolors.ENDC, latitude
				print bcolors.OKGREEN +'Longitude:   '+ bcolors.ENDC, longitude
				print bcolors.OKGREEN +'Google Maps: '+ bcolors.ENDC, gurl
				print bcolors.OKGREEN +'Tweet:       '+ bcolors.ENDC, text
				print  ' '
				csvwriter.writerow(row)
				result_count += 1
				time.sleep(.35)
			last_id = result["id"]


	if result_count == 1:
		print bcolors.WARNING + "Got %d result" % result_count + bcolors.ENDC
		csvfile.close()
		print bcolors.WARNING + "Saved to ", outfile + bcolors.ENDC
	elif result_count == 0:
		print bcolors.WARNING + "Didn't get any results try another Latitude and  Longitude" + bcolors.ENDC
	else:
		print bcolors.WARNING + "Got %d results" % result_count + bcolors.ENDC
		csvfile.close()
		print bcolors.WARNING + "Saved to ", outfile + bcolors.ENDC

except ImportError:
	print ('''There was an error Please install the requirements: pip install -r requirements.txt''')

