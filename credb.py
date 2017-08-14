import MySQLdb

db_host = 'localhost'
db_user = 'root'
db_pw = '1234'
db_name = 'ipb_rebuild'

try:
	db = MySQLdb.connect(db_host,db_user,db_pw,charset='utf8')
	cursor = db.cursor()

	# create database ipb
	cursor.execute('DROP DATABASE IF EXISTS %s' %db_name)
	cursor.execute('create database if not exists %s' %db_name )
	db.select_db(db_name)

	# create table
	table_name = 'ips'
	cursor.execute('CREATE TABLE %s' %table_name)

	except MySQLdb.Error as e:
		print "Mysql Error %d: %s" %(e.args[0],e.args[1])
	finally:
		db.close()
