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


def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODONE: Fill sum with the correct value, based on the
    # args provided.
    args = map(int, args)
    sum = sum(args)

    return str(sum)

# TODONE: Add functions for handling more arithmetic operations.


def multiply(*args):
    """ Returns a STRING with the product of the arguments """

    product = 1

    for arg in args:
        product *= int(arg)

    return str(product)


def divide(*args):
    """ Returns a STRING with the quotient of the arguments """


    initial_dividend = int(args[0])
    initial_divisor = int(args[1])
    quotient = initial_dividend/initial_divisor

    for arg in args[2:]:
        quotient /= int(arg)

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
    path = path.split('/')
    func = path[0]
    args = path[1:]

    return func, args

def application(environ, start_response):
    # TODO: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #
    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    pass

if __name__ == '__main__':
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    pass
