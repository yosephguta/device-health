import socket
import subprocess

def check_network():
    status = subprocess.run(['ping', '-c',  '1', '8.8.8.8',], 
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    local_ip = socket.gethostbyname(socket.gethostname())
    
    results = {
        "internet_connected": status.returncode == 0,
        "local_ip": local_ip,
    }
    return results