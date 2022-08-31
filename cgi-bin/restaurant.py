
import sys, io, requests, json, cgi, cgitb
from black import mypyc_attr
cgitb.enable()
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding="utf-8")

template="""

<html>
 <head> 
  <meta charset = "utf-8">
  <title>Search</title>
  <link rel="stylesheet" href="../R02/my_reg.css">
 </head>
 <body class="res">
  <div><a href=../R02/home.html>Homeへ戻る</a></div>
  <form method="GET" action="result.py">
   <p>店名 : <input type="text" name="res"></p>
   <p>住所 : <input type="text" name="add"></p>
   <p>キーワード（駅など） : <input type="text" name="key"></p>
   <p><input type="submit" value="検索"></p>
  <form>
 </body>
</html>

"""


results = template.format()
print("Content-type: text/html\n;")
print(results)



