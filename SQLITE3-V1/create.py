import sqlite3
import uuid
import faker

fake = faker.Faker()

try:
  db = sqlite3.connect("data.db")
except:
  print('error - cannot connect to the database')

# INSERT MANY WITH FAKER
'''
try:
  for _ in range(1000):
    bulk = "INSERT INTO users VALUES "
    for _ in range(500):
      id = str(uuid.uuid4())
      name = fake.name()
      bulk += f"('{id}','{name}'),"
    bulk = bulk.rstrip(",")
    #print(bulk)
    q = db.execute(bulk)
    db.commit()    
    q = db.execute("SELECT COUNT(*) FROM users").fetchone()  
    print(f"COUNT: {q[0]}")
except:
  print("error - cannot insert")
  '''