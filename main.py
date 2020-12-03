from flask import Flask
#import pandas as pd 
from flask_restful import Api, Resource

import pyodbc
import pandas as pd
#from datetime import date, datetime

app= Flask(__name__)
api = Api(app)


"""
data_put_args = reqparse.RequestParser()
data_put_args.add_argument("Number", type = int, help = "Phone Number Required", required = True)
data_put_args.add_argument("UID", type = str, help = "UID Required", required = True)
"""

number1 = 12344,
uid1 = "234GYLSH"
print ( number1,uid1)
class receiveData(Resource):
    def get(self, number, uid):
       # args= data_put_args.parse_args()
       number1=number
       uid1=uid
    
       print (number, uid)
       row= dbcall(uid1)
       return { "content" : row}


api.add_resource(receiveData,"/receivedata/<int:number>/<string:uid>")


def dbcall(uid1):
    Driver='ODBC Driver 17 for SQL Server'
    Server='sql-itcatta-dev01.database.windows.net'
    Database='sqldb-itcatta-dev01'
    Username='itcadmin'
    Pwd='Passw0rd'
    cnxn = pyodbc.connect('DRIVER='+Driver+';PORT=1433;SERVER='+Server+';DATABASE='+Database+';UID='+Username+';PWD='+Pwd)
       # engine=create_engine(Database_connection)
       # connection=engine.connect()
    cursor= cnxn.cursor()
    '''
    Sql_query4=pd.read_sql_query(select * from JSON_FILE_LOAD_STATUS,cnxn)
    
    df5=pd.DataFrame(Sql_query4,columns=['batchno','datetime','lastprinteduid','manufacturingdate','mrp'])
    
    for i in  len(df5[lastprinteduid]):
        if uid1==lastprinteduid:
            message="Valid UID"
        else:
            message="invalid"
            '''
            
    cursor.execute("SELECT * FROM dbo.JSON_FILE_LOAD_STATUS WHERE lastprinteDUID = '%s'" % uid1 )
    
    #cursor.execute('''DECLARE @uidcheck 
                   #SET @uidcheck= '%s' ''' % uid1)
    #check= '''IF @uidcheck = (SELECT UID FROM dbo.JSON_FILE_LOAD_STATUS)
                   #PRINT  'oRIGINAL' ''' 
    #cursor.executemany(check)
                
    row=cursor.fetchone()
    print (row)
    if row is None:
        return("Not Original")
    else:
        return("Original")
   
if __name__== "__main__":
    app.run(debug=True)