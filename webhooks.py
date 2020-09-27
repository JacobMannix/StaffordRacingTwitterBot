#!/home/mannix/anaconda3/bin/python
# # Jacob Mannix [08-31-2020]

# Webhook Function

# Import Dependencies
import requests

# Function
def webhookMessage(webhook_url, message_content):
    Message = {"content": message_content}
    requests.post(webhook_url, data=Message)
