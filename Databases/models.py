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
    Nameplate = models.CharField(max_length=16)
    NameColor = models.CharField(max_length=16)
    NameplateColor = models.CharField(max_length=16)
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
    Text = models.TextField()

    def __str__(self):
        return self.username

    def data(self):
        return [
            {
                'name':
                    {
                        'text': self.Username,
                        'color': self.NameColor
                    },
                'Sex': self.Sex,
                    'avatar': self.Avatar,
                    'nameplate':
                    {
                        'text': self.Nameplate,
                        'color': self.NameplateColor
                    },
                'text': self.Text,
                    'date': self.UserRegisterDate,
                    'coins': self.Coins,
                    'experince': self.Experience,
                    'contribution': self.Contribution,
                    'rating': self.Rating,
                    'statics':
                    {
                        'AC': self.AcceptedCount,
                        'WA': self.WrongAnswerCount,
                        'RE': self.RuntimeErrorCount,
                        'TLE': self.TimeLimitExceededCount,
                        'MLE': self.MemoryLimitExceededCount,
                        'OLE': self.OutputLimitExceededCount,
                        'PC': self.ParticallyCorrectCount,
                        'SE': self.SystemErrorCount
                    }
            }
        ]


class Group(models.Model):
    LEVEL_CHOICE = {
        ('N', 'Normal'), ('T', 'Trusted'), ('A', 'Admin')
    }
    GroupName = models.TextField()
    UserCount = models.BigIntegerField()
    Level = models.CharField(max_length=16, choices=LEVEL_CHOICE)
    AllowJoin = models.NullBooleanField()
    isOfficial = models.BooleanField()
    

    def __str__(self):
        return self.GroupName


class ProblemSet(models.Model):
    PERMISSION_CHOICE = {
        ('S', 'Stricted'), ('SP', 'Private'), ('P', 'Public')
    }
    ProblemSetName = models.TextField()
    ProblemSerPrefix = models.TextField()
    Group = models.ManyToManyField(Group, related_name='ProblemSet')
    Permission = models.CharField(max_length=16, choices=PERMISSION_CHOICE)
    AuthedUser = models.ManyToManyField(User)

    def __str__(self):
        return self.ProblemSetName


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
    # TODO:ProblemLevel
    ProblemTitle = models.TextField()
    ProblemDescription = models.TextField()
    ProblemDataPath = models.TextField()

    def __str__(self):
        return self.ProblemTitle


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


class Vote(models.Model):
    Discussion = models.ForeignKey(Discussion, blank=True, null=True, on_delete=models.SET_NULL)
    Comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    DeltaUpvote=models.BigIntegerField()
    DeltaDownvote=models.BigIntegerField()
    isUpvote=models.BooleanField()
    isDeleted=models.BooleanField()
    

class paste(models.Model):
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    url = models.TextField()


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
    Score = models.FloatField()
    LocalID = models.BigIntegerField()
    ProblemSet = models.ForeignKey(ProblemSet, blank=True, null=True, on_delete=models.SET_NULL)
    Problem = models.ForeignKey(Problem, blank=True, null=True, on_delete=models.SET_NULL)
    Contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    isPublic = models.BooleanField()