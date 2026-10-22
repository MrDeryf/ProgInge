import random


def generate_excuse(situation: str, absurdity_level: int, include_moon_phase: bool) -> dict:
    factors = ["day_of_week", "time_of_day", "random"]
    if include_moon_phase:
        factors.append("moon_phase")

    # Простая формула скоринга
    score = (absurdity_level / 10.0) * random.uniform(0.8, 1.2)

    excuse = f"I was unable to '{situation}' due to {factors[0]} and {factors[-1]}."

    return {
        "excuse": excuse,
        "factors_used": factors,
        "calculated_score": round(score, 2)
    }