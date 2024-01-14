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

func SocketHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		http.Error(w, "Failed to upgrade connection", http.StatusInternalServerError)
		return
	}
	defer conn.Close()

	socketID := mux.Vars(r)["id"]
	sockets[socketID] = conn

	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			fmt.Println(err)
			return
		}

		fmt.Printf("Received message from socket %s: %s\n", socketID, string(p))

		err = conn.WriteMessage(messageType, p)
		if err != nil {
			fmt.Println(err)
			return
		}
	}
}

func OpenSocketHandler(w http.ResponseWriter, r *http.Request) {
	socketID := mux.Vars(r)["id"]

	if _, exists := sockets[socketID]; exists {
		http.Error(w, "Socket ID already in use", http.StatusBadRequest)
		return
	}

	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
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

	port := ":8080"
	fmt.Printf("Server is listening on port %s...\n", port)
	http.ListenAndServe(port, r)
}
