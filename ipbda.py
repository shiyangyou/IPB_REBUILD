import json
from collections import defaultdict #create default values for dict
import MySQLdb

sub_di = {}

db = MySQLdb.connect(host="localhost",user="root",passwd="1234",db="ipb_rebuild")
table = "ips2view"
cursor = db.cursor()


f = open("newips2pop.json")
df = f.read()
di = json.loads(df)


# ips2pop writing into db
for k in di[0]:
	#print k
	ips_id=k[8:40]
	for pop in di[0][k]:
		di_2=json.loads(di[0][k][pop])		
		sub_di["IPS_ID"]=ips_id
		sub_di["POP_IPS"]=pop
		sub_di["TT"]=di_2["tt"]
		sub_di["QOS"]=di_2["qos"]
		sub_di["TS"]=di_2["ts"]
		sub_di["LP"]=di_2["lp"]
		qmarks = ','.join(['%s']*len(sub_di))
		cols = ','.join(sub_di.keys())
		sql_insert = "INSERT INTO %s (%s) VALUES (%s)" % (table,cols,qmarks)
		cursor.execute(sql_insert,sub_di.values())

# very important
db.commit()
cursor.close()
db.close()

