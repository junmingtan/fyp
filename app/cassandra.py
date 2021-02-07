from cassandra.cluster import Cluster

class Casssandra:
    def __init__(self):
        self.cluster = Cluster(['192.168.201.1', '192.168.202.1', '192.168.203.1'])
        self.session = self.cluster.connect()
        self.session.set_keyspace('testspace')

    def get_questions(self):
        rows = self.session.execute('SELECT userid, email, name FROM users')
        results = []
        for row in rows:
            results.append(row.name)
        return results
    
    def create_question(self, question):
        self.session.execute(
            """
            INSERT INTO users (userid, email, name)
            VALUES (%s, %s, %s)
            """,
            (uuid.uuid1(), 'email', question)
        )

cassandra = Casssandra()



