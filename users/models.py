from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255,verbose_name = "用戶名稱")
	password = models.CharField(max_length = 255,verbose_name = "密碼")
	phone = models.CharField(max_length = 255,verbose_name = "電話")
	address = models.CharField(max_length = 255,verbose_name = "地址")
	created_time = models.DateTimeField(auto_now = True)
	modified_time = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "users"
