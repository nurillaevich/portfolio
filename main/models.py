from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    friends = models.CharField(max_length=212)
    image = models.ImageField('author', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    column_7 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Friends(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField('friends', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Pricing(models.Model):
    name = models.CharField(max_length=212)
    price = models.CharField(max_length=212)
    image = models.ImageField(upload_to='pricing', null=True, blank=True)
    photo_count = models.PositiveIntegerField(default=0)
    process = models.CharField(max_length=212)
    camera_type = models.CharField(max_length=212)
    resolution = models.CharField(max_length=212)
    term = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
