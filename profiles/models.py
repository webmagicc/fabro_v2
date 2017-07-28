from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from fabro_v2.models import OrderingBaseModel, BaseModel
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
from django.utils.functional import cached_property


class CustomUserMaager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('User mast have email')

        email = self.normalize_email(email)

        user = self.model( email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username_validator = ''
    email = models.EmailField(_('Email'),
            unique=True,
            default='',
            help_text=_('Required'),
            error_messages={
            'unique': _("A user with that username already exists."),
            },)
    username = models.CharField(
            _('username'),
            max_length=255,
            blank=True,
            default=""
        )

    objects = CustomUserMaager()


    def get_fullname(self):
        if self.first_name or self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return self.email
