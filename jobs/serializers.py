from rest_framework import serializers
from rest_framework.exceptions import ParseError

from .models import Company,Category,Job,Applicant
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

# tag serializer




class CompanySerializer(serializers.HyperlinkedModelSerializer):

#foreign key
    job = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name = 'job-detail'

    )

    class Meta:

        model = Company
        fields = ('url','id','name','added_by','telephone','fax','address','date_add','job')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Category
        fields = ('url', 'id', 'cate_name' )

# serialize the tag, gain control over the serialization


class JobSerializer(TaggitSerializer,serializers.HyperlinkedModelSerializer):

    #foreign key
    category = serializers.SlugRelatedField(

        many=True,
        #read_only=True,
        queryset = Category.objects.all(),
        #view_name = 'category-detail'
        slug_field = 'cate_name'

    )


    # tag serializer
    tags = TagListSerializerField()

    class Meta:
        model = Job
        fields = ('url','id','status','company','title','description','tags','location','category','start_date',
                  'due_date','date_add', 'date_updated')


    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(JobSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        """
        #writable nested serializer on category
        category_data = validated_data.pop('category')
        instance = Job.object.create(**validated_data)
        for cate in category_data:
            Category.objects.create(instance=instance, **category_data)
        """
        return instance


    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start_date'] != None and data['due_date']!=None:
            if data['start_date'] > data['due_date']:
                raise serializers.ValidationError("finish must occur after start")
        return data


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Applicant
        fields = ('url', 'id', 'user', 'job','status','date_applied' )


