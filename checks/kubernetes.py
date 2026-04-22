import subprocess

def check_kubernetes():
    try:
        output = subprocess.run(['kubectl', 'get',  'pods', '--all-namespaces'], 
        capture_output=True , text=True)
        results = {
            "kubectl_available": output.returncode == 0,
            "output": output.stdout 
        }
        return results
    except FileNotFoundError:
        results = {
            "kubectl_available": False,
            "output": "kubectl not found"
        }
        return results