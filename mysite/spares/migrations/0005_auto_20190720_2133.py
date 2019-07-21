# Generated by Django 2.2.3 on 2019-07-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spares', '0004_auto_20190720_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare',
            name='品牌',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='spare',
            name='图片',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='spare',
            name='用途',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='spare',
            name='设备名',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='spare',
            name='资产类型',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
