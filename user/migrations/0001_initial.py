# Generated by Django 5.0.2 on 2024-12-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'رمز یکبار مصرف',
                'verbose_name_plural': 'رمز یکبار مصرف',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره تماس')),
                ('name', models.CharField(max_length=20, verbose_name='نام')),
                ('family', models.CharField(max_length=20, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('national_id', models.CharField(max_length=10, unique=True, verbose_name='کد ملی')),
                ('card_number', models.CharField(max_length=16, verbose_name='شماره کارت')),
                ('address', models.CharField(max_length=255, verbose_name='ادرس')),
                ('is_active', models.BooleanField(default=1, verbose_name='فعال/غیر فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
    ]
