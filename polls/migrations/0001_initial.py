# Generated by Django 2.2.3 on 2019-07-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=254)),
                ('nome_usuario', models.CharField(max_length=240)),
                ('email_usuario', models.EmailField(max_length=254)),
            ],
        ),
    ]
