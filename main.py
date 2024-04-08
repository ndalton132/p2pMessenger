import Client
import Server
# main.py

import threading
import Server
import Client

def main():
    # Start the server in a separate thread
    server_thread = threading.Thread(target=Server.start_server)
    server_thread.start()

    # Start the client
    Client.start_client()
    
    

if __name__ == "__main__":
    main()
