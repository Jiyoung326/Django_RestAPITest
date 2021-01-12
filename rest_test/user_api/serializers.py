from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = '__all__' #필요한 것만 보려면 튜플로 나열하면 됨 ('id','address'...,'tel')