from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from dashboard.models import Tweets
from .serializers import TweetSerial

@api_view(['GET', 'POST']) #http methods that are allowed to access this view
def getRoutes(request):
    routes = [
        'GET /accruvia-api',
        'GET /accruvia-api/get-tweets/',

        'POST /accruvia-api/make-tweet/:name/:tweeText',
    ]
    return Response(routes)

# Gets all the tweets
@api_view(['GET'])
def get_tweets(request):
    tweets_data = Tweets.objects.all().order_by('-created')
    tweets_serializer = TweetSerial(tweets_data, many=True) #many = False when is one element
    return Response(tweets_serializer.data)

# creates tweets
@api_view(['POST'])
def make_tweet(request, name, tweeText):
    new_tweet = Tweets(fullName=name, tweetText=tweeText)
    new_tweet.save()
    tweets_serializer = TweetSerial(new_tweet, many=False) #many = False when is one element
    return Response(tweets_serializer.data)