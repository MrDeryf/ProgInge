from backend.generator import generate_excuse


def test_generate_excuse_basic():
    result = generate_excuse("Meeting", 5, False)
    assert "excuse" in result
    assert "moon_phase" not in result["factors_used"]

def test_generate_excuse_with_moon():
    result = generate_excuse("Meeting", 5, True)
    assert "moon_phase" in result["factors_used"]