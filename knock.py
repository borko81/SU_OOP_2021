import socket
import time

data = [
    {'Name one': {'IP': '192.168.168.1', 'PORTS': [10, 11, 12, 13]}},
    {'Name two': {'IP': '192.168.168.2', 'PORTS': [10, 11, 12, 13]}},
]


def generate_url_with_port(MY_PORTS):
    for p in MY_PORTS:
        yield p


def generate_socket(IP, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.setblocking(False)
        try:
            client.connect((IP, port))
        except socket.error:
            pass


class KnockKnock:

    def __init__(self, data):
        self.data = data

    def show_what_you_need(self):
        for key, info in enumerate(self.data):
            print(key, list(info.keys())[0])

    def get_from_param(self, option):
        IP = ''
        PORTS = []
        for key, value in self.data[0].items():
            IP = self.data[0][key]['IP']
            PORTS = self.data[0][key]['PORTS']
        return str(IP), PORTS

    def generate_socket(self, option):
        IP, PORTS = self.get_from_param(option)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.setblocking(False)
            try:
                client.connect((IP, PORTS))
            except socket.error:
                pass


# print('knock... knock...')
# for res in generate_url_with_port(MY_PORTS):
#     generate_socket(IP, res)
#     time.sleep(1)

if __name__ == '__main__':
    knock = KnockKnock(data)
    knock.show_what_you_need()
    input_server_name = int(input("Enter which server you need :"))
    knock.generate_socket(input_server_name)
