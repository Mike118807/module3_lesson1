Initialization: We start with a dictionary service_tickets containing two sample tickets.

Open a New Ticket:

The open_ticket function takes a ticket_id, customer, and issue as inputs.

It checks if the ticket_id already exists. If not, it creates a new ticket with an open status.

Update Ticket Status:

The update_ticket_status function takes a ticket_id and a status.

It checks if the ticket_id exists. If it does, it updates the status; otherwise, it prints a message indicating the ticket was not found.

Display Tickets:

The display_tickets function can optionally filter tickets by status.

If no status is provided, it displays all tickets. If a status is provided, it displays only the tickets that match that status.

Testing:

We create a new ticket with open_ticket.

We update the status of an existing ticket with update_ticket_status.

We display all tickets and then specifically display only open tickets.