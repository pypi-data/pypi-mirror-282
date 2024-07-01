import dataclasses
from logging import getLogger
from typing import Callable
from uuid import uuid4
from reactivex import Observable, compose, operators
from bittrade_binance_websocket.events.request_response import wait_for_response
from bittrade_binance_websocket.models.enhanced_websocket import EnhancedWebsocket
from bittrade_binance_websocket.models.message import UserFeedMessage

from bittrade_binance_websocket.models.response_message import ResponseMessage

logger = getLogger(__name__)

@dataclasses.dataclass
class PingRequest:
  method: str
  id: str


def ping(
    messages: Observable[ResponseMessage]
  ) -> Callable[[Observable[EnhancedWebsocket]], Observable[ResponseMessage]]:
  def socket_to_event_messages(
    socket: EnhancedWebsocket
  ) -> Observable[ResponseMessage]:
      request_id = str(uuid4())
      ping_request = PingRequest(method="ping", id=request_id)
      
      logger.info(f'ping request, {ping_request}')
      logger.info(socket)

      socket.send_message(ping_request)
      return messages.pipe(
        wait_for_response(request_id, 5.0),
        operators.do_action(lambda x: logger.info(x))
      )
  
  return compose(
    operators.flat_map(socket_to_event_messages)
  )