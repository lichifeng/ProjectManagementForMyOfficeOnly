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
                ('name', models.CharField(max_length=255, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('introduction', models.TextField(verbose_name='\u9879\u76ee\u7b80\u4ecb', blank=True)),
                ('planned', models.BooleanField(default=True, help_text='\u662f\u5426\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee', verbose_name='\u8ba1\u5212\u5185\u9879\u76ee')),
                ('permit', models.BooleanField(default=False, help_text='\u662f\u5426\u6709\u7acb\u9879\u7533\u8bf7\uff08\u5e74\u5ea6\u8ba1\u5212\u5185\u9879\u76ee\u4e0d\u9700\u8981\uff09', verbose_name='\u7acb\u9879\u7533\u8bf7', choices=[(True, '\u5df2\u529e\u7406'), (False, '\u672a\u529e\u7406')])),
                ('permit_img', models.ImageField(help_text='\u9879\u76ee\u7acb\u9879\u7533\u8bf7\u626b\u63cf\u56fe\u7247', upload_to=b'', verbose_name='\u7acb\u9879\u7533\u8bf7', blank=True)),
                ('approval_chart', models.BooleanField(default=False, help_text='\u7acb\u9879\u5355\u529e\u7406\u60c5\u51b5', verbose_name='\u9879\u76ee\u7acb\u9879', choices=[(True, '\u5df2\u7acb\u9879'), (False, '\u529e\u7406\u4e2d')])),
                ('approval_chart_img', models.ImageField(help_text='\u9879\u76ee\u7acb\u9879\u5355\u626b\u63cf\u56fe\u7247', upload_to=b'', verbose_name='\u9879\u76ee\u7acb\u9879\u5355', blank=True)),
                ('tendering_chart', models.IntegerField(default=0, help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u529e\u7406\u60c5\u51b5', verbose_name='\u62db\u6807\u767b\u8bb0', choices=[(0, '\u529e\u7406\u4e2d'), (1, '\u5e02\u7ea7\u516c\u5f00'), (2, '\u9547\u7ea7\u516c\u5f00'), (3, '\u9080\u8bf7\u62db\u6807'), (4, '\u7ade\u4e89\u6027\u8c08\u5224'), (5, '\u8be2\u4ef7\u53d1\u5305'), (6, '\u76f4\u63a5\u53d1\u5305')])),
                ('tendering_agency_img', models.ImageField(help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u626b\u63cf\u56fe\u7247', upload_to=b'', verbose_name='\u62db\u6807\u767b\u8bb0\u8868', blank=True)),
                ('tendering_agency', models.CharField(help_text='\u9879\u76ee\u62db\u6807\u4ee3\u7406\u60c5\u51b5', max_length=255, verbose_name='\u62db\u6807\u4ee3\u7406', blank=True)),
                ('controlled_price', models.IntegerField(default=0, help_text='\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143', verbose_name='\u62db\u6807\u63a7\u5236\u4ef7', blank=True)),
                ('successful_bidder', models.CharField(help_text='\u5305\u62ec\u4e2d\u6807\u5355\u4f4d\u540d\u79f0\uff0c\u9879\u76ee\u8054\u7cfb\u4eba\u53ca\u8054\u7cfb\u65b9\u5f0f', max_length=255, verbose_name='\u4e2d\u6807\u5355\u4f4d', blank=True)),
                ('bid_price', models.IntegerField(default=0, help_text='\u7cbe\u786e\u5230\u6574\u6570\uff0c\u5355\u4f4d\u5143', verbose_name='\u4e2d\u6807\u4ef7\u683c', blank=True)),
                ('supervisor', models.CharField(help_text='\u5305\u62ec\u76d1\u7406\u5355\u4f4d\u540d\u79f0\uff0c\u9879\u76ee\u8054\u7cfb\u4eba\u53ca\u8054\u7cfb\u65b9\u5f0f', max_length=255, verbose_name='\u76d1\u7406\u5355\u4f4d', blank=True)),
                ('audit', models.CharField(help_text='\u5305\u62ec\u5ba1\u8ba1\u5355\u4f4d\u540d\u79f0\uff0c\u9879\u76ee\u8054\u7cfb\u4eba\u53ca\u8054\u7cfb\u65b9\u5f0f', max_length=255, verbose_name='\u5ba1\u8ba1\u5355\u4f4d', blank=True)),
                ('contract', models.BooleanField(default=False, verbose_name='\u5408\u540c\u7b7e\u8ba2', choices=[(True, '\u5df2\u7b7e\u8ba2'), (False, '\u672a\u7b7e\u8ba2')])),
                ('online_system_input', models.BooleanField(default=False, help_text='\u9547\u62db\u6295\u6807\u76d1\u7ba1\u7cfb\u7edf\u5f55\u5165\u60c5\u51b5', verbose_name='\u7cfb\u7edf\u5f55\u5165', choices=[(True, '\u5df2\u5f55\u5165'), (False, '\u672a\u5f55\u5165')])),
                ('acceptance', models.BooleanField(default=False, verbose_name='\u5de5\u7a0b\u9a8c\u6536', choices=[(True, '\u5df2\u9a8c\u6536'), (False, '\u672a\u9a8c\u6536')])),
                ('acceptance_img', models.ImageField(help_text='\u5de5\u7a0b\u9a8c\u6536\u5355\u626b\u63cf\u56fe\u7247', upload_to=b'', verbose_name='\u7ae3\u5de5\u9a8c\u6536\u5355', blank=True)),
                ('audit_price', models.IntegerField(default=0, help_text='\u5de5\u7a0b\u6700\u7ec8\u5ba1\u5b9a\u4ef7\u683c', verbose_name='\u5ba1\u5b9a\u4ef7\u683c', blank=True)),
                ('project_begin', models.DateField(verbose_name='\u5f00\u5de5\u65e5\u671f', blank=True)),
                ('project_finish', models.DateField(verbose_name='\u7ae3\u5de5\u65e5\u671f', blank=True)),
            ],
        ),
    ]
