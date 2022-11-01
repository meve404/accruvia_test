from rest_framework.serializers import ModelSerializer
from dashboard.models import Tweets

class TweetSerial(ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'