from Databases.models import Problem
from rest_framework import serializers
from django.contrib.auth import get_user_model
from Databases.models import Problem,ProblemSet,Notice
from dj_rest_auth.serializers import PasswordResetSerializer, PasswordResetConfirmSerializer
from allauth.account.forms import ResetPasswordForm, ResetPasswordKeyForm
User = get_user_model()


class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=['password','user_permissions','groups','last_login','first_name','last_name','is_staff','date_joined',]
        read_only_fields = ['id','username','is_superuser','is_active','Coins','Rating','Experience','Nameplate','NameColor','NameplateColor','UserRegisterDate','Contribution','CompileErrorCount','AcceptedCount','WrongAnswerCount','RuntimeErrorCount','TimeLimitExceededCount','MemoryLimitExceededCount','OutputLimitExceededCount','ParticallyCorrectCount','SystemErrorCount','email','CreatedProblemSetCount','CreatedProblemCount']
        depths = 1

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','Avatar']
        read_only_fields=['id','username','Avatar']

class ProblemSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemSet
        exclude=['Group']
        read_only_fields = ('owner',)

class ProblemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude=[]
        read_only_fields = ["ProblemSet","ProblemProvider_overwrite","ProblemProviderUser","ProblemProviderGroup"]

class NoticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notice
        exclude=[]
        read_only_fields = ['Title','Color','Background','Type']

    