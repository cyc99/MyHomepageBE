### 직접 작성하고 수정한 파일만 기재합니다.
# models.py
프로젝트 모델이 정의되어 있는 파일입니다.

S3에 이미지 파일을 저장할 때 파일 이름을 임의로 바꾸도록 만드는 함수와 

데이터가 삭제될 때 등록된 이미지를 S3에서 삭제하는 함수도 정의되어 있습니다.
# serializers.py
프로젝트 모델에서 데이터를 가져오거나 저장하는 데 사용하는 Serializer가 정의되어 있는 파일입니다.

Serializer의 create 함수에서 \n를 제대로 저장할 수 있도록 \n을 \\\n로 변환하는 과정을 진행합니다.
# urls.py
프로젝트 APIView의 엔드포인트가 정의되어 있는 파일입니다.
# views.py
프로젝트 APIView가 정의되어 있는 파일입니다.

GET, POST, DELETE 메소드에 대해 정의되있습니다.

POST의 경우 다른 API와 다르게 form-data를 처리하는 과정이 있습니다.

POST, DELETE의 경우 어드민 유저만 사용할 수 있게 유저가 속한 그룹에 어드민이 있는지 확인하는 과정이 있습니다.