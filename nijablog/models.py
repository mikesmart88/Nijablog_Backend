from django.db import models
import os, datetime, random, string
from django.utils import timezone
from PIL import ImageDraw, Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.files.base import ContentFile
from django.core.files import File
import uuid
from django.contrib.auth.models import User
from .utils import Update_file

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name} --tag'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)


class ArticleFile(models.Model):
    FileType = [
        ('Video', 'Video'),
        ('Image', 'Image'),
        ('Iframe', 'Iframe'),
        ('other', 'Other')
    ]

    type = models.CharField(null=False, max_length=200, choices=FileType)
    file = models.FileField(null=False, unique=True)
    file_url = models.TextField(null=True, blank=True)
    file_uuid = models.UUIDField(null=True, unique=True, blank=True)

    def __str__(self):
        return 'post file'
    
    def save(self, *args, **kwargs):
        defult_uuid = uuid.uuid4()
        self.file_uuid = defult_uuid
        if self.file:
            new_path, newfile = Update_file(self.file, self.type, defult_uuid)
            self.file.save(new_path, newfile, save=False)
            self.file_url = new_path

        return super(ArticleFile, self).save(*args, **kwargs)
    

class Nationality(models.Model):
    name = models.CharField(max_length=1000, null=False, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Nationality, self).save(*args, **kwargs)

class Article(models.Model):

    ContentType = [
        ('Business', 'Business'),
        ('Entertainments', 'Entertainment'),
        ('Sport', 'Sport'),
        ('Education', 'Education'),
        ('Social', 'Social'),
        ('Programming', 'Programming'),
        ('Technology', 'Technology'),
        ('Tools', 'Tools'),
        ('Marketing', 'Marketing'),
        ('News', 'News'),
        ('Finance', 'Finance'),
        ('Health', 'Health'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Lifestyle', 'Lifestyle'),
        ('Music', 'Music'),
        ('Movies', 'Movies'),
        ('Science', 'Science'),
        ('Politics', 'Politics'),
        ('Environment', 'Environment'),
        ('Fashion', 'Fashion'),
        ('Gaming', 'Gaming'),
        ('Art', 'Art'),
        ('History', 'History'),
        ('Culture', 'Culture'),
        ('Religion', 'Religion'),
        ('Philosophy', 'Philosophy'),
        ('Psychology', 'Psychology'),
        ('Self-Help', 'Self-Help'),
        ('Relationships', 'Relationships'),
        ('Parenting', 'Parenting'),
        ('Pets', 'Pets'),
        ('Automotive', 'Automotive'),
        ('Real Estate', 'Real Estate'),
        ('Legal', 'Legal'),
        ('Human Resources', 'Human Resources'),
        ('Economics', 'Economics'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('Blockchain', 'Blockchain'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('Data Science', 'Data Science'),
    ]

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    cartegory = models.CharField(max_length=200, null=True, choices=ContentType)
    content = models.TextField(null=False)
    tags = models.ManyToManyField(Tag, related_name="PostTags")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='PostAuthor', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    post_uuid = models.UUIDField(null=True, unique=True, blank=True)
    post_file = models.ForeignKey(ArticleFile, null=False, related_name='Post_file', on_delete=models.PROTECT)
    region = models.ForeignKey(Nationality, related_name='Region', on_delete=models.CASCADE)
    reads = models.BigIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ---Published" if self.is_published == True else f"{self.title} ---Draft"
    
    def save(self, *args, **kwargs):
        if self.is_edited == False:
            self.post_uuid = uuid.uuid4()
            self.is_edited = True
        else:
            pass
        return super(Article, self).save(*args, **kwargs)
    
    
        

