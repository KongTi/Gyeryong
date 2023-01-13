from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class MyAccountManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        if not nickname:
            raise ValueError("닉네임을 입력해주세요.")
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    # 관리자 User 생성
    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email,
            nickname = nickname,
            password = password
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user
 
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='이메일', max_length=32, unique=True)
    nickname = models.CharField(verbose_name='이름', max_length=8, unique=True)
    phone_num = models.CharField(verbose_name='전화번호', max_length=12, blank=True)

    update_at = models.DateTimeField(verbose_name='업데이트 날짜', auto_now_add=True)

    is_admin = models.BooleanField(verbose_name="관리자",default=False)
    is_active = models.BooleanField(verbose_name="활동",default=True)
 
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'accounts'
        verbose_name = '계정'
        verbose_name_plural = '계정'