package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

// SocketHandler handles WebSocket connections
func SocketHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	vars := mux.Vars(r)
	socketID := vars["id"]

	// Store the WebSocket connection with the provided ID
	sockets[socketID] = conn

	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			fmt.Println(err)
			return
		}

		// Handle incoming messages as needed
		fmt.Printf("Received message from socket %s: %s\n", socketID, string(p))

		// Broadcast the message to all clients except the sender
		for id, socket := range sockets {
			if id != socketID {
				err := socket.WriteMessage(messageType, p)
				if err != nil {
					fmt.Println(err)
					return
				}
			}
		}
	}
}

// OpenSocketHandler opens a new WebSocket with a specific ID
func OpenSocketHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	socketID := vars["id"]

	if _, exists := sockets[socketID]; exists {
		http.Error(w, "Socket ID already in use", http.StatusBadRequest)
		return
	}

	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println(err)
		http.Error(w, "Failed to open socket", http.StatusInternalServerError)
		return
	}
	defer conn.Close()

	sockets[socketID] = conn

	fmt.Printf("Opened socket with ID: %s\n", socketID)
	w.WriteHeader(http.StatusOK)
}

var sockets = make(map[string]*websocket.Conn)

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/socket/{id}", SocketHandler)
	r.HandleFunc("/open-socket/{id}", OpenSocketHandler)

	http.Handle("/", r)

	port := ":8080"
	fmt.Printf("Server is listening on port %s...\n", port)
	http.ListenAndServe(port, nil)
}
