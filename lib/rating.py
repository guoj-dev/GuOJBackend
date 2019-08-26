from math import pow,sqrt,trunc
def GetEloWinProbility(RankA:int, RankB:int):
    return 1.0/(1+pow(10,(RankB-RankA)/400.0))
def GetPlayerSeed(PlayerRatings:dict,PlayerName:str):
    if type(PlayerRatings)!=dict or type(PlayerName)!=str:
        raise TypeError
    seed=1
    Rating=PlayerRatings[PlayerName]
    for (PlayerName1,Rating1) in PlayerRatings.items():
        if PlayerName1 == PlayerName:
            continue
        seed+=GetEloWinProbility(Rating1,Rating)
    return seed
def GetRatingSeed(PlayerRatings:dict,Rating:int):
    if type(PlayerRatings)!=dict or type(Rating)!=int:
        raise TypeError
    return sum([GetEloWinProbility(i,Rating) for (name,i) in PlayerRatings.items()],1)
def GetAverageRank(PlayerRatings:dict,PlayerRanks:dict,PlayerName:str):
    if type(PlayerRatings)!=dict or type(PlayerRanks)!=dict or type(PlayerName)!=str:
        raise TypeError
    return sqrt(PlayerRanks[PlayerName]*GetPlayerSeed(PlayerRatings,PlayerName))
def BinarySearch(PlayerRatings:dict,m:int):
    left=1
    right=8000
    while right-left>1:
        mid=(left+right)/2
        if GetRatingSeed(PlayerRatings,mid)<m:
            right=mid;
        else:
            left=mid
    return left
# PlayerName:(Rating,Rank)
def GetPlayerNewRatingDelta(PlayerData:dict):
    if type(PlayerData)!=dict:
        raise TypeError
    PlayerRatings={}
    PlayerRanks={}
    for (PlayerName,Data) in PlayerData.items():
        if type(Data)!=tuple:
            raise TypeError
        PlayerRatings[PlayerName]=Data[0]
        PlayerRanks[PlayerName]=Data[1]
    PlayerRatingDelta={}
    for (PlayerName,Data) in PlayerData.items():
        PlayerRatingDelta[PlayerName]=(BinarySearch(PlayerRatings,GetAverageRank(PlayerRatings,PlayerRanks,PlayerName)-Data[0]))
    PlayerRatingDeltaSum=sum([Delta for (PlayerName,Delta) in PlayerRatingDelta.items()])
    for (PlayerName,Data) in PlayerRatingDelta.items():
        Data+=-PlayerRatingDeltaSum/len(PlayerRatingDelta)-1
    for (PlayerName,Data) in PlayerRatingDelta.items():
        Data+=min(max(-sum(PlayerRatingDelta[0:min(trunc(4*round(sqrt(len(PlayerRatingDelta)))),len(PlayerRatingDelta))])/min(trunc(4*round(sqrt(len(PlayerRatingDelta)))),len(PlayerRatingDelta)),-10),0)
    return PlayerRatingDelta
    