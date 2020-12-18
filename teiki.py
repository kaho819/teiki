def teiki(n, m):
    buy = 54660/6 + 126*2*n + 263*m

    not_buy = 1110*n + 1278*m

    print("渋谷:"+str(n)+"回　三茶:"+str(m)+"回")
    print("買った場合"+str(buy))
    print("買わない場合"+str(not_buy))
    print("買った方が" + str(not_buy-buy) + "円得")

print("渋谷，三茶に行く回数")
n, m = (int(x) for x in input().split())
teiki(n, m)