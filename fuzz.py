#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3:
    print("Usage: %s <TARGET_IP> <TARGET_PORT>" % sys.argv[0])
    sys.exit(1)

target_host = str(sys.argv[1])
target_ip = int(sys.argv[2])

buffer_strings = ["A" * 100]
addition = 100

# Create fuzzing strings in increments of 100
while len(buffer_strings) <= 50:
    buffer_strings.append("A" * addition)
    addition += 100

# Create connection to service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_ip))

# Try to crash the program with different length streams
for buffer in buffer_strings:
    # Fill this in with potentially vulnerable command, remove newline if needed
    attack_string = "USER: " + buffer + "\n"
    print("Sending buffer of length: %s" % len(buffer))
    s.send(attack_string)
    response = s.recv(1024)
    print("Response: %s" % response)