import psutil

def check_system():

    disk_stat = psutil.disk_usage('/')
    ram_stat = psutil.virtual_memory()

    results = {
        "disk_total": round(disk_stat.total / (1024 ** 3) , 2),
        "disk_used": round(disk_stat.used / (1024 ** 3) , 2),
        "disk_percent": round(disk_stat.percent, 2),
        "ram_total": round(ram_stat.total / (1024 ** 3) , 2),
        "ram_used": round(ram_stat.used / (1024 ** 3) ,2),
        "ram_percent": round(ram_stat.percent, 2),
    }

    
    return results