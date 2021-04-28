"""
 Implements a simple HTTP/1.0 Server

"""

import socket
from logger import get_logger
import configparser
config = configparser.ConfigParser()
config.read("/home/sweta/Sweta/myworks/toy-server-in-python/config.ini")
# Define socket host and port
print(config['SERVER'])
try:
    SERVER_HOST = config['SERVER']['SERVER_HOST']
    SERVER_PORT = config['SERVER']['SERVER_PORT']
    E_LOG = config['LOG_CONFIG']['error_log_path']
    O_LOG = config['LOG_CONFIG']['other_log_path']
except:
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    E_LOG = '/var/error.log'
    O_LOG = 'var/all.log'

error_logger = get_logger(E_LOG)
other_logger = get_logger(O_LOG)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, int(SERVER_PORT)))
server_socket.listen(1)
other_logger.debug('Listening on port %s ...' % SERVER_PORT)
while True:
    # Wait for client connections
    try:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        other_logger.info("Getting request ...")
        other_logger.debug(request)
        
        response = 'HTTP/1.0 200 OK\n\nHello World'
        client_connection.sendall(response.encode())
        other_logger.info("Sending response ...")
        client_connection.close()

    except Exception as e:
        error_logger.error(str(e))

# Close socket
server_socket.close()