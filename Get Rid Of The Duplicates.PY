student_data = {
    "Id1": {"Name": "Sara", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "Id2": {"Name": "David", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "Id3": {"Name": "Sara", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "Id4": {"Name": "Surya", "Class": "V", "Subject_Integration": "English, Math, Science"},
}

result = {}
seen_keys = []


for student_id, details in student_data.items():
    unique_key = {details["Name"], details["Class"], details["Subject_Integration"]}

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)