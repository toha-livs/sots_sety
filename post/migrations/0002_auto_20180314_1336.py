# Generated by Django 2.0.3 on 2018-03-14 13:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=30)),
                ('login', models.TextField(max_length=30)),
                ('password', models.TextField(max_length=30)),
                ('birthday', models.DateField()),
                ('country', models.TextField(null=True)),
                ('city', models.TextField(null=True)),
                ('user_fk', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userall',
            name='email',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userall',
            name='login',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userall',
            name='password',
            field=models.TextField(max_length=30),
        ),
    ]
