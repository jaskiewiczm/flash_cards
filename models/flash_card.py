from sqlalchemy import Column, String, Integer

from database.database import database_instance


class FlashCard(database_instance.base):
    __tablename__ = 'flash_cards'

    id = Column('user_id', Integer, primary_key=True)
    question = Column('question', String(1024))
    answer = Column('answer', String(1024))

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_json(self):
        return dict(question=self.question, answer=self.answer)
