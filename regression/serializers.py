from rest_framework import serializers
from regression.models import UserStory



class UserStorySerializer(serializers.ModelSerializer):

	class Meta:
		model = UserStory
		fields = ('subject', 'case_title') #for all use '__all__'
