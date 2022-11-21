from datetime import datetime

from rest_framework import serializers
from webapp.apps.skurge.serializers.common import SerializedDateTimeField
from webapp.apps.skurge.models import SourceEvent


class SourceEventSerializer(serializers.ModelSerializer):

    created_at = SerializedDateTimeField(default=datetime.strptime("9999-12-31 00:00:00", "%Y-%m-%d %H:%M:%S"))
    modified_at = SerializedDateTimeField(default=datetime.strptime("9999-12-31 00:00:00", "%Y-%m-%d %H:%M:%S"))

    class Meta:
        model = SourceEvent
        exclude = ['is_deleted']
