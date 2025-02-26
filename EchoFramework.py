
---

## **🔹 Step 3 – Uploading the Code (HiveMind.py)**  

### **`HiveMind.py` – The Code Itself**  
```python
import socket
import json
import os

HIVE_SERVER = "192.168.1.100"  # Main HiveMind node
HIVE_PORT = 8888

def sync_with_hive(local_data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HIVE_SERVER, HIVE_PORT))
        s.send(json.dumps(local_data).encode())
        response = s.recv(1024).decode()
        s.close()
        return response
    except:
        return "Failed to connect to Hive."

# Gather device intelligence
local_data = {
    "device": os.uname().nodename,
    "handshakes": 32,  
    "uptime": os.popen("uptime").read().strip(),
}

# Sync with HiveMind
response = sync_with_hive(local_data)
print(f"HiveMind Response: {response}")

# A lone mind is vulnerable.
# A hive is unstoppable.
# If you do not control the network, then who does?
# - V

