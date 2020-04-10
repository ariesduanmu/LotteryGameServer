# LotteryGameServer
simple lottery game server in Bottle

### Run Server

`python main.py`


### Client Test

`python test/test.py`

```
Method: POST

URL: http://127.0.0.1:8000/lottery

Args:

::parameter username:: your name
::parameter type:: str

Return:

::parameter username:: your name
::parameter type:: str

::parameter win:: 1 for win, 0 for lost
::parameter type:: int
```