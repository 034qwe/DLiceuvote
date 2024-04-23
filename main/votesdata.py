import sqlite3 as sq



def data_start():
    global base,curs
    base = sq.connect('votes.db')
    curs = base.cursor()
    if base:
        print('data1 connect')
    base.execute('CREATE TABLE IF NOT EXISTS data1(name TEXT,sqnum TEXT PRIMARY KEY,vote INTEGER)')
    base.commit()
    base.execute("""CREATE TABLE IF NOT EXISTS data2(who INTEGER )""")
    base.commit()

def vote_check(sqnum):
    try:
        vt= base.execute(f"SELECT vote FROM data1 WHERE sqnum='{sqnum}'")
        base.commit()
        vot=str(*vt)[1:-2:]

        if int(vot)==1:
            
            return False
        else:
            return True 
    
    except Exception as e:
        print(f'ay{e} problem blin')

    # base.execute("INSERT INTO data1 VALUES('sasha','121212',True) ")
    # base.commit()

def add_vote(w):
    base.execute("INSERT INTO data2 (who) VALUES (?)", (w,))
    base.commit()


def block_vote(num):

    base.execute(f"UPDATE data1 SET vote = 1 WHERE sqnum = '{num}'")
    base.commit()


def get_result():
    lt= []
    n=1
    while n!=6:
        a = base.execute(f"SELECT who FROM data2 WHERE who={n}")
        lst= len([i[0] for i in [*a]])
        lt.append(lst)
        n+=1
    return lt
    
    
    
    # print(len(*a))