import sys, io, requests, json, cgi, cgitb
import sqlite3

cgitb.enable()
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding="utf-8")

con = sqlite3.connect("myrest.sqlite3")
cur = con.cursor()

name = form.getvalue("name"," ")
sta = form.getvalue("station"," ")

h = 0
if(name != " " and sta == " "):
    h = 1
    se = "SELECT * FROM rest WHERE name LIKE '%{name}%'".format(name=name)
    cur.execute(se)
    all = cur.fetchall()
elif(sta != " " and name == " "):
    h = 1
    se = "SELECT * FROM rest WHERE sta == '{sta}'".format(sta=sta)
    cur.execute(se)
    all = cur.fetchall()
elif(name != " " and sta != " "):
    h = 1
    se = "SELECT * FROM rest WHERE sta == '{sta}' and name LIKE '%{name}%'".format(sta=sta,name = name)
    cur.execute(se)
    all = cur.fetchall()
else:
    h = 0

template="""
<html>
 <head> 
  <meta charset = "utf-8">
  <title>MyShow</title>
  <link rel="stylesheet" href="../R02/my_reg.css">
 </head>
 <body class=show_result>
 <div class="show"><a href='../R02/home.html'>Homeへ戻る</a></div>
 <div class="b">
  {a}
 </div>
 </body>
</html>

"""

if(h==1):
    if(len(all)==0):
        content = "<h1>該当なし</h1>"
    else:
        content = "<table border=4> <tr><th>店名</th><th>評価</th><th>駅</th><th>コメント</th></tr>"
        for x in all:
            content+= "<tr><td>{rest}</td><td>{eva}</td><td>{sta}</td><td>{com}</td></tr>".format(rest=x[0],eva=x[1],sta=x[2],com=x[3])
        content += "</table>"


template2 = """
<html>
<head> 
<meta charset = "utf-8">
<title>MySearch</title>
<link rel="stylesheet" href="../R02/my_reg.css">
</head>
<body class="search">
<div><a href=../R02/home.html>Homeへ戻る</a></div>
<form method="GET" action="my_search.py">
<p>あなたの評価を検索できます。</p>
<p>登録名（部分一致） : <input type="text" name="name"></p>
<p>駅（完全一致）: <input type="text" name="station"></p>
<p><input type="submit" value="検索"></p>
</form>

</body>
</html>
"""

if(h==0):
    results = template2.format()
elif(h==1):
    results = template.format(a=content)

print("Content-type: text/html\n;")
print(results)
