from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

import time

class Casssandra:
    def __init__(self):
        self.cluster = Cluster(['192.168.201.1', '192.168.202.1', '192.168.203.1'])
        self.session = self.cluster.connect()
        self.session.set_keyspace('testspace')

    def get_questions(self):
        query = SimpleStatement('SELECT qid, user, question_text FROM questions', consistency_level=ConsistencyLevel.QUORUM)
        rows = self.session.execute(query)
        results = []
        for row in rows:
            results.append(row.question_text)
        return results
    
    def create_question(self, question):
        qid = str(round(time.time()*1000))
        self.session.execute(
            """
            INSERT INTO questions (qid, user, question_text)
            VALUES (%s, %s, %s)
            """,
            (qid, 'user', question)
        )

    def clear_questions(self):
        self.session.execute(
            """
            TRUNCATE questions
            """
        )

cassandra = Casssandra()



