from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Check if a new profile picture is uploaded
        if self.pk and self.photo != 'profile_photos/default.png':
            try:
                # Get the old photo
                old_photo = UserProfile.objects.get(pk=self.pk).photo
                if old_photo and old_photo.name != 'profile_photos/default.png':
                    old_photo.delete(save=False)  # Delete the old photo
            except UserProfile.DoesNotExist:
                pass
        super().save(*args, **kwargs)

class cancelled(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    reason = models.TextField()
    date_cancelled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Cancelled Profile'