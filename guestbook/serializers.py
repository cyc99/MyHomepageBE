from rest_framework import serializers
from .models import GuestBook
import bcrypt

class GuestBookInfoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type')
    nickname = serializers.ReadOnlyField(source='author.nickname')
    
    class Meta:
        model = GuestBook
        fields = ('nickname', 'type', 'gid', 'content', 'created_at')
        
    def get_type(self, obj):
        author = obj.author
        return 1 if author else 0 
    
class GuestBookManageSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()
        
    class Meta:
        model = GuestBook
        fields = '__all__'
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['content'] = '\\n'.join(validated_data['content'].split('\n'))
        if validated_data['type'] == 0:
            pw = validated_data['password'].encode('utf-8')
            if len(pw) < 8:
                raise
            pw_crypt = bcrypt.hashpw(pw, bcrypt.gensalt())
            pw_crypt = pw_crypt.decode('utf-8')
            validated_data['password'] = pw_crypt
        if type == 1 and not validated_data['author']:
                raise
        elif type == 0 and validated_data['author']:
            raise
        validated_data.pop('type')
        return validated_data