# Generated by Django 2.0.6 on 2018-07-03 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=100)),
                ('active', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pdescription', models.CharField(max_length=150)),
                ('pimg', models.CharField(max_length=100, null=True)),
                ('pquantity', models.FloatField()),
                ('pprice', models.FloatField()),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.CharField(max_length=50)),
                ('pcategoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='KB.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('purchaseprice', models.FloatField()),
                ('tax', models.FloatField()),
                ('Tcost', models.FloatField()),
                ('pquantity', models.FloatField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='KB.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('utype', models.CharField(max_length=10)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('active', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('userimg', models.ImageField(null=True, upload_to='')),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaseuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='KB.User_Detail'),
        ),
        migrations.AddField(
            model_name='product',
            name='user_detailid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='KB.User_Detail'),
        ),
    ]
