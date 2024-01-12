# WebSocket Server Setup Guide

This guide will help you set up and run the WebSocket server written in Go.

## Prerequisites

Make sure you have the following installed on your system:

- [Go](https://golang.org/doc/install)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Setup Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies:**

   ```bash
   go get -u github.com/gorilla/mux
   go get -u github.com/gorilla/websocket
   ```

3. **Run the Server:**
   ```bash
   go run main.go
   ```

## Usage

### Open a New WebSocket

- **Endpoint:** `POST /open-socket/{id}`
  - Open a new WebSocket with a specific ID.
  - Example:
    ```bash
    curl -X POST http://localhost:8080/open-socket/mysocketid
    ```

### Connect to a WebSocket

- **Endpoint:** `GET /socket/{id}`
  - Connect to an existing WebSocket with the provided ID.
  - Example:
    ```bash
    // Use a WebSocket client, browser, or a tool like `websocat` to connect.
    websocat ws://localhost:8080/socket/mysocketid
    ```

### Send a Message to a WebSocket

- **Endpoint:** `POST /send-message/{id}`
  - Send a message to a specific WebSocket.
  - Example:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello"}' http://localhost:8080/send-message/mysocketid
    ```

Make sure to replace `{id}` with the desired socket ID in the examples.

The server will print received messages and handle communication between connected sockets.
