"""
For your homework this week, you'll be creating a wsgi application of
your own.

You'll create an online calculator that can perform several operations.

You'll need to support:

  * Addition
  * Subtractions
  * Multiplication
  * Division

Your users should be able to send appropriate requests and get back
proper responses. For example, if I open a browser to your wsgi
application at `http://localhost:8080/multiple/3/5' then the response
body in my browser should be `15`.

Consider the following URL/Response body pairs as tests:

```
  http://localhost:8080/multiply/3/5   => 15
  http://localhost:8080/add/23/42      => 65
  http://localhost:8080/subtract/23/42 => -19
  http://localhost:8080/divide/22/11   => 2
  http://localhost:8080/               => <html>Here's how to use this page...</html>
```

To submit your homework:

  * Fork this repository (Session03).
  * Edit this file to meet the homework requirements.
  * Your script should be runnable using `$ python calculator.py`
  * When the script is running, I should be able to view your
    application in my browser.
  * I should also be able to see a home page (http://localhost:8080/)
    that explains how to perform calculations.
  * Commit and push your changes to your fork.
  * Submit a link to your Session03 fork repository!


"""
# import pysnooper

# @pysnooper.snoop()
def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODONE: Fill sum with the correct value, based on the
    # args provided.

    my_sum = sum(map(int,args))

    return str(my_sum)

# TODONE: Add functions for handling more arithmetic operations.

def subtract(*args):
    """ Returns a STRING with the difference of the arguments """


    a = int(args[0])
    b = int(args[1])
    difference = a - b

    return str(difference)

def multiply(*args):
    """ Returns a STRING with the product of the arguments """

    product = 1

    for arg in args:
        product *= int(arg)

    return str(product)


def divide(*args):
    """ Returns a STRING with the quotient of the arguments """


    dividend = int(args[0])
    divisor = int(args[1])
    quotient = int(dividend/divisor)

    return str(quotient)

def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """

    # TODONE: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.
    funcs = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    '': index
    }

    path = path.strip('/').split('/')
    func = path[0]
    func = funcs[func]

    args = path[1:]

    return func, args

def index():
    body = 'To perform calculations, enter the name operation you would like '
    body += 'to perform followed by a \\. Then enter the numbers you would like to perform'
    body += 'the operation on, separated by a \\'
    body += '\r\n'
    body += 'You may add, subtract, mulitply, and divide'
    return body

# @pysnooper.snoop()
def application(environ, start_response):
    # TODONE: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #
    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]

if __name__ == '__main__':
    # TODONE: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()