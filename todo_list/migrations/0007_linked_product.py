# Generated by Django 3.0.5 on 2020-06-14 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20200615_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('belongs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_list.Userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Linked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.Userinfo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.Product')),
            ],
        ),
    ]
