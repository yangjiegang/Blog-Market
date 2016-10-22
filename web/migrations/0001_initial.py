# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserType'
        db.create_table('web_usertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('web', ['UserType'])

        # Adding model 'Admin'
        db.create_table('web_admin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('user_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserType'])),
        ))
        db.send_create_signal('web', ['Admin'])

        # Adding model 'NewsType'
        db.create_table('web_newstype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('web', ['NewsType'])

        # Adding model 'News'
        db.create_table('web_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=500, default='')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('favor_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reply_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('news_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.NewsType'])),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Admin'])),
            ('create_data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['News'])

        # Adding model 'Reply'
        db.create_table('web_reply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Admin'])),
            ('new', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.News'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['Reply'])

        # Adding model 'Chat'
        db.create_table('web_chat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Admin'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['Chat'])


    def backwards(self, orm):
        # Deleting model 'UserType'
        db.delete_table('web_usertype')

        # Deleting model 'Admin'
        db.delete_table('web_admin')

        # Deleting model 'NewsType'
        db.delete_table('web_newstype')

        # Deleting model 'News'
        db.delete_table('web_news')

        # Deleting model 'Reply'
        db.delete_table('web_reply')

        # Deleting model 'Chat'
        db.delete_table('web_chat')


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
        'web.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500', 'default': "''"}),
            'create_data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favor_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.NewsType']"}),
            'reply_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
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