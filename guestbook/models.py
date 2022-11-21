import django.db.models as models

class GuestBook(models.Model):
    gid = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=200)
    password = models.TextField(null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)