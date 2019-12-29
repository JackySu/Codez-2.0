# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       smtprox.py
#       Shouts to suidrewt
#
# ############################################# #
# This module allows Proxy support in MailFux.  #
# Shouts to Betrayed for telling me about       #
# http CONNECT                                  #
# ############################################# #
import smtplib
import socket
from sys import stderr


def recvline(sock):
    stop = 0
    line = ''
    while True:
        i = sock.recv(1)
        if i == '\n':
            stop = 1
        line += i
        if stop == 1:
            break
    return line


class ProxSMTP(smtplib.SMTP):
    def __init__(self,
                 host='',
                 port=0,
                 p_address='',
                 p_port=0,
                 local_hostname=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """Initialize a new instance.

        If specified, `host' is the name of the remote host to which to
        connect.  If specified, `port' specifies the port to which to connect.
        By default, smtplib.SMTP_PORT is used.  An SMTPConnectError is raised
        if the specified `host' doesn't respond correctly.  If specified,
        `local_hostname` is used as the FQDN of the local host.  By default,
        the local hostname is found using socket.getfqdn().

        """
        self.p_address = p_address
        self.p_port = p_port

        self.timeout = timeout
        self.esmtp_features = {}
        self.default_port = smtplib.SMTP_PORT
        if host:
            (code, msg) = self.connect(host, port)
            if code != 220:
                raise smtplib.SMTPConnectError(code, msg)
        if local_hostname is not None:
            self.local_hostname = local_hostname
        else:
            # RFC 2821 says we should use the fqdn in the EHLO/HELO verb, and
            # if that can't be calculated, that we should use a domain literal
            # instead (essentially an encoded IP address like [A.B.C.D]).
            fqdn = socket.getfqdn()
            if '.' in fqdn:
                self.local_hostname = fqdn
            else:
                # We can't find an fqdn hostname, so use a domain literal
                addr = '127.0.0.1'
                try:
                    addr = socket.gethostbyname(socket.gethostname())
                except socket.gaierror:
                    pass
                self.local_hostname = '[%s]' % addr
        smtplib.SMTP.__init__(self)

    def _get_socket(self, port, host, timeout):
        # This makes it simpler for SMTP_SSL to use the SMTP connect code
        # and just alter the socket connection bit.
        if self.debuglevel > 0:
            print(stderr, 'connect:', (host, port))
        new_socket = socket.create_connection((self.p_address, self.p_port),
                                              timeout)
        new_socket.sendall("CONNECT {0}:{1} HTTP/1.1\r\n\r\n".format(
            port, host))
        for x in range(2):
            recvline(new_socket)
        return new_socket
