import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY, name text, nationality text, passport integer, department integer)")
        self.conn.commit()

    def insert(self, name, nationality, passport, department):
        self.cur.execute("INSERT INTO Student VALUES (NULL,?,?,?,?)", (name, nationality, passport, department))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM Student")
        rows = self.cur.fetchall()
        return rows

    def search(self, name="", nationality="", passport="", department=""):
        self.cur.execute("SELECT * FROM Student WHERE name=? OR nationality=? OR passport=? OR department=?", (name, nationality, passport, department))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM Student WHERE id=?", (id,))
        self.conn.execute()

    def update(self, id, name, nationality, passport, department):
        self.cur.execute("UPDATE Student SET title=?, author=?, year=?, isbn=? WHERE id=?", (name, nationality, passport, department))
        self.conn.execute()

    def __del__(self):
        self.conn.close()