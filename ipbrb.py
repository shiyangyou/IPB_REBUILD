import MySQLdb

table_ips_cv = "ips_cv_814"
table_ips2view = "ips2view"

db = MySQLdb.connect(host="localhost",user="root",passwd="1234",db="ipb_rebuild")
cursor = db.cursor()

sql_q1 = "select * from %s" %s table_ips_cv

rows = cursor.execute(sql_query)
List = cursor.fetchall()

for i in range(len(List)):
	id = List[i][0]
	sql_q2 = "select "