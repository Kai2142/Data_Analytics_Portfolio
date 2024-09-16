import pandas as pd


def clean_name(name):
    cleaned_name = ''.join(char for char in name if char.isalpha() or char.isspace())
    return cleaned_name


# Function to generate the student ID
def generate_student_id(row):
    full_name = clean_name(row["Full Name"])
    names = full_name.split()

    first_name = names[0] if names else ""
    last_name = names[-1] if names else ""
    middle_name = ' '.join(name[0] for name in names[1:-1]) if len(names) > 2 else ""

    dob = pd.to_datetime(row["Date of Birth"]).date()
    gender = row["Gender"]

    initials = ''.join(name[0].upper() for name in [first_name, middle_name, last_name] if name)
    dob_formatted = dob.strftime('%Y%m')
    gender_code = '0' if gender.lower() == 'female' else '1'

    return f"{initials}-{dob_formatted}-{gender_code}"