# Generated by Django 4.1.7 on 2023-03-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('emailid', models.CharField(default='', max_length=150)),
                ('password', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(default='', max_length=100)),
                ('subcategory_id', models.CharField(default='', max_length=100)),
                ('model_year', models.CharField(default='', max_length=170)),
                ('variant', models.CharField(default='', max_length=170)),
                ('price', models.CharField(default='', max_length=170)),
                ('insured', models.CharField(default='', max_length=70)),
                ('registration_no', models.CharField(default='', max_length=170)),
                ('owner_name', models.CharField(default='', max_length=170)),
                ('mobile_no', models.CharField(default='', max_length=170)),
                ('color', models.CharField(default='', max_length=170)),
                ('fuel_type', models.CharField(default='', max_length=170)),
                ('no_of_seats', models.CharField(default='', max_length=170)),
                ('transmission_type', models.CharField(default='', max_length=170)),
                ('icon', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='categoryid',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='subcategoryname',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_id',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='company_name',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='subcategory_name',
            field=models.CharField(default='', max_length=70),
        ),
    ]
