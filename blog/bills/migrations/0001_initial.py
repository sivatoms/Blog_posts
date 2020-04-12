# Generated by Django 3.0.1 on 2020-04-09 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, verbose_name='Group name')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.ManyToManyField(to='bills.Group')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(max_length=200, verbose_name='Bill type')),
                ('purchase_date', models.DateField(auto_now=True)),
                ('share_with', models.CharField(max_length=250, verbose_name='Share among')),
                ('amount', models.FloatField(default=0)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.GroupMembers')),
                ('added_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(default='Grocery type', max_length=50, verbose_name='Bill type')),
                ('paid_by', models.CharField(blank=True, max_length=150, null=True)),
                ('paid_amount', models.FloatField(blank=True, default=0, null=True, verbose_name='You Spent')),
                ('due_amount', models.FloatField(blank=True, default=0, null=True, verbose_name='You Owe')),
                ('shared_with', models.CharField(max_length=250, verbose_name='Shared With')),
                ('purchase_date', models.DateField(auto_now=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Transactions')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]