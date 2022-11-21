import django.db.models as models
from django.dispatch import receiver
import uuid


def get_uuid_name(instance, filename):
    split = filename.split('.')
    ext = split[-1]
    uuid_name = '{}.{}'.format(''.join(str(uuid.uuid4()).split('-')), ext)
    return uuid_name

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    img = models.FileField(null=True, upload_to=get_uuid_name)
    link = models.URLField(null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
@receiver(models.signals.post_delete, sender=Project)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.img.delete(save=False)
