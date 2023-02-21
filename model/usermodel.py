import json
import mysql.connector
class User():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Singh@@19961996",database="USER")
            print("connection stablished")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
        except:
            print("some error occered!!")


        
        
    def getalluser(self):
        self.cur.execute("SELECT * FROM alluser")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data available !!!!"

    
    def getoneuser(self,data):
        self.cur.execute(f"SELECT * FROM alluser WHERE USERNAME='{data['USERNAME']}'")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data available against this name !!!!"
        


    def createuser(self,data):
        self.cur.execute(f"INSERT INTO alluser(USERNAME,PASSWORD,FATHERNAME) VALUES('{data['USERNAME']}','{data['PASSWORD']}','{data['FATHERNAME']}')")
        return "user created"

    def deleteuser(self,data):
        try:
            self.cur.execute(f"DELETE FROM alluser WHERE USERNAME='{data['USERNAME']}'")
            return "user deleted"
        except:
            return "no user exist with this name "





