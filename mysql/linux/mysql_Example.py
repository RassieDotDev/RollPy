import MySQLdb

connection = MySQLdb.connect (host = "localhost",		#server location
                              user = "username",		#server username
                              passwd = "password",		#server password
                              db = "database")			#db we are connecting to
cursor = connection.cursor()					#this is where you create a object that can comunicate with the mysql daemon 
cursor.execute("SELECT * FROM users") 				#execute a mysql command to interface with the db
print("fetchall:")						
result = cursor.fetchall() 					#store the output inside of a variable
for r in result:						#itterate through the results
    print(r)							#print out the results of the command. will be an array
