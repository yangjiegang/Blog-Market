# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.content'
        db.alter_column('web_news', 'content', self.gf('django.db.models.fields.TextField')(max_length=1000))

        # Changing field 'News.summary'
        db.alter_column('web_news', 'summary', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'News.url'
        db.alter_column('web_news', 'url', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'News.content'
        db.alter_column('web_news', 'content', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'News.summary'
        db.alter_column('web_news', 'summary', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'News.url'
        db.alter_column('web_news', 'url', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        'web.admin': {
            'Meta': {'object_name': 'Admin'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.UserType']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'web.chat': {
            'Meta': {'object_name': 'Chat'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']"})
        },
        'web.goods': {
            'Meta': {'object_name': 'Goods'},
            'descript': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'goodsImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'web.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favor_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.NewsType']"}),
            'reply_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']"})
        },
        'web.newstype': {
            'Meta': {'object_name': 'NewsType'},
            'display': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'web.reply': {
            'Meta': {'object_name': 'Reply'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.News']"}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']"})
        },
        'web.usertype': {
            'Meta': {'object_name': 'UserType'},
            'display': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['web']