import responder
from calc import Calc

api = responder.API()


@api.route("/")
def index(req, resp):
    resp.html = api.template('index.html')


@api.route("/calc")
async def calc(req, resp):
    data = await req.media()

    arg1 = int(data.get('arg1'))
    arg2 = int(data.get('arg2'))
    operator = data.get('operator')
    result = Calc.calc(arg1, arg2, operator)

    resp.html = api.template('result.html', arg1=arg1,
                             arg2=arg2, operator=operator, result=result)

if __name__ == '__main__':
    api.run(address="0.0.0.0")
