stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stocksList = stocks.split(",")
stock = tuple(stocksList)

list = []
for idx, val in enumerate(stock):
    this = val.split("/")
    print
    list.append({"종목": this[0], "수익률": f"{(sells[idx]/int(this[2]) * 100 - 100):.2f}"})

list = sorted(list, key=lambda s:(float(s['수익률'])), reverse=True)

for idx, val in enumerate(list):
    print(list[idx]["종목"]+"의 수익률 "+ list[idx]["수익률"])
