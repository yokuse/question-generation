package ws

import "go.uber.org/zap"

// Hub maintains the set of active Clients and broadcasts messages to the
// Clients.
type Hub struct {
	// Registered Clients.
	Clients map[*Client]bool

	// Inbound messages from the Clients.
	Broadcast chan []byte

	// Register requests from the Clients.
	Register chan *Client

	// Unregister requests from Clients.
	Unregister chan *Client

	Log *zap.SugaredLogger
}

func NewHub(log *zap.SugaredLogger) *Hub {
	return &Hub{
		Broadcast:  make(chan []byte),
		Register:   make(chan *Client),
		Unregister: make(chan *Client),
		Clients:    make(map[*Client]bool),
		Log:        log,
	}
}

func (h *Hub) Run() {
	for {
		select {
		case client := <-h.Register:
			h.Log.Debugw("new client connected", "client", client.Ip())
			h.Clients[client] = true
		case client := <-h.Unregister:
			if _, ok := h.Clients[client]; ok {
				delete(h.Clients, client)
				close(client.Send)
			}
		case message := <-h.Broadcast:
			for client := range h.Clients {
				select {
				case client.Send <- message:
					h.Log.Debugw("sent message to client", "client", client.Ip(), "message", string(message))
				default:
					close(client.Send)
					delete(h.Clients, client)
				}
			}
		}
	}
}
