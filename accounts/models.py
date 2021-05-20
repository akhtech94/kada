from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("email is mandatory")

        if not password:
            raise ValueError("Password is mandatory")
        
        user = self.model( email = self.normalize_email(email) )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("email is mandatory.")
        
        if not password:
            raise ValueError("Password is mandatory.")

        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email               = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active           = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_shop             = models.BooleanField(default=False)
    is_delivery_person  = models.BooleanField(default=False)
    is_customer         = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        print(perm)
        if not self.is_admin:
            if perm == "accounts.view_customuser":
                return True
            else:
                return False
        return self.is_admin

    def has_module_perms(self, app_label):
        # print("app_label : {}".format(app_label))
        return True

    
