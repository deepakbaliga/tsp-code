# 3

import pandas as pd
import numpy as np
import sqlite3 as lite
import sys

con = None


try:
    con = lite.connect('mouse.db')
       

    with con:
        cur = con.cursor() 

        # Get every entry in 
        
        

        con.commit()
        

    
              
except lite.Error, e:   
    print "Error %s:" % e.args[0]
    con.close()
    sys.exit(1)

if con:
    
    con.close()