# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u9879\u76ee\u540d\u79f0', max_length=255)),
                ('introduction', models.TextField(help_text='\u9879\u76ee\u7b80\u4ecb')),
                ('planned', models.BooleanField(help_text='\u662f\u5426\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee')),
                ('permit', models.BooleanField(verbose_name='\u662f\u5426\u6709\u7acb\u9879\u7533\u8bf7\uff08\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee\u4e0d\u9700\u8981\uff09')),
                ('permit_img', models.ImageField(help_text='\u9879\u76ee\u7acb\u9879\u7533\u8bf7\u626b\u63cf\u56fe\u7247', upload_to=b'')),
                ('approval_chart', models.BooleanField(help_text='\u7acb\u9879\u5355\u6d41\u7a0b\u662f\u5426\u5b8c\u6210')),
                ('approval_chart_img', models.ImageField(upload_to=b'', verbose_name='\u9879\u76ee\u7acb\u9879\u5355\u626b\u63cf\u56fe\u7247')),
                ('tendering_chart', models.BooleanField(help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u6d41\u7a0b\u662f\u5426\u5b8c\u6210')),
                ('tendering_agency_img', models.ImageField(help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u626b\u63cf\u56fe\u7247', upload_to=b'')),
                ('tendering_agency', models.CharField(help_text='\u9879\u76ee\u62db\u6807\u4ee3\u7406\u60c5\u51b5', max_length=255)),
                ('controlled_price', models.IntegerField(help_text='\u9879\u76ee\u62db\u6807\u63a7\u5236\u4ef7\uff08\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143\uff09')),
                ('successful_bidder', models.CharField(help_text='\u4e2d\u6807\u5355\u4f4d\u4fe1\u606f', max_length=255)),
                ('bid_price', models.FloatField(help_text='\u9879\u76ee\u4e2d\u6807\u4ef7\u683c\uff08\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143\uff09')),
                ('supervisor', models.CharField(help_text='\u9879\u76ee\u76d1\u7406\u5355\u4f4d\u4fe1\u606f', max_length=255)),
                ('audit', models.CharField(help_text='\u9879\u76ee\u5ba1\u8ba1\u5355\u4f4d\u4fe1\u606f', max_length=255)),
                ('contract', models.BooleanField(help_text='\u5408\u540c\u7b7e\u8ba2\u60c5\u51b5')),
                ('online_system_input', models.BooleanField(help_text='\u62db\u6295\u6807\u7ba1\u7406\u7cfb\u7edf\u5f55\u5165\u60c5\u51b5')),
                ('acceptance', models.BooleanField(help_text='\u5de5\u7a0b\u9a8c\u6536\u60c5\u51b5')),
                ('acceptance_img', models.ImageField(help_text='\u5de5\u7a0b\u9a8c\u6536\u5355\u56fe\u7247', upload_to=b'')),
                ('audit_price', models.IntegerField(help_text='\u5de5\u7a0b\u6700\u7ec8\u5ba1\u5b9a\u4ef7\u683c')),
            ],
        ),
    ]
