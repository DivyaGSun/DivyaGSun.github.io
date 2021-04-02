#!/usr/bin/python
import pymysql
import sys
import cgi

import cgitb
cgitb.enable()

# print content-type
print("Content-type: text/html\n")

print("<html><head>")
print("<title>Search miRNA by target</title>")
#margin:30;padding:30;
print('''<style>
body {padding:30; min-height: 100%; width: 100%;}
.bg-image {
	background-image: url('https://img.wallpapersafari.com/desktop/1680/1050/88/96/kygWwU.jpg');
	width:100%;
	min-height:100%;
	background-repeat: no-repeat;
	background-attachment: fixed;
	background-size: cover;

}

h1 {
  font-size: 30px;
  color: #000;
  border-bottom: 2px solid #ccc;
  padding-bottom: 5px;
}

h1::after {
  content: "";
  display: block;
  border-bottom: 1px solid orange;
  width: 13%;
  position: relative;
  bottom: -7px; /* padding + border-width */
}


#miRNA {
	font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
	border-collapse: collapse;
	width: 50%;
}

#miRNA td, #miRNA th {
	border: 1px solid #ddd;
	padding: 8px;
}

#miRNA tr:nth-child(even){background-color: #f2f2f2;}

#miRNA tr:hover {background-color: #ddd;}

#miRNA th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #266150;
	color: white;
}
</style>

</head>''')
print("<body>")
print('''<div class="bg-image">''')
print("<h1>Search Gene</h1>")
print("<h3>Find which miRNAs target your gene of Interest</h3>")
# fix the url below! add your username
print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/divyas3/HW04.py" onsubmit="return checkInput()" method="GET" >
		<div class = "ui-widget">
		<label for = "genename">Enter Genename: </label>
		<input type="text" id="genename" name="genename" placeholder="genename" step="any">
		</div>
		<label for = "score">Optional: </label>
		<input type="text" id="score" name="score" placeholder="max score">
		<input type="submit" id="submit" value="Search">
		</form>''')
#query for checking if gene exists
query = """SELECT gene.name as name
		   FROM gene;"""
try:
	connection = pymysql.connect(host="bioed.bu.edu", user="test", password="test", db="miRNA", port=4253)
	with connection.cursor() as cursor:
		row = cursor.execute(query)
		records = cursor.fetchall()
		resultList = [list(i) for i in records]
		flat_list = [item for sublist in resultList for item in sublist]
	cursor.close()
	connection.close()
except Exception as mysqlError:
	print("<p><font color=red><b>Error</b> while executing query</font></p>")
	print(flat_list)

#javascript for checking valid input
print('''<script type="text/javascript">
function checkInput() {
	var x = document.getElementById('genename').value;
	var genes = %s
	var ret = false;
	if (x == "") {
		alert("Please enter a gene name");
		return false;
	}
	else if (genes.indexOf(x)== -1) {
		alert ("gene name not found");
		return false;
	}
	else {
		return true;
	}
}
</script>''')%flat_list
# get the form
form = cgi.FieldStorage()
genename = form.getvalue("genename")
score = form.getvalue("score")
#querys for valid inputs
if genename:
		print("<h2>%s Max Score:%s</h2>"%(genename,score))
		print("<table id=miRNA>")
		print("<tr><th>miRNA name</th><th>score</th></tr>")
		if score:
		 query = """SELECT miRNA.name as name, targets.score as score
		 FROM miRNA JOIN targets ON (miRNA.mid=targets.mid) JOIN gene ON (targets.gid=gene.gid)
		 WHERE gene.name='%s' and score < '%s';""" %(genename,score)
		else:
		 query = """SELECT miRNA.name as name, targets.score as score
		FROM miRNA JOIN targets ON (miRNA.mid=targets.mid) JOIN gene ON (targets.gid=gene.gid)
		WHERE gene.name='%s';""" %(genename)

		#print(query)
		try:
			connection = pymysql.connect(host="bioed.bu.edu", user="test", password="test", db="miRNA", port=4253)
			with connection.cursor() as cursor:
				cursor.execute(query)
				records = cursor.fetchall()
				y = list(records)
				y = [(x[0], 'NA') if x[1] is None else x for x in y]
				records = tuple(y)
				for row in records:
					print("<tr><td>%s</td><td>%s</td></tr>" % (row[0], row[1]))
				cursor.close()
			connection.close()
		except Exception as mysqlError:
			print("<p><font color=red><b>Error</b> while executing query</font></p>")

		print("</table>")
print('''<link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css"
         rel = "stylesheet">
      <script src = "https://code.jquery.com/jquery-1.10.2.js"></script>
      <script src = "https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script>

      <!-- Javascript -->
      <script>
         $(function() {
            var availableGenes  = %s
            $( "#genename" ).autocomplete({
               source: availableGenes
            });
         });
      </script>''')%flat_list
print("</body></html>")
