import socket
import time

# Hard code data
data = [
    {'Ogi': {'IP': 'IP', 'PORTS': [10, 11, 12, 13]}},
    {'Name two': {'IP': '192.168.168.2', 'PORTS': [10, 11, 12, 13]}},
]


class KnockKnock:
    '''
        Through data info, generate socket
    '''
    def __init__(self, data):
        self.data = data

    def show_what_you_need(self):
        ''' Ask which server do you need '''
        for key, info in enumerate(self.data):
            print(key, list(info.keys())[0])

    def get_from_param(self, option):
        """
        Construct params, return ip and ports
        :param option: int
        :return: IP: str, Ports [int]
        """
        IP = ''
        PORTS = []
        for key, value in self.data[option].items():
            IP = value['IP']
            PORTS = value['PORTS']
        return str(IP), PORTS

    @staticmethod
    def socket_start(IP, PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.setblocking(False)
            try:
                client.connect((IP, PORT))
            except socket.error:
                pass

    def generate_socket(self, option):
        IP, PORTS = self.get_from_param(option)
        for p in PORTS:
            self.socket_start(IP, p)
            time.sleep(1)


if __name__ == '__main__':
    knock = KnockKnock(data)
    knock.show_what_you_need()
    input_server_name = int(input("Enter which server you need :"))
    knock.generate_socket(input_server_name)
    print('All is done')
