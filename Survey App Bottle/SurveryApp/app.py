from views import success, index, submit_survey, engine
from models import Survey, Base
from sqlalchemy.ext.declarative import declarative_base
from bottle.ext import sqlalchemy


from bottle import Bottle, run, debug

app = Bottle()

Base.metadata.create_all(engine)


plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

app.install(plugin)


if __name__=='__main__':
    debug(True)
    run()