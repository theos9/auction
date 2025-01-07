from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html

class AboutUsModel(models.Model):
    title= models.CharField(max_length=150,verbose_name='title',blank=True,null=True)
    message=models.TextField(verbose_name='message',blank=True,null=True)
    image=models.ImageField(upload_to='data/about-us',verbose_name='image',blank=True,null=True)
    link=models.CharField(max_length=500,verbose_name='link',blank=True,null=True)
    address=models.CharField(max_length=300,verbose_name='address',blank=True,null=True)
    coordinates=models.CharField(max_length=100,verbose_name='coordinates',blank=True,null=True)
    additional_text=models.TextField(verbose_name='additional text',blank=True,null=True)

    def image_tag(self):
            if self.image:
                return format_html(f'<img src="{self.image.url}" width="100" height="100" />')
            return 'No image available'
    image_tag.short_description = "preview"

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='about us'
        verbose_name_plural='about us page'
        