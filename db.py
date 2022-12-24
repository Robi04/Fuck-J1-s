import sqlite3 
import datetime
global con 
con = sqlite3.connect("robzybird.db")
global c 
c = con.cursor()


def getScoresDesc():
    c.execute("Select * from records order by score desc limit 10")
    return c.fetchall()

def insertScore(player_name, score):
    date_str = str(datetime.datetime.now())[:10] +" "+ str(datetime.datetime.now())[11:16] 
    c.execute("insert into records(score,player_name,date_hour) values (?, ?, ?)",
            (score, player_name, date_str))
    con.commit()




# c.execute("CREATE TABLE IF NOT EXISTS RECORDS(record_id integer primary key,score,player_name,date_hour)")
# c.execute("insert into records(score,player_name,date_hour) values(2,'fabien', '02/01/2021 13:56')")
# c.execute("insert into records(score,player_name,date_hour) values(66,'margot', '05/12/2022 12:45')")
# c.execute("insert into records(score,player_name,date_hour) values(67,'robin', '04/07/2022 11:30')")
# c.execute("Select * from records")
# con.commit()
# print(c.fetchall())