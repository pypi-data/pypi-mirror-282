from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    USER_TYPE = [
        ('Author', 'Author'),
        ('Public', 'Public')
    ]

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_type = models.CharField(
        max_length=255, blank=True, choices=USER_TYPE, default='Public')
    phone_number = models.CharField(null=True, blank=True, max_length=11, validators=[
                                    RegexValidator(r'^\d{11}$', 'Enter a valid phone number.')])
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    gender = models.CharField(
        max_length=255, null=True, blank=True, choices=GENDER)
    home_address = models.TextField(null=True, blank=True)
    local_govt = models.CharField(max_length=255, null=True, blank=True)
    state_of_origin = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    ordering = ('email',)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_image_url(self):
        return (f"https://res.cloudinary.com/dkcjpdk1c/image/upload/{self.image}")

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "https://cdn-icons-png.flaticon.com/512/147/147142.png"

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Keyword(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='post_author', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='post_category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post_tag')
    keywords = models.ManyToManyField(Keyword, related_name='post_keyword')
    slug = models.SlugField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_user',
                             on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post} at {self.created_at}"


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user} on {self.content_object} at {self.created_at}"
