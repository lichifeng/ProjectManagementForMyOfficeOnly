# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='acceptance_img',
            field=models.ImageField(help_text='\u5de5\u7a0b\u9a8c\u6536\u5355\u56fe\u7247', upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='approval_chart_img',
            field=models.ImageField(help_text='\u9879\u76ee\u7acb\u9879\u5355\u626b\u63cf\u56fe\u7247', upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='permit_img',
            field=models.ImageField(help_text='\u9879\u76ee\u7acb\u9879\u7533\u8bf7\u626b\u63cf\u56fe\u7247', upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tendering_agency_img',
            field=models.ImageField(help_text='\u62db\u6295\u6807\u767b\u8bb0\u8868\u626b\u63cf\u56fe\u7247', upload_to=b'', blank=True),
        ),
    ]
