import sys, io, requests, json, cgi, cgitb
import sqlite3

cgitb.enable()
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding="utf-8")


con = sqlite3.connect("myrest.sqlite3")
cur = con.cursor()

a = 0
try:
    cur.execute("SELECT * FROM rest")
    all = cur.fetchall()
except:
    a = 1
    content = "<h1>該当なし</h1>"


template="""
<html>
 <head> 
  <meta charset = "utf-8">
  <title>MyShow</title>
  <link rel="stylesheet" href="../R02/my_reg.css">
 </head>
 <body class="show_result">
 <div class="show"><a href=../R02/home.html>Homeへ戻る</a></div>
 <div class="b">
  {a}
  </div>
 </body>
</html>

"""

if(a==0):
    content = "<table border=4> <tr><th>店名</th><th>評価</th><th>駅</th><th>コメント</th></tr>"
    for x in all:
        content+= "<tr><td>{rest}</td><td>{eva}</td><td>{sta}</td><td>{com}</td></tr>".format(rest=x[0],eva=x[1],sta=x[2],com=x[3])
    content += "</table>"


results = template.format(a=content)
print("Content-type: text/html\n;")
print(results)