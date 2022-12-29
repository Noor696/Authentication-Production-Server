from rest_framework import serializers
from .models import Novel

class NovelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Novel
        # fields=['name','auther', 'rate', 'price']
        fields='__all__'
