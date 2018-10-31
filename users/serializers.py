from rest_framework import serializers
#import the custome user model using get_user_model
from django.contrib.auth import get_user_model
from .models import StudentProfile, CompanyProfile, Skill, OwnedSkills, Transcript, Education, Wh, Interest, SkillTest, Policy

#change the model and add user_type field
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        depth = 1
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email','user_type',
                  'is_superuser', 'is_staff')

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 1
        model = Skill
        fields = ('url', 'id', 'name', 'skill_type')

class TranscriptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Transcript
        fields = ('url','id','studentprofile','transcript_name','transcript')

class InterestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = Interest
        fields = ('url', 'id', 'inte_name')


#foreign Key serializer
class EducationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model  = Education
        fields = ('url', 'id', 'studentprofile', 'edu_name', 'qualification', 'institute', 'description')

class WhSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model   = Wh
        fields  = ('url', 'id', 'studentprofile', 'work_name', 'title', 'company_name','description')

class SkillTestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model   = SkillTest
        fields  = ('url', 'id', 'studentprofile', 'skill_name', 'score')


class StudentProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only = True)

    owned_skills = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Skill.objects.all(),
        view_name='skill-detail'
    )
    #transcript foreign key
    transcripts = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name='transcript-detail'
    )


    education = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name = 'education-detail'

    )

    work_history = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name='wh-detail'

    )

    skill_test = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name='skill-detail'

    )

    chosen_interests  = serializers.HyperlinkedRelatedField(
        many      = True,
        read_only = False,
        queryset  = Interest.objects.all(),
        view_name = 'interest-detail'

    )

    class Meta:
        model = StudentProfile
        depth = 1
        fields = ('url', 'id', 'user','location', 'about', 'phone', 'birthday', 'image', 'linked_in_website', 'twitter_website',
                  'facebook_website','owned_skills','chosen_interests','date_created','date_updated','education','work_history','transcripts','skill_test')

    def get_full_name(self, obj):
        request = self.context['request']
        return request.user.get_full_name()
        
        #deal with the nested object by update
    def update(self, instance, validated_data):
        # retrieve the User
        #user_data = validated_data.pop('user', None)
        #for attr, value in user_data.items():
            #setattr(instance.user, attr, value)

        # retrieve Profile
        for attr, value in validated_data.items():
            #put all choosen skills & interests to the list
            if str(attr) == 'owned_skills':
                instance.owned_skills.set(value)

            elif str(attr) == 'chosen_interests':
                instance.chosen_interests.set(value)

            else:
                setattr(instance, attr, value)

        #instance.user.save()
        instance.save()
        return instance


#create policy Serializer for the company
class PolicySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model  = Policy
        fields = ('url', 'id', 'companyprofile', 'policy_name', 'description')

#create the company profile Serializer
class CompanyProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only = True)

    policies = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name = 'policy-detail'

    )

    class Meta:
        model = CompanyProfile
        depth = 1
        fields = ('url', 'id', 'user','location', 'about', 'phone', 'tax', 'image', 'linked_in_website', 
                  'twitter_website','facebook_website','policies','date_created','date_updated','user')

