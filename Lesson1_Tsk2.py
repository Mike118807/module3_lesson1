# a system to track customer service tickets. Problem Statement: Develop a program that: Tracks customer service tickets, 
# each with a unique ID, customer name, issue description, and status (open/closed). Implement functions to: 
# Open a new service ticket. Update the status of an existing ticket. Display all tickets or filter by status. 
# Initialize with some sample tickets and include functionality for additional ticket entry.

# Initial setvice tickets

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


# Open New Ticket

def open_ticket(ticket_id, customer, issue):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open "}
        print(f"Ticket {ticket_id} opened for {customer} with issue: {issue}")
    else:
        print(f"Ticket {ticket_id} already exists. ")

# Function to update the status of an existing ticket

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}. ")
    else:
        print(f"Ticket {ticket_id} not found.")

# Display all tickets

def display_tickets(status=None):
    for ticket_id, ticket_info in service_tickets.items():
        if status is None or ticket_info["status"] == status:
            print(f"{ticket_id}: {ticket_info} ")

# Testing Functions

open_ticket("Ticket003", "Charlie", "Network issue ")
update_ticket_status("Ticket001", "closed")
display_tickets() # all tickets
print("\nOpen Tickets: ")
display_tickets("open") # only open tickets