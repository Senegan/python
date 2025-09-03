import pywhatkit

EMERGENCY_CONTACTS = ["+91xxxxx","+91xxxxxxx"]  # Add multiple numbers if needed

# Function to send an emergency WhatsApp alert instantly
def send_emergency_alert():
    message = "hi welcom to whatsapp"
    
    for contact in EMERGENCY_CONTACTS:
        print(f"Sending WhatsApp emergency alert to {contact}...")
        pywhatkit.sendwhatmsg_instantly(contact, message)
    return
send_emergency_alert()