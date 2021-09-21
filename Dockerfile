FROM python:2

ADD tx_UDP_v2.py /


CMD [ "python", "./tx_UDP_v2.py" ]
