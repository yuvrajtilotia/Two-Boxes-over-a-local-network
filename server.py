from base64 import encode
import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.10.23"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server initialised. Waiting for connection... \n")

players = [Player(0, 0, 50, 50, (255, 255, 255)), Player(100, 100, 50, 50, (255, 0, 0))]

def t_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(8192))
            players[player] = data
            if not data:
                print("Disconnected \n")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Receiving data : ", data)
                print("Sending data : ", reply)
            
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Connection Lost \n")
    conn.close()

playerCount = 0
while True:
    conn, addr = s.accept()
    print("New connection : \n", addr)
    start_new_thread(t_client, (conn, playerCount))
    playerCount += 1
    print("Total Player Count = \n", playerCount)
