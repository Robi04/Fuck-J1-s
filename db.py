import sqlite3 
import datetime
global con 
con = sqlite3.connect("fuckJ1.db")
global c 
c = con.cursor()


def getScoresDesc(difficulty):
    c.execute("Select * from records WHERE difficulty = ? order by score desc limit 10",(difficulty,))
    return c.fetchall()

def insertScore(player_name, score,jump_count,time,difficulty):
    date_str = str(datetime.datetime.now())[:10] +" "+ str(datetime.datetime.now())[11:16] 
    c.execute("insert into records(score,player_name,date_hour,jump_count,time,difficulty) values (?, ?, ?, ?, ?, ?)",
            (score, player_name, date_str,jump_count,time,difficulty))
    con.commit()


# c.execute("DELETE FROM records")

# c.execute("CREATE TABLE IF NOT EXISTS RECORDS(record_id integer primary key,score,player_name,date_hour,jump_count,time,difficulty)")
# c.execute("insert into records(score,player_name,date_hour,jump_count,time,difficulty values(2,'fabien', '02/01/2021 13:56',)")
# c.execute("insert into records(score,player_name,date_hour,jump_count,time,difficulty) values(66,'margot', '05/12/2022 12:45')")
# c.execute("insert into records(score,player_name,date_hour,jump_count,time,difficulty) values(67,'robin', '04/07/2022 11:30')")
# c.execute("Select * from records")
con.commit()
print(c.fetchall())