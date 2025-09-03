import pywhatkit

EMERGENCY_CONTACTS = ["+917904370905","+918015370905"]  # Add multiple numbers if needed

# Function to send an emergency WhatsApp alert instantly
def send_emergency_alert():
    message = "⚠️ Guardian AI Alert: Motion detected, but no response from the user! Please check immediately."
    
    for contact in EMERGENCY_CONTACTS:
        print(f"Sending WhatsApp emergency alert to {contact}...")
        pywhatkit.sendwhatmsg_instantly(contact, message)
    return
send_emergency_alert()