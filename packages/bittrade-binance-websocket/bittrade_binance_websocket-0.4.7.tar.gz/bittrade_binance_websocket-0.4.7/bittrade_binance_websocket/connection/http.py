from ast import Attribute
from os import getenv
import os
from typing import Literal, TYPE_CHECKING
import requests
import reactivex
from reactivex.disposable import Disposable
from logging import getLogger

if TYPE_CHECKING:
    from bittrade_binance_websocket.models import RequestMessage, ResponseMessage

MARKET_URL = getenv("BINANCE_HTTP_MARKET_URL", "https://api.binance.com")

session = requests.Session()

logger = getLogger(__name__)


def generate_add_api_key(key: str):
    def _add_api_key(request: requests.models.Request):
        request.headers.update({"X-MBX-APIKEY": key})
        logger.debug(request.headers)
        return request

    return _add_api_key

class BinanceError(Exception):
    body: dict = {}

    def __init__(self, message: str, body: dict = {}):
        super().__init__(message)
        self.body = body

def prepare_request(message: "RequestMessage") -> requests.models.Request:
    http_method = message.method
    kwargs = {}
    # check if message params are set, if not, ignores
    if message.params:
        if http_method == "GET":
            kwargs["params"] = message.params
        else:
            kwargs["data"] = message.params

    # There are (few) cases where the endpoint must be a string; "handle" that below
    try:
        endpoint = message.endpoint.value
    except AttributeError:
        endpoint = message.endpoint
    return requests.Request(http_method, f"{MARKET_URL}{endpoint}", **kwargs)


def send_request(request: requests.models.Request) -> reactivex.Observable:
    def subscribe(
        observer: reactivex.abc.ObserverBase,
        scheduler: reactivex.abc.SchedulerBase | None = None,
    ) -> reactivex.abc.DisposableBase:
        response = session.send(request.prepare())
        if response.ok:
            try:
                body = response.json()
                observer.on_next(body)
                observer.on_completed()
            except Exception as exc:
                logger.error(
                    "Error parsing request %s; request was %s",
                    response.text,
                    response.request.body
                )
                observer.on_error(exc)
        else:
            try:
                logger.error(
                    "Error with request %s; request was %s",
                    response.text,
                    response.request.body
                )
                # Binance returns 400 with a message in the body
                if response.status_code == 400 and response.text:
                    observer.on_error(BinanceError(response.text, body=response.json()))
                else:
                    response.raise_for_status()
            except Exception as exc:
                observer.on_error(exc)
        return Disposable()

    return reactivex.Observable(subscribe)
