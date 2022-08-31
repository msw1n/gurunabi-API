import sqlite3
import sys, io, requests, json, cgi, cgitb
import os.path
cgitb.enable()
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding="utf-8")




con = sqlite3.connect("myrest.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS rest(name,eva,sta,com);")


name = form.getvalue("rest"," ")
eva = form.getvalue("eva"," ")
sta = form.getvalue("sta"," ")
t = form.getvalue("t"," ")

h = 0
if(name != " " and eva != " " and sta != " "):
    se = "SELECT * FROM rest WHERE name == '{name}' and sta=='{sta}'".format(name=name,sta=sta)
    cur.execute(se)
    all = cur.fetchall()
    if(len(all)==0):
        h = 1
        cur.execute("INSERT INTO rest(name,eva,sta,com) values(?,?,?,?)",[name,eva,sta,t])
    else:
        h = 1
        cur.execute("DELETE FROM rest WHERE name='{name}' and sta=='{sta}'".format(name=all[0][0],sta=all[0][2]))
        con.commit()
        cur.execute("INSERT INTO rest(name,eva,sta,com) values(?,?,?,?)",[name,eva,sta,t])


else:
    h = 0


template = """
<html>
<head> 
<meta charset = "utf-8">
<title>myrest</title>
<link rel="stylesheet" href="../R02/my_reg.css">
</head>
<body class="reg">
<div><a href=../R02/home.html>Homeへ戻る</a></div>

<form method="GET" action="my_reg.py">
<p>あなたの評価を登録できます。</p>
<p>登録名（必須） : <input type="text" name="rest"></p>
<p  class="radios">評価（星☆ 1~5）（必須）: <input type="radio" name="eva" value="1">1
<input type="radio" name="eva" value="2">2
<input type="radio" name="eva" value="3">3
<input type="radio" name="eva" value="4">4
<input type="radio" name="eva" value="5">5
</p>
<p>駅（必須） : <input type="text" name="sta"></p>
<p>コメント : <textarea name="t"></textarea></p>
<p><input type="submit" value="登録"></p>
</form>

</body>
</html>
"""


template2 = """
<html>
<head> 
<meta charset = "utf-8">
<title>MyReg</title>
<link rel="stylesheet" href="../R02/my_reg.css">
</head>
<body class="accept">
<div class="a">
<h2>登録完了</h2>
<div class="show"><a href="../R02/home.html">Homeへ戻る</a></div>
</div>
</body>
</html>
"""





if(h==0):
    results = template.format()
elif(h==1):
    results = template2.format()
con.commit()
con.close()



print("Content-type: text/html\n;")
print(results)









