def take_input():
    global username
    global filepath

    username = input("Enter the Username: ")
    password = input("Enter the Password: ")

    filepath = "A:\\BCA PART-3\\Project\\SkillSync (CyberSecurity)\\User Authentaction System\\data.txt"

    return username, password


def check_login(username, password, filepath):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                fields = line.strip().split(",")

                # Remove the newline character from the stored password
                stored_password = fields[1].strip()

                if fields[0] == username and stored_password == password:
                    return True

        print("User is not authenticated!")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False


# Example usage:
username, password = take_input()
if check_login(username, password, filepath):
    print("Authentication successful!")
else:
    print("Authentication failed. Please check your credentials.")
