def Cowcoin(coin_list,coin_set):
    for i in coin_list:
        coin_set|={current+i for current in coin_set}
    return len(coin_set)-1


coins=int(input())
coin_list=list(map(int,input().split()))[:coins]
coin_set={0}
print(Cowcoin(coin_list,coin_set))