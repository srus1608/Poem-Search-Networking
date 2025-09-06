# 📝 Networking Poem Search Project (Client-Server with XML & Sockets)

This project demonstrates a simple networking application in Python using **socket programming** and **XML data exchange**.
It allows a user (client) to input a word, which is then sent to a server. The server searches that word in a poem, cleans the text, and sends matching lines back in **XML format**. 
The client receives and parses the XML, displaying the results in a structured format.


## 📁 Project Structure

├── poem.txt # Poem source file
├── poem.py # Handles reading, cleaning, and XML formatting
├── server.py # Receives word, finds matches, sends XML
├── client.py # Sends word, receives XML, parses & displays
└── README.md # Project documentation

## 💡 Features

- Socket-based communication between client and server
- Dynamic search of any word entered by the client
- Text cleaning using regex (3 different Python approaches)
- Data sent in structured XML format
- XML parsing using `xml.dom.minidom`
- Graceful handling of "no match" scenarios

## 📌 Technologies Used

- Python 3
- Socket Programming (`socket`)
- Regular Expressions (`re`)
- XML Parsing (`xml.dom.minidom`)

  ## 🚀 How to Run

### 1. Clone the repository

git clone https://github.com/srus1608/poem-search-networking.git
cd poem-search-networking  

## Open two terminals:
Terminal 1 – Start the server:
python server.py

Terminal 2 – Start the client:
python client.py


Then enter the word you want to search for.
you will get the output.
