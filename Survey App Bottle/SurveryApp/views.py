from bottle import Bottle, route, run, debug
from bottle import redirect, request, template, static_file
from models import Survey, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///survey.db", echo=True)
create_session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@route('/', method='GET')
def index():
    return template('survey.tpl')


@route('/submit_survey', method='POST')
def submit_survey():
    if request.method == 'POST':
        print('inside post')
        print(request)
        if request.POST.submit_survey:
            print('inside the submit survey')
            radio1 = request.POST.radio1.strip()
            radio2 = request.POST.radio2.strip()
            radio3 = request.POST.radio3.strip()
            radio4 = request.POST.radio4.strip()
            radio5 = request.POST.radio5.strip()
            check_answer = request.POST.check_answer.strip()
            subjective1 = request.POST.subjective1.strip()
            subjective2 = request.POST.subjective2.strip()
            survey = Survey(
                radio_question1=radio1,
                radio_question2=radio2,
                radio_question3=radio3,
                radio_question4=radio4,
                radio_question5=radio5,
                check_question1=check_answer,
                subjective_question1=subjective1,
                subjective_question2=subjective2
            )
            session = create_session()
            session.add(survey)
            session.commit()
            return success()
    return redirect('/')


def success():
    return template('success.tpl')