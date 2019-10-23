from Databases.models import Problem
from rest_framework import serializers
from django.contrib.auth import get_user_model
from Databases.models import Problem,ProblemSet
User = get_user_model()


class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=['password','user_permissions','groups','last_login','first_name','last_name','is_staff','date_joined']
        read_only_fields = ['id','username','is_superuser','is_active','Coins','Rating','Experience','Nameplate','NameColor','NameplateColor','UserRegisterDate','Contribution','CompileErrorCount','AcceptedCount','WrongAnswerCount','RuntimeErrorCount','TimeLimitExceededCount','MemoryLimitExceededCount','OutputLimitExceededCount','ParticallyCorrectCount','SystemErrorCount','email']
        depths = 1

# TODO: Finish Problem Serializers
class ProblemSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemSet
        exclude=['AuthedUser','Group']
        read_only_fields = []
        depth = 1

class ProblemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude=["ProblemProvider_overwrite","ProblemProviderUser","ProblemSet","ProblemDataPath","ProblemProviderGroup"]
        read_only_fields = []
        depth = 1