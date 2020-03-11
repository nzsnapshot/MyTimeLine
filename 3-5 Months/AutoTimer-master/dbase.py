import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS report (name TEXT, active BOOLEAN, start TEXT, end TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS times (start TEXT, end TEXT)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS production (date TEXT, item TEXT, begin TEXT, end TEXT)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS pause (date TEXT, begin TEXT, end TEXT)")

        # self.cur.execute("CREATE TABLE IF NOT EXISTS pricing (id INTEGER PRIMARY KEY, title TEXT, price INTEGER)")

        # self.cur.execute("CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS passwords (password TEXT PRIMARY KEY)")
        self.conn.commit()

    def reportfetch(self):
        self.cur.execute("SELECT * FROM report")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, active):
        # self.cur.execute("INSERT OR IGNORE INTO report VALUES (?, ?, ?, ?)", (name, active, start, end,))
        self.cur.execute("INSERT OR IGNORE INTO report VALUES (?, ?)", (name, active,))
        self.conn.commit()

    def times(self, start, end):
        # self.cur.execute("INSERT OR IGNORE INTO report VALUES (?, ?, ?, ?)", (name, active, start, end,))
        self.cur.execute("INSERT OR IGNORE INTO times VALUES (?, ?)", (start, end,))
        self.conn.commit()

    def update(self, name, bool):
        self.cur.execute("SELECT * FROM report")
        self.cur.execute(f"UPDATE report SET active = {bool} WHERE name = '{name}'")
        self.conn.commit()
            

    def diff(self):
        self.cur.execute("SELECT julianday(end) - julianday(start) FROM times")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
