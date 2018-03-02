# !/usr/bin/python3
# https://serverfault.com/questions/899551/why-does-this-url-with-excessive-preceding-dots-resolve-to-an-ip-address
import socket


class URLTrick:
    def __init__(self, url):
        self.url = url
        self.domain = self.url.split('//')[1].split('www.')[-1].split('/')[
            0]
        self.path = self.url.split(self.domain)[-1]
        self.site_ip = socket.gethostbyname(self.domain)

    def ip_octets_to_hex(self):
        hex_url = ''
        for octet in self.site_ip.split('.'):
            hex_rep = hex(int(octet)).split('0x')[-1]
            if len(hex_rep) == 1:
                hex_rep = f'0{hex_rep}'
            hex_url += hex_rep
        return hex_url.upper()

    def build_url(self):
        decimal_from_hex_octets = int(self.ip_octets_to_hex(), 16)
        print(f'{self.url} ->')
        print(
            f'{self.url.split("//")[0]}//{decimal_from_hex_octets}{self.path}')


URLTrick('https://people.rit.edu/zdw7287/').build_url()
