import re


def is_valid_bc_license_plate(plate):
    """ Returns True if the plate is a valid BC license plate """
    pattern1 = "^[A-Z]{3}\d{3}$"
    pattern2 = "^\d{3}[A-Z]{3}$"
    pattern3 = "^[A-Z]{2}\d[ -]\d{2}[A-Z]$"
    regex = "%s|%s|%s" % (pattern1, pattern2, pattern3)

    if re.search(regex, plate):
        return True

    return False


def is_valid_python_variable_name(variable):
    """ Returns True if the variable is named in lower_snake_case"""

    if re.search("^[a-z_]{1,32}$", variable):
        if re.search("[a-z]+__[a-z]+", variable) is None:
            return True
    return False


def is_valid_email_address(email):
    """ Returns True if the email address matches the requirements"""

    email_data = re.split("@", email)
    username = email_data[0]
    domain_data = re.split("[.]", email_data[1])
    domain_name = domain_data[0]
    top_level_domain = domain_data[1]

    if re.search("^[a-zA-Z][a-zA-Z_]{0,255}$", username):
        if re.search("_$", username) is None:
            if re.search("^[a-zA-Z]{1,32}$", domain_name):
                if re.search("^[a-zA-Z]{2,5}$", top_level_domain):
                    return True
    return False


def is_valid_human_height(height):
    """ Returns True if the parameters match the height requirements """
    data = re.split("'", height)
    if len(data) != 2:
        return False

    feet = data[0]
    inches = data[1]

    if re.search("^[3-8]$", feet):
        if re.search("^((0?[0-9])|(1[01]))((\")|('in'))$", inches):
            return True

    if re.search("^2$", feet):
        if re.search("^((0?[0-9])|(1[01]))((\")|('in'))$", inches):
            return True
    return False


def main():
    # License Plate validation
    license_sample = {"ABC123": True,
                      "789XYZ": True,
                      "AB1 23C": True,
                      "AB1-23C": True,
                      "AB1--23C": False,
                      "AB123C": False}

    is_license_function_good = True
    for plate, is_valid in license_sample.items():
        result = is_valid_bc_license_plate(plate)
        if result != is_valid:
            print("%s should be %s" % (plate, str(is_valid)))
            is_license_function_good = False

    if is_license_function_good:
        print("License plate validator is all good")

    # Python variable name validator
    variable_samples = {"the_dog": True,
                        "the__dog": False,
                        "abcdefghijklmnopqrstuvwxyzabcdef": True,
                        "abcdefghijklmnopqrstuvwxyzabcdefg": False,
                        "the_dog_is_spotted": True}

    is_variable_function_good = True
    for variable, is_valid in variable_samples.items():
        result = is_valid_python_variable_name(variable)
        if result != is_valid:
            print("%s should be %s" % (variable, str(is_valid)))
            is_variable_function_good = False

    if is_variable_function_good:
        print("Python variable validator is all good")


    # email validator
    email_samples = {"Jason_Harrison@bcit.ca": True,
                     "a_____b@c.com": True,
                     "dd99@bcit.ca": False,
                     "abfS@bcit.88": False
                     }

    is_email_good = True
    for email, is_valid in email_samples.items():
        result = is_valid_email_address(email)
        if result != is_valid:
            print("Invalid email address")
            is_email_good = False

    if is_email_good:
        print("Email address validator is all good")

    # height validator

    height_samples = {"2'1\"": True,
                      "8'11\"": True,
                      "9'88\"": False
                      }

    is_height_good = True
    for height, is_valid in height_samples.items():
        result = is_valid_human_height(height)
        if result != is_valid:
            print("Incorrect data")
            is_height_good = False

    if is_height_good:
        print("Height validator is all good")


if __name__ == "__main__":
    main()
