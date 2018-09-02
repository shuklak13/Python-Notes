# http://www.sqlitetutorial.net/sqlite-python/

# to view this database, go to C:\data\db and run `sqlite3 pythonsqlite.db`

import sqlite3

sql_cmd = { "create_table": {
                "projects":    """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """,
                "tasks":        """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );""" } ,
            "insert_row": {
                "projects":    ''' INSERT INTO projects(name, begin_date, end_date) VALUES(?,?,?) ''',
                "tasks":        ''' INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date) VALUES(?,?,?,?,?,?) '''}
            }

def create_connection(db_file=None):
    if db_file is None:
        db_file = ':memory:'
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn, table):
    sql = sql_cmd["create_table"][table]
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# "Row" is a tuple
def insert_row(conn, row, table):
    sql = sql_cmd["insert_row"][table]
    cur = conn.cursor()
    cur.execute(sql, row)   # row's values replace the '?'s in sql
    return cur.lastrowid

def delete_row(conn, row, table):
    sql = 'DELETE FROM ' + table + ' WHERE id=?'
    cur = conn.curosr()
    cur.execute(sql, (id,))

def delete_all_rows(conn, row, table):
    sql = 'DELETE FROM ' + table
    cur = conn.curosr()
    cur.execute(sql)

def update_rows(conn, update_params, table):
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, update_params)

def view_table(conn, table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table)
    for row in cur.fetchall():
        print(row)

if __name__ == '__main__':
    conn = create_connection("C:\\data\db\pythonsqlite.db")
    
    create_table(conn, "projects")
    create_table(conn, "tasks")
    
    project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
    project_id = insert_row(conn, project, "projects")

    task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
    task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
    insert_row(conn, task_1, "tasks")
    insert_row(conn, task_2, "tasks")

    update_rows(conn, (2, '2015-01-04', '2015-01-06',2), "tasks")

    view_table(conn, "tasks")
    
    conn.close()