# Generated by Django 2.2.5 on 2019-09-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('street_name', models.CharField(max_length=64)),
                ('street_number', models.IntegerField()),
                ('apartment_number', models.IntegerField(blank=True)),
            ],
            options={
                'unique_together': {('city', 'street_name', 'street_number', 'apartment_number')},
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=64, unique=True)),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Address')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Email')),
                ('telephone', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Telephone')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('member', models.ManyToManyField(to='contacts.Person')),
            ],
        ),
    ]
