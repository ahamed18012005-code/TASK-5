
from pathlib import Path

# Path to the sample email
EMAIL_FILE = Path("samples/mock_phishing_email.txt")


def detect_phishing(email_text):
    """Check a sample email for common phishing indicators."""

    text = email_text.lower()
    alerts = []

    # Check for urgent or threatening language
    urgent_words = ["urgent", "immediately", "suspension"]

    if any(word in text for word in urgent_words):
        alerts.append("Urgent or threatening language detected")

    # Check for account verification requests
    verification_phrases = [
        "verify your account",
        "account requires"
    ]

    if any(phrase in text for phrase in verification_phrases):
        alerts.append("Account verification request detected")

    # Check whether the email contains a URL
    if "http://" in text or "https://" in text:
        alerts.append("URL detected in the email")

    return alerts


def main():
    if not EMAIL_FILE.exists():
        print(f"Error: Sample email not found: {EMAIL_FILE}")
        return

    email_text = EMAIL_FILE.read_text(encoding="utf-8")

    print("=" * 50)
    print("       PHISHAWARE - PHISHING EMAIL DETECTOR")
    print("=" * 50)

    alerts = detect_phishing(email_text)

    if alerts:
        print("\nPotential phishing indicators found:\n")

        for number, alert in enumerate(alerts, start=1):
            print(f"{number}. {alert}")

        print("\nResult: Manual review recommended.")
    else:
        print("\nNo configured phishing indicators detected.")

    print("\nNote: These indicators alone do not prove an email")
    print("is phishing. Verify the sender and links manually.")


if __name__ == "__main__":
    main()
