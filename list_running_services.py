import subprocess
import shlex

def get_running_services():
    # Run systemctl to list active services without header/legend
    result = subprocess.run(
        ['systemctl', 'list-units', '--type=services', '--no-legend'],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error running systemctl: {result.stderr}")
        return []

    output = result.stdout.strip()
    services = []

    for line in output.split('\n'):
        words = shlex.split(line)
        if not words:
            continue
        # Extract first word, remove '.service' suffix
        service_name = words[0].split('.')[0]
        services.append(service_name)

    return services

if __name__ == "__main__":
    services = get_running_services()
    for svc in services:
        print(svc)
