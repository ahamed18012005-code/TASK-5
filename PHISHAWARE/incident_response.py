
from datetime import datetime
from pathlib import Path

# Evidence log location
LOG_FILE = Path("evidence/incident-response-log.txt")


def main():
    # Create the evidence directory if necessary
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    steps = [
        ("Detection", "A suspicious sample email was identified."),
        ("Analysis", "The email was checked for common phishing indicators."),
        ("Containment", "The sample was isolated for safe analysis."),
        ("Eradication", "The simulated malicious message was marked for removal."),
        ("Recovery", "The simulated system was considered ready for normal use."),
        ("Lessons Learned", "Email verification and user awareness were recommended.")
    ]

    print("=" * 55)
    print("       PHISHAWARE - INCIDENT RESPONSE SIMULATION")
    print("=" * 55)
    print(f"Timestamp: {timestamp}\n")

    log_lines = [
        "PHISHAWARE - INCIDENT RESPONSE LOG",
        f"Timestamp: {timestamp}",
        "-" * 45
    ]

    for number, (stage, description) in enumerate(steps, start=1):
        message = f"{number}. {stage}: {description}"
        print(message)
        log_lines.append(message)

    log_lines.append("\nSimulation completed successfully.")
    log_lines.append(
        "No real accounts, credentials, or systems were accessed."
    )

    LOG_FILE.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    print("\nSimulation completed successfully.")
    print(f"Evidence log saved to: {LOG_FILE}")
    print("This is a simulation; no real system was modified.")


if __name__ == "__main__":
    main()
