from django.db import models
import uuid
# Create your models here.
class Objective(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    title = models.CharField(max_length=120)
    points = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    owner = models.UUIDField(editable=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']