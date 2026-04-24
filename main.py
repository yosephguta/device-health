from checks.system import check_system
from checks.network import check_network
from checks.kubernetes import check_kubernetes
from checks.audio import check_audio
from reporter import generate_report, bundle_tarball

def main():
    print("Running device health checks...\n")

    results = {
        "system": check_system(),
        "network": check_network(),
        "kubernetes": check_kubernetes(),
        "audio": check_audio(),
    }

    report = generate_report(results)
    print(report)

    tarball_path = bundle_tarball(report)
    print(f"\nBundle saved to: {tarball_path}")

if __name__ == "__main__":
    main()