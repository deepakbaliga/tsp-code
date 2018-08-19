#2 
# In this module we seperate clicks inside of the specified lab exams and otherwise exam and normal lab conditions
# The labs took place on the 7th and 28th of November 2014, from 11am-1pm on both days. (Measured as stress)
# The start and end times in UNIX form of both labs are shown in Table 4-1.

# Lab 1 1415358000000 1415365200000
# Lab 2 1417172400000 1417179600000


# Adding a new column to the SQLite database

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('mouse.db')
       

    with con:
        cur = con.cursor() 
        
        #cur.execute("ALTER TABLE MOVEMENTS ADD COLUMN ENVIRONMENT TEXT;")
        cur.execute("UPDATE MOVEMENTS SET ENVIRONMENT = 'IN LAB' WHERE (timestamp >= 1415358000000 and timestamp <= 1415365200000) or (timestamp >= 1417172400000 and timestamp <= 1417179600000);");
        cur.execute("UPDATE MOVEMENTS SET ENVIRONMENT = 'OUT LAB' WHERE  NOT (timestamp >= 1415358000000 and timestamp <= 1415365200000) or (timestamp >= 1417172400000 and timestamp <= 1417179600000);");
        con.commit()
        

    
              
except lite.Error, e:   
    print "Error %s:" % e.args[0]
    con.close()
    sys.exit(1)

if con:
    
    con.close()


