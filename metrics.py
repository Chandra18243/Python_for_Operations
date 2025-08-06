import psutil
import json
from datetime import datetime

def get_server_metrics_py():
    # Collect memory, swap, and disk I/O only once
    vmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk_io = psutil.disk_io_counters()

    metrics = {
        "timestamp": datetime.now().isoformat(),
        "cpu": {
            "usage_percent": psutil.cpu_percent(interval=1),
            "core_count": psutil.cpu_count(logical=False),
            "logical_processors": psutil.cpu_count(logical=True),
        },
        "memory": {
            "usage_percentage": round((vmem.used / vmem.total) * 100, 2),
            "available_percentage": round((vmem.available / vmem.total) * 100, 2),
        },
        "swap": {
            "usage_percentage": round((swap.used / swap.total) * 100, 2) if swap.total > 0 else 0,
            "free_percentage": round((swap.free / swap.total) * 100, 2) if swap.total > 0 else 0,
        },
        "disk_io": {
            "read_mb": round(disk_io.read_bytes / (1024 * 1024), 2),
            "write_mb": round(disk_io.write_bytes / (1024 * 1024), 2),
        }
    }
    return metrics

if __name__ == "__main__":
    metrics = get_server_metrics_py()
    output_json = json.dumps(metrics, indent=4)

    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = f"/var/server_metrics_{date_str}.json"

    try:
        with open(log_file, "w") as f:
            f.write(output_json)
        print(f"Server metrics written to {log_file}")
    except Exception as e:
        print(f"Failed to write metrics: {e}")