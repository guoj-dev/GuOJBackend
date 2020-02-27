from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser  
from django.db import models
import json

# Create your models here.


class User(AbstractUser):
    Sexs = [('M','Male'), ('W','Female')]
    Sex = models.CharField(max_length=16, choices=Sexs)
    Avatar = models.URLField()
    Coins = models.BigIntegerField(default=0)
    Rating = models.BigIntegerField(default=1500)
    Experience = models.BigIntegerField(default=0)
    Nameplate = models.CharField(max_length=16,blank=True)
    NameColor = models.CharField(max_length=16,default='Blue')
    NameplateColor = models.CharField(max_length=16,blank=True)
    UserRegisterDate = models.DateTimeField(auto_now_add=True)
    Contribution = models.FloatField(default=0)
    CompileErrorCount = models.BigIntegerField(default=0)
    AcceptedCount = models.BigIntegerField(default=0)
    WrongAnswerCount = models.BigIntegerField(default=0)
    RuntimeErrorCount = models.BigIntegerField(default=0)
    TimeLimitExceededCount = models.BigIntegerField(default=0)
    MemoryLimitExceededCount = models.BigIntegerField(default=0)
    OutputLimitExceededCount = models.BigIntegerField(default=0)
    ParticallyCorrectCount = models.BigIntegerField(default=0)
    SystemErrorCount = models.BigIntegerField(default=0)
    Text = models.TextField(blank=True)
    CreatedProblemSetCount = models.BigIntegerField(default=0)
    CreatedProblemCount = models.BigIntegerField(default=0)
    class Meta:
      verbose_name = '用户' 
      verbose_name_plural = verbose_name 
      ordering = ['-id']




class Group(models.Model):
    LEVEL_CHOICE = {
        ('N', 'Normal'), ('T', 'Trusted'), ('A', 'Admin')
    }
    GroupName = models.TextField()
    UserCount = models.BigIntegerField()
    Level = models.CharField(max_length=16, choices=LEVEL_CHOICE)
    AllowJoin = models.NullBooleanField()
    isOfficial = models.BooleanField()
    Admins = models.ManyToManyField(
        User, blank=True, null=True, related_name='admins')
    Users = models.ManyToManyField(
        User, blank=True, null=True, related_name='users')
    def __str__(self):
        return self.GroupName


    class Meta:
      verbose_name = '用户组' 
      verbose_name_plural = verbose_name 
      ordering = ['-id']


class ProblemSet(models.Model):
    PERMISSION_CHOICE = {
        ('S', 'Stricted'), ('SP', 'Private'), ('P', 'Public')
    }
    ProblemSetName = models.TextField()
    ProblemSetPrefix = models.TextField()
    Group = models.ManyToManyField(Group, related_name='ProblemSet')
    Permission = models.CharField(max_length=16, choices=PERMISSION_CHOICE)
    AuthedUser = models.ManyToManyField(User)

    def __str__(self):
        return self.ProblemSetName


    class Meta:
      verbose_name = '题库' 
      verbose_name_plural = verbose_name 
      ordering = ['-id']


class Problem(models.Model):
    ProblemSet = models.ForeignKey(
        ProblemSet, blank=True, null=True, on_delete=models.SET_NULL)
    LocalProblemID = models.BigIntegerField()
    ProblemProviderUser = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    ProblemProviderGroup = models.ForeignKey(
        Group, blank=True, null=True, on_delete=models.SET_NULL, related_name='Problem')
    # This will Overwrite the Provider!
    ProblemProvider_overwrite = models.TextField()
    ProblemLevel=models.FloatField(default=0)
    ProblemLevel_overwrite=models.FloatField(default=0)
    ProblemTitle = models.TextField()
    ProblemDescription = models.TextField()
    ProblemDataPath = models.TextField()

    def __str__(self):
        return self.ProblemTitle
    

    class Meta:
      verbose_name = '题目' 
      verbose_name_plural = verbose_name 
      ordering = ['-id']


class Contest(models.Model):
    ProviderUser = models.ManyToManyField(User)
    ProviderGroup = models.ForeignKey(
        Group, blank=True, null=True, on_delete=models.SET_NULL, related_name='Contest')
    Title = models.TextField()
    Description = models.TextField()
    isPublic = models.BooleanField()
    isGlobal = models.BooleanField()
    isRated = models.BooleanField()
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    ProblemSet = models.ManyToManyField(ProblemSet)
    Problem = models.ManyToManyField(Problem)
    ContestRules = JSONField()
    class Meta:
      verbose_name = '比赛' 
      verbose_name_plural = verbose_name 
      ordering = ['-id']


class ContestSolutions(models.Model):
    ProviderUser = models.ManyToManyField(User)
    ProviderGroup = models.ForeignKey(
        Group, blank=True, null=True, on_delete=models.SET_NULL, related_name='ContestSolutions')
    Title = models.TextField()
    Text = models.TextField()
    ReleaseTime = models.DateTimeField()


class Discussion(models.Model):
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    ProblemSet = models.ForeignKey(
        ProblemSet, blank=True, null=True, on_delete=models.SET_NULL)
    Problem = models.ForeignKey(
        Problem, blank=True, null=True, on_delete=models.SET_NULL)
    Contest = models.ForeignKey(
        Contest, blank=True, null=True, on_delete=models.SET_NULL)
    Title = models.TextField()
    Text = models.TextField()
    ReleaseTime = models.DateTimeField()
    ishide = models.BooleanField(default=False)
    Reply = models.BigIntegerField()
    Like = models.BigIntegerField()
    DisLike = models.BigIntegerField()
    DownVote = models.BigIntegerField()
    isDeleted = models.BooleanField(default=False)
    class Meta:
      verbose_name = '讨论' 
      verbose_name_plural = verbose_name 


class Comment(models.Model):
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    Discussion = models.ForeignKey(Discussion, blank=True, null=True, on_delete=models.SET_NULL)
    Number = models.BigIntegerField()
    Text = models.TextField()
    ReleaseTime = models.DateTimeField()
    Like = models.BigIntegerField()
    DisLike = models.BigIntegerField()
    DownVote = models.BigIntegerField()
    isDeleted = models.BooleanField(default=False)
    class Meta:
      verbose_name = '评论' 
      verbose_name_plural = verbose_name 


class Vote(models.Model):
    Discussion = models.ForeignKey(Discussion, blank=True, null=True, on_delete=models.SET_NULL)
    Comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    DeltaUpvote=models.BigIntegerField()
    DeltaDownvote=models.BigIntegerField()
    isUpvote=models.BooleanField()
    isDeleted=models.BooleanField()
    class Meta:
      verbose_name = '赞/踩' 
      verbose_name_plural = verbose_name 
    

class paste(models.Model):
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    url = models.TextField()
    isPublic = models.BooleanField(default=False)
    class Meta:
      verbose_name = '剪切板' 
      verbose_name_plural = verbose_name 


class JudgeData(models.Model):
    CompileError = 'CE'
    Accepted = 'AC'
    WrongAnswer = 'WA'
    RuntimeERROR = 'RE'  # Please do not use 'RuntimeError' as a name
    TimeLimitExceeded = 'TLE'
    MemoryLimitExceeded = 'MLE'
    OutputLimitExceeded = 'OLE'
    ParticallyCorrect = 'PC'
    SystemError = 'SE'
    STATUS_CHOICES = {
        (CompileError, 'CompileError'),
        (Accepted, 'Accepted'),
        (WrongAnswer, "WrongAnswer"),
        (RuntimeERROR, 'RuntimeError'),
        (TimeLimitExceeded, "TimeLimitExceeded"),
        (MemoryLimitExceeded, 'MemoryLimitExceeded'),
        (OutputLimitExceeded, 'OutputLimitExceeded'),
        (ParticallyCorrect, 'ParticallyCorrect'),
        (SystemError, 'SystemError')
    }
    JudgeStatus = models.CharField(max_length=64, choices=STATUS_CHOICES)
    Score = models.FloatField(default=0)
    LocalID = models.BigIntegerField()
    ProblemSet = models.ForeignKey(ProblemSet, blank=True, null=True, on_delete=models.SET_NULL)
    Problem = models.ForeignKey(Problem, blank=True, null=True, on_delete=models.SET_NULL)
    Contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    isPublic = models.BooleanField()
    class Meta:
      verbose_name = '评测任务' 
      verbose_name_plural = verbose_name 

class Notice(models.Model):
    Title=models.TextField()
    Color=models.TextField()
    Background=models.TextField(default='null')
    Type=models.TextField(default='Color')
    class Meta:
      verbose_name = '公告' 
      verbose_name_plural = verbose_name 