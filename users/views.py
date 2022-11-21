from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from my_settings import KAKAO_CLIENT_ID, KAKAO_INFO_URI, KAKAO_REDIRECT, KAKAO_TOKEN_URI, GOOGLE_INFO_URI
import requests
from .tokens import TokenManager


class GoogleAuthView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            if 'access_token' in data:
                google_info_resp = requests.get(
                    GOOGLE_INFO_URI,
                    params={
                        'access_token': data['access_token']
                    }
                )
                if not google_info_resp.ok:
                    raise
                
                info = google_info_resp.json()
                user, _ = User.objects.get_or_create(
                    email = info['email'],
                    social_type = 'google',
                )
                nickname = user.nickname
                if nickname != info['name']:
                    user.nickname = info['name']
                    user.save()
                token = TokenManager.generate_token(user=user.id)
                result = {
                    'access_token': token, 
                    'nickname': info['name'],
                }
                if user.groups.filter(name='admin').exists():
                    result['isAdmin'] = True
                return Response(result)
            else:
                raise
            
        except Exception as e:
            return Response('Authorization failed {}'.format(e), status=403)
        
class KakaoAuthView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            if 'code' in data:
                access_token_resp = requests.post(
                    KAKAO_TOKEN_URI,
                    data = {
                        'grant_type': 'authorization_code',
                        'code': data['code'],
                        'client_id': 'd3401557af68a8a34ba8bb0c13b4bc77',
                        'redirect_uri': KAKAO_REDIRECT
                    }
                )
                if not access_token_resp.ok:
                    raise
                access_token = access_token_resp.json()['access_token']
                kakao_info_resp = requests.post(
                    KAKAO_INFO_URI,
                    headers = {
                        'Authorization': f'Bearer {access_token}'
                    }
                )
                if not kakao_info_resp.ok:
                    raise
                info = kakao_info_resp.json()
                properties= info['properties']
                user, _ = User.objects.get_or_create(
                    social_type = 'kakao',
                    email = f'kakao-{info["id"]}',
                )
                nickname = user.nickname
                if nickname != properties['nickname']:
                    user.nickname = properties['nickname']
                    user.save()
                token = TokenManager.generate_token(user=user.id)
                result = {
                    'access_token': token, 
                    'nickname': properties['nickname'],
                }
                if user.groups.filter(name='admin').exists():
                    result['isAdmin'] = True
                return Response(result)
            else:
                raise
            
        except Exception as e:
            return Response('Authorization failed {}'.format(e), status=403)