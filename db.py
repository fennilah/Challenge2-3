import os


def connect_to_db(config=None):
    if config == 'test':
        
        db_name' = os.getenv('TEST_DB')
    
    else:
        
        db_name = os.getenv('DB_NAME')

    user = os.getenv('DB_USERNAME')
    host = os.getenv('DB_HOST')
    password = os.getenv('DB_PASSWORD')

    print  "db"
    
    # db=('db_name')
    # user=('user')
    # host=('host')
    # password=('password')


def create_user_table():
        """CREATE TABLE users (
            userid serial PRIMARY KEY,
            username varchar (30) NOT NULL,
            useremail varchar (50) NOT NULL,
            password varchar (80) NOT NUL
        """


def create_entry_table(cur):
    cur.execute(
        """CREATE TABLE diaries (
            mydiaryid serial PRIMARY KEY,
            userid integer REFERENCES users(userid),
            mydiarydate varchar (30) NOT NULL,
            mydiarytitle varchar (30) NOT NULL,
            mydiary text NOT NULL
        """)


def main(config=None):
    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute

    create_user_table(cur)
    create_entry_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database successful')


if __name__ == '__main__':
    main()