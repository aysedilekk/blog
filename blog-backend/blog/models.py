from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.JSONField()
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=20)
    company = models.JSONField()
    profile_image = models.BinaryField(blank=True, null=True)


class Post(models.Model):
    class Meta:
        db_table = "post"

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()


class Comment(models.Model):
    class Meta:
        db_table = "comment"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()


class Album(models.Model):
    class Meta:
        db_table = "album"

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)


class Photo(models.Model):
    class Meta:
        db_table = "photo"

    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    thumbnailUrl = models.CharField(max_length=255)


class Todo(models.Model):
    class Meta:
        db_table = "todo"

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
