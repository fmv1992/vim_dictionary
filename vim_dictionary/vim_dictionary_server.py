"""Python server for the vim_dictionary application."""

import sys
import json
import os
import socket
import socketserver

import __init__ as vim_dictionary


HOST, PORT = 'localhost', 49158


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """Server that handles dictionary requests by vim and lookups."""

    tcpreqhan_logger = vim_dictionary.instantiate_logger('tcpreqhan')
    tcpreqhan_logger.debug("Initializing 'ThreadedTCPRequestHandler' class.")

    def handle(self):
        """Receive and send data from vim."""
        self.dictionary = vim_dictionary.get_dictionary()

        self.tcpreqhan_logger.debug("Started log in 'handle'.")
        while True:
            # Data receiving part.
            try:
                data = self.request.recv(4096).decode('utf-8')
                self.tcpreqhan_logger.debug(
                    "Got data: '{0}'.".format(repr(data)))
            except socket.error:
                self.tcpreqhan_logger.debug(
                    "Socket error: 'socket.error'.")
                break
            except IOError:
                self.tcpreqhan_logger.debug(
                    "Socket error: 'IOError'.")
                break
            if data == '':
                self.tcpreqhan_logger.debug("Socket error: 'empty data'.")
                break
            self.tcpreqhan_logger.debug(
                "Socket received: '{0}'.".format(repr(data)))
            try:
                decoded = map(lambda x: (int(x[0]), x[1]),
                              map(json.loads, data.splitlines()))
            except ValueError:
                self.tcpreqhan_logger.debug(
                    "Json decoding error: 'ValueError'.")
                break

            for code, content in decoded:
                self.tcpreqhan_logger.debug(
                    "Correctly decoded json. "
                    "Code: '{0}'. Content: '{1}'.".format(
                        code, content))

                # Send a response if the sequence number is positive.
                # Negative numbers are used for "eval" responses.
                if content == '!close':
                    self.tcpreqhan_logger.debug(
                        "Terminating ThreadedTCPRequestHandler.")
                    self.server.shutdown()
                    self.server.server_close()
                    return 1
                elif content == '!is_alive':
                    self.tcpreqhan_logger.debug("Send '!is_alive' signal.")
                    self.request.sendall('TRUE'.encode('utf-8'))
                elif code >= 0:
                    response = self.dictionary.lookup(content)
                    encoded = json.dumps([code, response])
                    # self.tcpreqhan_logger.info("Sleeping for 2 seconds.")
                    # time.sleep(2)
                    try:
                        self.request.sendall(encoded.encode('utf-8'))
                    except BrokenPipeError as exp:
                        print(exp)
                    self.tcpreqhan_logger.info(
                        "Sending: '{0}'.".format(encoded))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Base class to receive 'ThreadedTCPRequestHandler'."""

    allow_reuse_address = True

    pass


def check_server_is_on():
    """Check if server is online."""
    csio_logger = vim_dictionary.instantiate_logger('check_server_is_on')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        while True:
            try:
                csio_logger.debug('Trying to connect to socket.')
                sock.connect((HOST, PORT))
                break
            except ConnectionRefusedError:
                csio_logger.debug('Got a ConnectionRefusedError exception.')
                return False
        csio_logger.debug('Connected.')
        message = json.dumps(['-1', '!is_alive'])
        sock.sendall(bytes(message, 'utf8'))
        response = str(sock.recv(1024), 'ascii')
        if response == 'TRUE':
            csio_logger.debug('Server is alive.')
            return True
        else:
            csio_logger.debug('Server is not alive.')
            return False


if __name__ == '__main__':

    # Start logging.
    vim_dictionary.setup_logging()
    server_logger = vim_dictionary.instantiate_logger(
        os.path.basename(__file__).strip('.py'))
    server_logger.debug('Is inside main.')
    server_logger.debug(
        "Was initialized with arguments: '{0}'".format(' '.join(sys.argv)))

    # Instantiate server.
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_logger.debug("Listening on port {0}".format(PORT))

    # Start server.
    server.serve_forever()

    # Finish server gracefully.
    server_logger.debug("Finished '{0}'.".format(__file__))
    server.shutdown()
