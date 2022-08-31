import sys, io, requests, json, cgi, cgitb,os
from dotenv import load_dotenv
cgitb.enable()
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding="utf-8")

shops = {} #辞書だとkey名同じで一番最後しか登録されない
name = []
logo = []
address = []
station = []
area = []
genre = []
budget = []
url = []
photo = []
open = []
close = []


res = form.getvalue("res","")
add=form.getvalue("add","")
keyword=form.getvalue("key","")

count = 1


while True:
    urls = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key='APIキー打つ'&name={name}&format=json&count=100&start={count}&address={add}&keyword={keyword}".format(count=count,name=res,add=add,keyword=keyword)
    responce = requests.get(urls)
    result = json.loads(responce.text)["results"]["shop"]
    if len(result)==0:
        break
    else:
        for x in result:
            print("a")
            name.append(x["name"])
            logo.append(x["logo_image"])
            address.append(x["address"])
            station.append(x["station_name"])
            area.append(x["middle_area"]["name"])
            genre.append(x["genre"]["name"])
            budget.append(x["budget"]["average"])
            url.append(x["urls"]["pc"])
            photo.append(x["photo"]["pc"]["m"])
            open.append(x["open"])
            close.append(x["close"])
        count += 100




template = """
<html>
 <head> 
  <meta charset = "utf-8">
  <title>cgi</title>
  <link rel="stylesheet" href="../R02/style.css">
 </head>
 <body>
 <a href=../R02/home.html>Homeへ戻る</a>
  {a}
 </body>
</html>
"""

contents = "<div class=all>"
for x in range(0,len(name)):
    content = """<div class=shop>
    <p> 
    <image src = {i}>
    </p>
    <div class=in>
    店名 : {n}<br>
    住所 : {a}<br>
    エリア : {ar}<br>
    駅 : {s}<br>
    ジャンル : {g}<br>
    予算目安 : {b}<br>
    開店時間 : {o}<br>
    閉店時間 : {c}<br>
    <a href = {u}>このお店のサイトへ</a>
    </div> 
    """.format(i=photo[x],n=name[x],a=address[x],ar=area[x],s=station[x],g=genre[x],b=budget[x],o=open[x],c=close[x],u=url[x])
    content += "</div>" #shop
    contents += content

contents += "</div>" #all


results = template.format(a=contents)
print("Content-type: text/html\n;")
print(results)






