import math

def password_strength(password):

  # Scoring system
  scores = {
    "length": 2,
    "uppercase": 2,
    "lowercase": 2,
    "number": 2,
    "special": 2,
  }

  # Entropy calculation
  entropy = 0

  # Criteria check
  criteria = {
    "length": len(password) >= 8,
    "uppercase": any(char.isupper() for char in password),
    "lowercase": any(char.islower() for char in password),
    "number": any(char.isdigit() for char in password),
    "special": any(not char.isalnum() and not char.isspace() for char in password),
  }

  # Calculate entropy
  total_characters = sum(criteria.values())
  if total_characters > 0:
    entropy = math.log2(total_characters**len(password))

  # Evaluate resistance to brute force attacks
  brute_force_resistance = scores["length"] * len(password) * total_characters

  # Display score and feedback
  score = sum(scores[feature] for feature, meets_criteria in criteria.items() if meets_criteria)
  print("Password Score:", score)

  if score < 6:
    print("Weak")
  elif score < 10:
    print("Moderate")
  else:
    print("Strong")

  # Display entropy and resistance information
  print("Entropy:", entropy)
  print("Brute Force Resistance:", brute_force_resistance)

  # Optionally, provide additional feedback
  if not criteria["length"]:
    print("Password should be at least 8 characters long.")
  if not criteria["uppercase"]:
    print("Password should contain at least one uppercase letter.")
  if not criteria["lowercase"]:
    print("Password should contain at least one lowercase letter.")
  if not criteria["number"]:
    print("Password should contain at least one number.")
  if not criteria["special"]:
    print("Password should contain at least one special character.")


# Get user input
password = input("Enter a password: ")

# Check password strength
password_strength(password)
