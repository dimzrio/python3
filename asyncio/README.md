### Asynchronous I/O

Ref:
~~~~
https://docs.python.org/3.8/library/asyncio.html
~~~~

Note: Python 3.7+

#### Coroutines
Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.

#### Tasks
Tasks are used to schedule coroutines concurrently.

#### Futures
A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.