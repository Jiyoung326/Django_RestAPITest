from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User
#필터 작업
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

class UserQuerySet(ModelViewSet):
    queryset = User.objects.all() #전체 데이터 가져오기
    serializer_class = UserSerializer

    def get_queryset(self,query): #메소드 오버라이드
        queryset = super().get_queryset()
        queryset = queryset.filter(addr=query) #address가 query인 것만 필터링 하기.
        return queryset

class UserView(APIView):

    def get(self,request, **kwargs):
        if kwargs.get('u_id') is None:#u_id없으면 여러개 보여줌
            if request.GET.get('query') is None: #쿼리 없으면 전체 가져오기
                user_queryset = User.objects.all()
            else: #쿼리 있으면 필터링하기
                query = request.GET.get('query')
                user_queryset = UserQuerySet().get_queryset(query)

            user_all_serializer= UserSerializer(user_queryset,many=True)
            return Response({'count':User.objects.count(),
                    'users':user_all_serializer.data}, status=status.HTTP_200_OK)
        else:#u_id있으면 하나만 보여줌
            u_id = kwargs.get('u_id')
            user_one_serializer= UserSerializer(User.objects.get(id=u_id))#id는 테이블의 실제 속성 이름
            return Response(user_one_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'result':'success', 'data':user_serializer.data},
                            status=status.HTTP_201_CREATED)
        else: #notnull인 속성을 채우지 않았다거나 데이터가 맞지 않으면 
            return Response({'result':'fail', 'data':user_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        if kwargs.get('u_id') is None :
            return Response('u_id is required',status=status.HTTP_400_BAD_REQUEST)
        else: 
            u_id = kwargs.get('u_id')
            user_obj= User.objects.get(id=u_id)
            user_put_serializer = UserSerializer(user_obj,data=request.data) 
            if user_put_serializer.is_valid():
                user_put_serializer.save()
                return Response({
                    'result':'success',
                    'data': user_put_serializer.data}, status=status.HTTP_200_OK)
            else :
                return Response({
                    'result':'fail',
                    'data': user_put_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, **kwargs):
        if kwargs.get('u_id') is None:
            return Response('u_id is required',status=status.HTTP_400_BAD_REQUEST)

        else:
            u_id = kwargs.get('u_id')
            user_obj = User.objects.get(id=u_id)
            #원래면 user_obj이 None인 경우도 처리해야함
            user_obj.delete()
            return Response({'result':'success'},status=status.HTTP_200_OK)

    