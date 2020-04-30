from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Survey(Base):
    __tablename__='survey'
    id = Column(Integer, primary_key=True)
    radio_question1 = Column(Integer, nullable=False, default=0)
    radio_question2 = Column(Integer, nullable=False, default=0)
    radio_question3 = Column(Integer, nullable=False, default=0)
    radio_question4 = Column(Integer, nullable=False, default=0)
    radio_question5 = Column(Integer, nullable=False, default=0)
    check_question1 = Column(String, nullable=False)
    subjective_question1 = Column(String, nullable=False)
    subjective_question2 = Column(String, nullable=False)

    def __init__(self, radio_question1, radio_question2,
                 radio_question3, radio_question4, radio_question5, check_question1,
                 subjective_question1, subjective_question2):
        self.radio_question1=radio_question1
        self.radio_question2=radio_question2
        self.radio_question3=radio_question3
        self.radio_question4=radio_question4
        self.radio_question5=radio_question5
        self.check_question1=check_question1
        self.subjective_question1=subjective_question1
        self.subjective_question2=subjective_question2





