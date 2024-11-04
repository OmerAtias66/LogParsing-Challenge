# Built by Omer Atias
import re

# Log entry to parse
log_entry = input("Please provide the log sample: ")
    ##"[2023-01-15T12:45:30] [INFO] [192.168.1.100] [Access Granted] [User: jdoe] [Resource: /admin-dashboard]"

# Regex pattern to match the log format
pattern = r"\[(\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2})\]\s\[(\w+)\]\s\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]\s\[([^\]]+)\]\s\[User:\s([^\]]+)\]\s\[Resource:\s([^\]]+)\]"

# Perform regex matching
match = re.match(pattern, log_entry)

# Check if there is a match
if match:
    # Extracted fields
    timestamp = match.group(1)
    log_level = match.group(2)
    ip_address = match.group(3)
    event_name = match.group(4)
    username = match.group(5)
    resource = match.group(6)

    # Output the captured groups
    print(f"Timestamp - {timestamp}")
    print(f"Severity - {log_level}")
    print(f"IP Address - {ip_address}")
    print(f"Event Name - {event_name}")
    print(f"Username - {username}")
    print(f"Resource - {resource}")
else:
    print("No match found in the log entry.")
