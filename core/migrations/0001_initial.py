# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'E1AutoAdv'
        db.create_table('core_e1autoadv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mark', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('probeg', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('valid_till', self.gf('django.db.models.fields.DateTimeField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('engine_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('privod', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('kpp', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rul', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('seller', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('images', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('adv_id', self.gf('django.db.models.fields.IntegerField')()),
            ('imported', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['E1AutoAdv'])


    def backwards(self, orm):
        
        # Deleting model 'E1AutoAdv'
        db.delete_table('core_e1autoadv')


    models = {
        'core.e1autoadv': {
            'Meta': {'object_name': 'E1AutoAdv'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'adv_id': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'engine_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kpp': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'privod': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'probeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rul': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_till': ('django.db.models.fields.DateTimeField', [], {}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']
