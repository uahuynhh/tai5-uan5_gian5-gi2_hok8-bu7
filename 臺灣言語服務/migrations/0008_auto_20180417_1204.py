# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
import 臺灣言語服務.models檢查


class Migration(migrations.Migration):

    dependencies = [
        ('臺灣言語服務', '0007_auto_20171221_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kaldi語料辨識',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('臺灣言語服務.kaldi辨識結果',),
        ),
        migrations.AddField(
            model_name='kaldi對齊結果',
            name='語言',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='kaldi辨識結果',
            name='語言',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kaldi對齊結果',
            name='切好的聽拍',
            field=jsonfield.fields.JSONField(blank=True, null=True, validators=[臺灣言語服務.models檢查.檢查聽拍內底欄位敢有夠]),
        ),
        migrations.AlterField(
            model_name='kaldi對齊結果',
            name='影音',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='kaldi對齊結果',
            name='欲切開的聽拍',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kaldi辨識結果',
            name='影音',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
