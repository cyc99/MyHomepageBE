### 직접 작성하고 수정한 파일만 기재합니다.
# models.py
방명록 모델이 정의되어 있는 파일입니다.

익명 방명록과 유저가 작성한 방명록을 구분하기 위해 null이 허용된 User를 foreign key로 사용하는 필드가 있습니다.
# serializers.py
방명록 데이터를 가져오는 Serializer와 저장을 위한 Serializer가 정의되어 있는 파일입니다.

Serializer가 따로 존재하는 이유는 요청에 대한 응답을 전달할 때 DB에 포함되지 않은 정보도 같이 보내기때문에 

하나의 Serializer로 데이터를 저장할 수 없기 때문입니다.

저장을 담당하는 GuestBookManageSerializer에는 유효성 검사를 진행할 때 type의 검증, 비밀번호 암호화를 하는 과정이 포함되어있습니다. 
# urls.py
방명록 APIView의 엔드포인트가 정의되어 있는 파일입니다.
# views.py
프로젝트 APIView가 정의되어 있는 파일입니다.

GET, POST, DELETE 메소드에 대해 정의되있습니다.

DELETE의 경우 해당 방명록이 익명 타입이면 bcrypt를 이용해 패스워드를 비교합니다.
