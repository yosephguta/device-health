import subprocess

def check_audio():
    try:
        output = subprocess.run(['systemctl', 'is-active', 'pipewire'], capture_output=True , text=True)
        results = {
            "pipewire_active": output.returncode == 0,
            "output": output.stdout,
        }
        return results
    except FileNotFoundError:
        results = {
            "pipewire_active": False,
            "output": "Pipewire not found"
        }
    return results