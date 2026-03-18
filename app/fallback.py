def fallback_process(text: str):
    text_lower = text.lower()

    if "otp" in text_lower or "bank" in text_lower:
        category = "Phishing"
        actions = [
            "Do not share OTP",
            "Contact your bank",
            "Enable 2FA"
        ]
    elif "stolen" in text_lower or "theft" in text_lower:
        category = "Theft"
        actions = [
            "Report to police",
            "Secure premises",
            "Alert neighbors"
        ]
    else:
        category = "General Alert"
        actions = ["Stay cautious"]

    summary = text[:100] if text else "No description provided"

    return {
        "category": category,
        "summary": summary,
        "actions": actions
    }