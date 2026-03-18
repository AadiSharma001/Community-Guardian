from app.fallback import fallback_process

def test_happy_path():
    result = fallback_process("Fake OTP scam call")
    assert result["category"] == "Phishing"
    assert len(result["actions"]) > 0

def test_edge_case_empty():
    result = fallback_process("")
    assert result["summary"] == "No description provided"