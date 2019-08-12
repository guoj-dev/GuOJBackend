from django.db import models

# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=256);
    Avatar=models.URLField()
    Coins=models.BigIntegerField()
    Nameplate=models.CharField(max_length=16)
    NameColor=models.CharField(max_length=16)
    NameplateColor=models.CharField(max_length=16)
    UserRegisterDate=models.DateField()
    Contributing=models.FloatField()
    CompileErrorCount=models.BigIntegerField()
    AcceptedCount=models.BigIntegerField()
    WrongAnswerCount=models.BigIntegerField()
    RuntimeErrorCount=models.BigIntegerField()
    TimeLimitExceededCount=models.BigIntegerField()
    MemoryLimitExceededCount=models.BigIntegerField()
    OutputLimitExceededCount=models.BigIntegerField()
    ParticallyCorrectCount=models.BigIntegerField()
    SystemErrorCount=models.BigIntegerField()
    Text=models.TextField()
    def __str__(self):
        return self.Username

class Group(models.Model):
    LEVEL_CHOICE={
        ('N','Normal'),('T','Trusted'),('A','Admin')
    }
    GroupName=models.TextField()
    UserCount=models.BigIntegerField()
    Level=models.CharField(max_length=16,choices=LEVEL_CHOICE)
    AllowJoin=models.NullBooleanField()
    def __str__(self):
        return self.GroupName

class ProblemSet(models.Model):
    PERMISSION_CHOICE={
        ('S','Stricted'),('SP','Private'),('P','Public')
    }
    ProblemSetName=models.TextField()
    Group=models.ManyToManyField(Group)
    Permission=models.CharField(max_length=16,choices=PERMISSION_CHOICE)
    AuthedUser=models.ManyToManyField(User)
    def __str__(self):
        return self.ProblemSetName

class Problem(models.Model):
    ProblemSet=models.ForeignKey(ProblemSet,blank=True, null=True,on_delete=models.SET_NULL)
    LocalProblemID=models.BigIntegerField()
    ProblemProviderUser=models.ForeignKey(User,blank=True, null=True,on_delete=models.SET_NULL)
    ProblemProviderGroup=models.ForeignKey(Group,blank=True, null=True,on_delete=models.SET_NULL)
    ProblemProvider_overwrite=models.TextField()#This will Overwrite the Provider!
    #TODO:ProblemLevel
    ProblemTitle=models.TextField()
    ProblemDiscription=models.TextField()
    def __str__(self):
        return self.ProblemTitle


class JudgeData(models.Model):
    CompileError='CE'
    Accepted='AC'
    WrongAnswer='WA'
    RuntimeERROR='RE'# Please do not use 'RuntimeError' as a name
    TimeLimitExceeded='TLE'
    MemoryLimitExceeded='MLE'
    OutputLimitExceeded='OLE'
    ParticallyCorrect='PC'
    SystemError='SE'
    STATUS_CHOICES={
        (CompileError,'CompileError'),
        (Accepted,'Accepted'),
        (WrongAnswer,"WrongAnswer"),
        (RuntimeERROR,'RuntimeError'),
        (TimeLimitExceeded,"TimeLimitExceeded"),
        (MemoryLimitExceeded,'MemoryLimitExceeded'),
        (OutputLimitExceeded,'OutputLimitExceeded'),
        (ParticallyCorrect,'ParticallyCorrect'),
        (SystemError,'SystemError')
    }
    JudgeStatus=models.CharField(max_length=64,choices=STATUS_CHOICES)
    Score=models.FloatField()
    LocalID=models.BigIntegerField()
    ProblemSetID=models.BigIntegerField()
    ProblemID=models.BigIntegerField()
    User=models.ForeignKey(User,blank=True, null=True,on_delete=models.SET_NULL)
    isPublic=models.BooleanField()
