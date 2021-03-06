# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'E1AutoAdv.year'
        db.alter_column('core_e1autoadv', 'year', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'E1AutoAdv.price'
        db.alter_column('core_e1autoadv', 'price', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'E1AutoAdv.probeg'
        db.alter_column('core_e1autoadv', 'probeg', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'E1AutoAdv.volume'
        db.alter_column('core_e1autoadv', 'volume', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))


    def backwards(self, orm):
        
        # Changing field 'E1AutoAdv.year'
        db.alter_column('core_e1autoadv', 'year', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'E1AutoAdv.price'
        db.alter_column('core_e1autoadv', 'price', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'E1AutoAdv.probeg'
        db.alter_column('core_e1autoadv', 'probeg', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'E1AutoAdv.volume'
        db.alter_column('core_e1autoadv', 'volume', self.gf('django.db.models.fields.FloatField')(null=True))


    models = {
        'core.e1autoadv': {
            'Meta': {'object_name': 'E1AutoAdv'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'adv_id': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'engine_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kpp': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'privod': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'probeg': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'rul': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_till': ('django.db.models.fields.DateTimeField', [], {}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['core']
