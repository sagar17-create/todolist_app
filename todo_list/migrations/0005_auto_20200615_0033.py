# Generated by Django 3.0.5 on 2020-06-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_house_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('house', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('interest', models.CharField(choices=[('gaming', 'gaming'), ('dancing', 'dancing'), ('singing', 'singing')], max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='textbox',
            name='house',
        ),
        migrations.RemoveField(
            model_name='textbox',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='textbox',
            name='phone',
        ),
    ]
