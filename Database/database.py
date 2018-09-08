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

   
       
        
    

    

    


    
    