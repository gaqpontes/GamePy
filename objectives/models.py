from django.db import models

# Create your models here.
class Objective(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False);
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']