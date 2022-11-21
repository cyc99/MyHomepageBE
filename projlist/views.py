from rest_framework.views import APIView
from rest_framework.response import Response
from projlist.models import Project
from projlist.serializers import ProjectSerializer
from uuid import uuid4
from users.models import User
from users.tokens import TokenManager
from .models import Project

class ProjectBoardView(APIView):
    
    def get(self, request):
        try:
            objs = Project.objects.all()
            serializer = ProjectSerializer(objs, many=True)
            data = serializer.data
            return Response(data)
        except:
            return Response(status=404)

    def post(self, request):
        try:
            print(request.data)
            files = request.FILES
            data_dict = dict(request.POST)
            for key, value in data_dict.items():
                data_dict[key] = value[0]
            if 'img' in files:
                data_dict.update({'img': files['img']})
            serializer = ProjectSerializer(data=data_dict)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("SAVED")
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response(serializer.errors, status=400)
        
    def delete(self, request):
        try:
            data = request.data
            userid = TokenManager.decode(header=request.headers)
            user = User.objects.get(
                groups__name = 'admin',
                id = userid,
            )
            obj = Project.objects.get(id=data['id'])
            obj.delete()
            return Response(status=200)
        except Exception as e:
            return Response(status=400)