import socket
from poem import Poem

server_socket = socket.socket()

host = '127.0.0.1'
port = 5656

server_socket.bind((host,port))
server_socket.listen(1)
print(f"server is listening on {host} {port}")

while True:
    conn,addr = server_socket.accept()
    print(f"connected to client at {addr}")

    word_bytes = conn.recv(1024)
    search_word = word_bytes.decode('utf-8').strip()
    print(f"Searching for word -> '{search_word}'")

    # word = conn.recv(1024).decode()
    # print(f"seraching for word -> {word} ")

    p=Poem("poem.txt")

    p.clean_with_enumerator()
    # p.clean_with_list_comp()
    # p.clean_with_map()

    xml_data = p.get_lines(search_word)
    print("xml prepared")

    conn.sendall(xml_data.encode("utf-8"))
    print("xml send the dta to client")

    conn.close()