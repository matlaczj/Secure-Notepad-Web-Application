from password_strength import PasswordPolicy
from password_strength import PasswordStats

def getPasswordEntropyScore(pw):
    """
    Need a password that has minimum 30 entropy bits (the power of its alphabet).
    """
    policy = PasswordPolicy.from_names(
        entropybits=30
    )
    score = policy.test(pw)
    return score

def getPasswordStrengthScore(pw):
    """
    Complexity is a number in the range of 0.00..0.99. Good, strong passwords start at 0.66.
    """
    score = PasswordStats(pw).strength()
    score = round(score,2)
    return score