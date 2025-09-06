import socket
import xml.dom.minidom


client_socket = socket.socket()

host="127.0.0.1"
port = 5656
client_socket.connect((host,port))

word = input("Enter word to search: \n").strip()
client_socket.sendall(word.encode("utf-8")) # sends to server
print(f"sent '{word}' to server")


xml_received = client_socket.recv(4096).decode('utf-8')
# print(xml_received)

dom = xml.dom.minidom.parseString(xml_received)
lines = dom.getElementsByTagName("line")

results =[]

for line in lines:
    number = line.getAttribute("number")
    text = line.firstChild.nodeValue
    results.append(f'{number},\" { text}"')



if results:
    print(f'"{word}"(' + "),(".join(results) + ")")
else:
    print("No such word is present")            

# print("), (".join(results) + ")")    
# print(results)

# print("Client received xml data :\n")
# print(xml_received)

client_socket.close()

# print("Client: Connection closed")

