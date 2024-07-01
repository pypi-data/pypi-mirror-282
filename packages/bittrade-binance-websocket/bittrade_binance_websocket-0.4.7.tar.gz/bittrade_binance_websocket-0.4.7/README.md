# Binance Websocket

[NOT RELEASED] This is very much a work in progress, despite being on pypi.
Most things might be wrongly documented; API **will** change

## Features

- Reconnect with incremental backoff 
- Respond to ping
- request/response factories e.g. `add_order_factory` make websocket events feel like calling an API
- ... but provides more info than a simple request/response; 
  for instance, `add_order` goes through each stage submitted->pending->open or canceled, 
  emitting a notification at each stage

## Installing

`pip install bittrade-binance-websocket` or `poetry add bittrade-binance-websocket`

## General considerations

### Observables/Reactivex

The whole library is build with [Reactivex](https://rxpy.readthedocs.io/en/latest/).

Though Observables seem complicated at first, they are the best way to handle - and (synchronously) test - complex situations that arise over time, like an invalid sequence of messages or socket disconnection and backoff reconnects.

For simple use cases, they are also rather easy to use as shown in the [examples](./examples) folder or in the Getting Started below

### Concurrency

Internally the library uses threads.
For your main program you don't have to worry about threads; you can block the main thread.

## Getting started

### Connect to the public feeds

```python
from bittrade_huobi_websocket import public_websocket_connection, subscribe_ticker
from bittrade_huobi_websocket.operators import keep_messages_only, filter_new_socket_only

# Prepare connection - note, this is a ConnectableObservable, so it will only trigger connection when we call its ``connect`` method
socket_connection = public_websocket_connection()
# Prepare a feed with only "real" messages, dropping things like status update, heartbeat, etc…
messages = socket_connection.pipe(
    keep_messages_only(),
)
socket_connection.pipe(
    filter_new_socket_only(),
    subscribe_ticker('USDT/USD', messages)
).subscribe(
    print, print, print  # you can do anything with the messages; here we simply print them out
)
socket_connection.connect()
```

_(This script is complete, it should run "as is")_


## Logging

We use Python's standard logging.
You can modify what logs you see as follows:

```
logging.getLogger('bittrade_huobi_websocket').addHandler(logging.StreamHandler())
```

In addition, two special logger logs every message sent/received from the socket (except heartbeat) at the `DEBUG` level: `bittrade_huobi_websocket.raw_socket.sent` and `bittrade_huobi_websocket.raw_socket.received`

To view a full, timestamped history of the socket exchanges use

```
handler = FileHandler("logs/raw_socket.log")
handler.setLevel(DEBUG)
logger = logging.getLogger("bittrade_huobi_websocket.raw_socket.sent")
formatter = logging.Formatter("%(asctime)s.%(msecs)03d <== %(message)s", datefmt="%H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
handler = FileHandler("logs/raw_socket.log")
handler.setLevel(DEBUG)
logger = logging.getLogger("bittrade_huobi_websocket.raw_socket.received")
formatter = logging.Formatter("%(asctime)s.%(msecs)03d --> %(message)s", datefmt="%H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
```

## Private feeds

Similar to [bittrade-kraken-rest](https://github.com/TechSpaceAsia/bittrade-kraken-rest), this library attempts to get as little access to sensitive information as possible.

This means that you'll need to implement the signature token yourself. The library never has access to your API secret.

See `examples/sign.py` for an example of implementation but it is generally as simple as:

```python
authenticated_sockets = connection.pipe(
    filter_new_socket_only(),
    operators.map(add_token),
    operators.share(),
)
```

# Development guidelines

## `*_http` methods

REST functions over http should be suffixed with `_http` e.g. `get_book_http`.
They should return an Observable containing the *full* json body; this is easily achieved via `prepare_request` and `send_request`.

Where possible models should be defined to describe the *raw* result and *parsed result* if available/useful.

Reactive operators may be provided for parsing, but they should never be included in the *raw* functionality of the `*_http` function, only optional.

Any operator that maps to CCXT types should be suffixed with `_ccxt` e.g. `parse_book_ccxt`.