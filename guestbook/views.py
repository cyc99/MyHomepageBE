from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GuestBook
from .serializers import GuestBookInfoSerializer, GuestBookManageSerializer
import bcrypt
from users.tokens import TokenManager

class GuestBookView(APIView):
    
    def get(self, request):
        id = request.query_params.get('id')
        qs = GuestBook.objects.filter(user=id).order_by('-gid') if id else GuestBook.objects.all().order_by('-gid')
        serializer = GuestBookInfoSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            data = request.data
            
            if data['type'] == 0:
                data.update({
                    'author': None,
                })
                
            else:
                author = TokenManager.decode(header = request.headers)
                if author:
                    data.update({
                        'author': author,
                        'password': None,
                    })
                else:
                    raise
            serializer = GuestBookManageSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('')
        except Exception as e:
            print(e)
            return Response('failed', status=400)
        
    def delete(self, request):
        try:
            data = request.data
            obj = GuestBook.objects.get(gid=data['gid'])
            if obj.author:
                if TokenManager.authenticate(obj.author.id, header=request.headers):
                    obj.delete()
                    return Response('deleted', status=200)
                raise
            else:
                if bcrypt.checkpw(data['password'].encode('utf-8'), obj.password.encode('utf-8')):
                    obj.delete()
                    return Response('deleted', status=200)
                raise
            
        except Exception as e:
            return Response('failed', status=400)