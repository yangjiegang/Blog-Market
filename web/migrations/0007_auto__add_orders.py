# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Orders'
        db.create_table('web_orders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('goods', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Goods'])),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Admin'], related_name='buyer')),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('reciever', self.gf('django.db.models.fields.CharField')(max_length=54, default='')),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=254, default='')),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=20, default=0)),
        ))
        db.send_create_signal('web', ['Orders'])


    def backwards(self, orm):
        # Deleting model 'Orders'
        db.delete_table('web_orders')


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
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'default': "''"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favor_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.NewsType']"}),
            'reply_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '400', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''"}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']"})
        },
        'web.newstype': {
            'Meta': {'object_name': 'NewsType'},
            'display': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'web.orders': {
            'Meta': {'object_name': 'Orders'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'default': "''"}),
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Admin']", 'related_name': "'buyer'"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'goods': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Goods']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'default': '0'}),
            'reciever': ('django.db.models.fields.CharField', [], {'max_length': '54', 'default': "''"})
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