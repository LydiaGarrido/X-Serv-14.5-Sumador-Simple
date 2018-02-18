#!/usr/bin/python3

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""
import calculadora
import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)


try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        request = str(recvSocket.recv(2048), 'utf-8')
        resource = request.split()[1]
        print(resource)
        
               
        try:
            _, operando1, operacion, operando2 = resource.split('/')
            operando1 = float(operando1)
            operando2 = float(operando2)
            solucion = calculadora.funciones[operacion](operando1, operando2)
            respuesta = ("El resultado de la " +operacion+ " de " +str(operando1)+ 
                        " y " +str(operando2)+ " es: " +str(solucion))
        except ValueError:
            respuesta = "No estan permitidos tipos que no sean numericos y debe ser /operando1/operacion/operando2"
        except KeyError:
            respuesta = "Las operaciones permitidas son: suma, resta, multiplicacion, division y elevacion"
        except ZeroDivisionError:
            respuesta = "No esta permitido dividir entre cero"

        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola.</h1>" +
                        "<p>" + respuesta +
                        "</p></body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
