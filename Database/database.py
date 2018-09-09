import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'opio'
        self.password = 'adminsteve'
        self.database = 'level_up'

        try:
            #print "Using psycopg2…"
            self.myConnection = psycopg2.connect( host=self.hostname, user=self.username, password=self.password, dbname=self.database )
            
        except:
            print('failed to connect to db')

    # Simple routine to run a query on a database and print the results:
    def doQuery(self) :
        cur = self.myConnection.cursor()

        cur.execute( "SELECT firstname, lastname FROM UserEvents.test" )

        for firstname, lastname in cur.fetchall() :
            print (firstname, lastname)
    
    def create_user(self):
        
        sql = "INSERT INTO Users(user_id,first_name,last_name,age,email,password,Created_at) VALUES (1, 'Paul','Musa', 32, 'pmusa@gmail', 'musa',DEFAULT)"
        try:

            cur = self.myConnection.cursor()
            # execute the INSERT statement
            cur.execute(sql)
             # commit the changes to the db
            self.myConnection.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_into_event(self):
        
        sql = "INSERT INTO Event(event_id,event_name,location,price) VALUES (1, 'john and mary wedding day','kampala', 15000)"
        try:

            cur = self.myConnection.cursor()
            # execute the INSERT statement
            cur.execute(sql)
             # commit the changes to the db
            self.myConnection.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_into_Ticket(self):
        
        sql = "INSERT INTO Ticket(Ticket_id,event_id,user_id,is_valid,verification_code,created_at) VALUES (1, 1,1,'yes','07kla', DEFAULT)"
        try:

            cur = self.myConnection.cursor()
            # execute the INSERT statement
            cur.execute(sql)
             # commit the changes to the db
            self.myConnection.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self):

        # create tables in the level_up database
        commands = (
            """
            CREATE TABLE Users(
                user_id INTEGER PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                age VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                Created_at VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP
            
            )
            """,
            """ CREATE TABLE Event (
                    event_id INTEGER PRIMARY KEY,
                    event_name VARCHAR(255) NOT NULL,
                    price VARCHAR(255) NOT NULL,
                    location VARCHAR(255) NOT NULL
                    )
            """,
           
            """
            CREATE TABLE Ticket (
                    Ticket_id INTEGER PRIMARY KEY,
                    event_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    is_valid VARCHAR(255) NOT NULL,
                    verification_code VARCHAR(255) NOT NULL,
                    Created_at VARCHAR(255)  NOT NULL DEFAULT CURRENT_TIMESTAMP,                    
                    FOREIGN KEY (user_id)
                        REFERENCES Users (user_id)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (event_id)
                        REFERENCES Event (event_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
            )
            """)
        try:
            cur = self.myConnection.cursor()
            # create table one at a time
            for command in commands:
                cur.execute(command)
            # close communication with the level_up database server
            cur.close()
            # commit the changes
            self.myConnection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.myConnection is not None:
                self.myConnection.close()
        
    
       
        
    

    

    


    
    