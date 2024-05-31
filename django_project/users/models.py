from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Call the original save method to save the image
        super().save(*args, **kwargs)

        # Open the image using Pillow
        img = Image.open(self.image)

        # Resize the image if needed
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            # Save the resized image to a BytesIO object
            img_io = BytesIO()
            img.save(img_io, format='JPEG')

            # Use InMemoryUploadedFile to save the resized image
            img_file = InMemoryUploadedFile(
                img_io,
                None,
                self.image.name,
                'image/jpeg',
                sys.getsizeof(img_io),
                None
            )
            # Save the image back to the model
            self.image.save(self.image.name, img_file, save=False)

        # Save the model with the new image
        super().save(*args, **kwargs)
