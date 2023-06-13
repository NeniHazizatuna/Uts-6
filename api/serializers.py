from rest_framework import serializers
from . models import mahasiswaModels
class mahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mahasiswaModels
        fields = ['Nim', 'Nama', 'Alamat']
 