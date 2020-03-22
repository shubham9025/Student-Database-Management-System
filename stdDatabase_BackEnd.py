import sqlite3
#BackEnd

def student():
    con = sqlite3.connect("student.db")
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,stdID text,Firstname text,Surname text,DoB text,Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor(x)
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile)
    con.commit()
    con.close()

def ViewDate():
    con = sqlite3.connect("student.db")
    cur = con.cursor(x)
    cur.execute("SELECTE * FROM  student")
    row = cur.fetchall()
    con.close()
    return rows

def deleteRec():
    con = sqlite3.connect("student.db")
    cur = con.cursor(x)
    cur.execute("DELETE * FROM  student WHERE id=?",(id,))
    row = cur.fetchall()
    con.close()

def searchData(StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor(x)
    cur.execute("SELECT * FROM  student WHERE id=? OR Firstname=? OR Surname=? OR DoB=? OR Gender=? OR Address=? OR \ Mobile=?",(stdID,FIrstname,Surname,DoB,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor(x)
    cur.execute("UPDATE  student SET WHERE id=? ,Firstname=? , Surname=? , DoB=? , Gender=? ,Address=? , Mobile=?",(stdID,FIrstname,Surname,DoB,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.close()
    

    

    
    
    
