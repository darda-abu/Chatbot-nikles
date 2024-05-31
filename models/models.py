from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_query: str


class ChatResponse(BaseModel):
    answer: str
    
class database:
     def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
