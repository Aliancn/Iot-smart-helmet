from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Msg(models.Model):
    id = models.AutoField(primary_key=True)
    describe = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(default='')
    detaail_html = models.CharField(default='')

    def __str__(self):
        return self.describe


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Status(models.TextChoices):
        ACTIVE = '在岗'
        INACTIVE = '休息'
        PENDING = '请假'
        OTHER = '其他'
    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    # 位置
    location = models.CharField(max_length=100)
    # 工作时间
    start_work_time = models.DateTimeField(auto_now_add=True)
    end_work_time = models.DateTimeField(auto_now_add=True)
    # 是否佩戴头盔
    helmet_wared = models.BooleanField(default=True)
    # 工作状态
    is_working = models.BooleanField(default=False)

    # 佩戴头盔记录
    helmet_wared_array = ArrayField(models.BooleanField(), default=list)
    # 到岗记录
    arrive_array = ArrayField(models.BooleanField(), default=list)

    # profile
    # phone
    phone = models.CharField(max_length=100)
    # email
    email = models.EmailField(max_length=100)
    # address
    address = models.CharField(max_length=100)
    # age
    age = models.IntegerField()
    # gender
    gender = models.CharField(max_length=100)
    # emergency_contact
    emergency_contact = models.CharField(max_length=100)
    # department_id
    department_id = models.IntegerField()
    # position_id
    position_id = models.IntegerField()

    def __str__(self):
        return self.name
