import tarfile
import os
from datetime import datetime

def generate_report(results):
    lines = []
    lines.append("=" * 50)
    lines.append("DEVICE HEALTH DIAGNOSTIC REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)

    for section, data in results.items():
        lines.append(f"\n[ {section.upper()} ]")
        for key, value in data.items():
            lines.append(f"  {key}: {value}")

    lines.append("\n" + "=" * 50)
    return "\n".join(lines)

def bundle_tarball(report, output_dir="/tmp"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"/tmp/report_{timestamp}.txt"
    tarball_path = f"{output_dir}/device_health_{timestamp}.tar.gz"

    with open(report_path, "w") as f:
        f.write(report)

    with tarfile.open(tarball_path, "w:gz") as tar:
        tar.add(report_path, arcname=f"report_{timestamp}.txt")

    os.remove(report_path)
    return tarball_path