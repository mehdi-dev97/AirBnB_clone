import uuid
class BaseModel:
    def __init__(self, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at
    
    def save():
        return 0
    
    def to_dict():
        return set.__dict__