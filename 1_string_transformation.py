booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """

booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()

parts = booking.split(' | ')

event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip = parts[5]

name_formatted = name.capitalize()
name_formatted = name_formatted.replace("_", "_")

room_formatted = room.upper()

email_domain = email.split('@')[1].lower()

vip_count = vip.count('VIP')

event_parts = event_code.split('-')
valid_event = event_parts[0] == 'EVT' and len(event_parts) == 2 and event_parts[1].isdigit()

valid_username = True
for ch in name:
    if not (ch.isalnum() or ch == '_'):
        valid_username = False
        break

room_parts = room.split('-')
valid_room = len(room_parts) == 2 and room_parts[1].isdigit()

time_parts = time.split(':')
valid_time = len(time_parts) == 2 and time_parts[0].isdigit() and time_parts[1].isdigit()

valid_email = '@' in email and '.' in email

print(f"Event code: {event_code}")
print(f"Name: {name_formatted}")
print(f"Room: {room_formatted}")
print(f"Time: {time}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_count}")
print(f"Valid event code: {valid_event}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")