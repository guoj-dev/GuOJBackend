from math import pow
def GetEloWinProbility(RankA, RankB):
    return 1.0/(1+pow(10,(RankB-RankA)/400.0))
def GetPlayerSeeds(PlayerRatings):
    if type(PlayerRatings)!=dict:
        raise TypeError
    PlayerSeeds=PlayerRatings
    for (PlayerName1,Rating1) in PlayerRatings.items():
        seed=1
        for (PlayerName2,Rating2) in PlayerRatings.items():
            if PlayerName1 == PlayerName2:
                continue
            seed+=GetEloWinProbility(Rating2,Rating1)
        PlayerSeeds[PlayerName1]=seed
    return PlayerSeeds
def BinarySearch(Ratings,m):
    pass
def GetPlayerNewRating(PlayerData):
    pass

            

