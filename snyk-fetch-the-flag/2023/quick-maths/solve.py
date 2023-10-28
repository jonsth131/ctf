#!/usr/bin/env python3
import socket

server_address = ('challenge.ctf.games', 31954)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)

    client_socket.send('Y'.encode('utf-8'))

    question = client_socket.recv(1024).decode('utf-8')
    print(question)
    while True:
        question = client_socket.recv(1024).decode('utf-8')

        if "Good bye" in question:
            break

        print(question)

        try:
            question_parts = question.split('?')
            question_text = question_parts[0]
            expression = question_parts[0].split("What is ")[1].strip()

            if '/' in expression:
                if '.' in expression:
                    answer = round(eval(expression), 1)  # Double division
                else:
                    answer = int(eval(expression))  # Integer division
            else:
                answer = round(eval(expression), 1)

            print("Answer", answer)
            client_socket.send(str(answer).encode('utf-8'))
        except:
            break

        result = client_socket.recv(1024).decode('utf-8')
        print(result)

finally:
    client_socket.close()
