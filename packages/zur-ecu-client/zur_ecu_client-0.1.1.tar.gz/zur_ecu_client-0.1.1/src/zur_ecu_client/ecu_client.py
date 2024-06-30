import json
import logging
import sched
import time
from threading import Thread
from typing import Union

from zur_ecu_client.senml.senml_msg_dv import SenmlNames, Dv
from zur_ecu_client.udp_server import UdpServer
from zur_ecu_client.messages import Messages


class EcuClient:

    def __init__(
        self, listener, ecu_ip: str, ecu_port: int, calls_per_second: int
    ) -> None:
        logging.basicConfig(level=logging.CRITICAL)
        self.listener = listener
        self.requestInterval = 1.0 / calls_per_second
        self.subscriptions: dict[SenmlNames, list[callable]] = {}
        self.compiledMessages = []

        self.ecuIP = ecu_ip
        self.ecuPort = ecu_port

        self.udpServer = UdpServer("127.0.0.1", 9000, ecu_ip, ecu_port)

        self.thread1 = Thread(target=self.__receive_msg)
        # self.thread1.daemon = True
        self.thread2 = Thread(target=self.__schedule_requests)
        # self.thread2.daemon = True

    def start(self):
        self.thread1.start()
        self.thread2.start()

    def subscribe(self, data_field: Union[SenmlNames, str], subscriber: callable):
        if type(data_field) is not SenmlNames and SenmlNames(data_field):
            data_field = SenmlNames(data_field)
        if data_field in self.subscriptions:
            self.subscriptions.get(data_field).append(subscriber)
        else:
            self.subscriptions[data_field] = [subscriber]
        self.__compile_subscriptions()

    def unsubscribe(self, data_field: Union[SenmlNames, str], subscriber: callable):
        if data_field in self.subscriptions:
            self.subscriptions.get(data_field).remove(subscriber)
            if not self.subscriptions[data_field]:
                self.subscriptions.pop(data_field)
            self.__compile_subscriptions()

    def unsubscribe_all(self):
        self.subscriptions = {}
        self.__compile_subscriptions()

    def send_msg(self, msg):
        if not msg:
            return
        msg = json.dumps(msg)
        self.udpServer.send_data(msg)

    def __compile_subscriptions(self):
        self.compiledMessages = []
        for key in self.subscriptions:
            parameters = key.value.split(":")
            new = {"bn": parameters[0], "n": parameters[1], "vs": parameters[2]}
            if new not in self.compiledMessages:
                self.compiledMessages.append(
                    {"bn": parameters[0], "n": parameters[1], "vs": parameters[2]}
                )

    def __receive_msg(self):
        while True:
            data = self.udpServer.receive_data()
            if data:
                senml = Messages.parse(data)
                self.listener(senml)
                logging.info(f"Received -> {senml}")

    def __request_messages(self):
        self.send_msg(self.compiledMessages)

    def __schedule_requests(self):
        scheduler = sched.scheduler(time.time, time.sleep)
        while True:
            scheduler.enter(self.requestInterval, 1, self.__request_messages, ())
            scheduler.run()


def __main__():
    # 2 ecu clients so we can have different calls per second
    mock_ecu_accu = EcuClient(None, "127.0.0.1", 9001, 1)
    mock_ecu_velo = EcuClient(None, "127.0.0.1", 9001, 1)
    msg = Dv.Ctrl(0, 0, 0, "Hello World!").get()

    try:
        mock_ecu_accu.start()
        mock_ecu_accu.subscribe("ECU:accu:sensor", None)  # Send a request to server
        mock_ecu_velo.start()
        mock_ecu_velo.subscribe("ECU:inverter:actual", None)

        # for item in msg:
        #     mock_ecu.compiledMessages.append(item)  # for sending data to server

    except KeyboardInterrupt:
        mock_ecu_accu.udpServer.close()
        mock_ecu_velo.udpServer.close()


if __name__ == "__main__":
    __main__()
