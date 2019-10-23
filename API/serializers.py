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

class ProblemSetSerializers(serializers.ModuleSerializer):
    class Meta:
        model = ProblemSet
        exclude=[]
        read_only_fields = []
        depth = 1

class ProblemSerializers(serializers.ModuleSerializer):
    class Meta:
        model = Problem
        exclude=[]
        read_only_fields = []
        depth = 1