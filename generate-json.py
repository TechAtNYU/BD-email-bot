import json
import sys

if len(sys.argv) != 2:
    print("Incorrect number of arguments.")
    sys.exit(0)
file = sys.argv[1]

name = raw_input(
    "What name would you like the email to come from? ex: Aneesh Ashutosh\n")
username = raw_input(
    "What is the email you are sending from? ex: aneesh@techatnyu.com\n")
password = raw_input(
    "What is the password to that email account? ex: password\n")
subject = raw_input(
    "What is the subject of the email? ex: \"Hello, {{NAME}}!\"\n")
message = raw_input(
    "What is the message? ex: \"Welcome to Tech@NYU, {{NAME}}! We want your company, {{COMPANY}}, to give us cash money.\"\n")
raw_emails = raw_input(
    "Please enter all emails the message should be sent to in a comma-separated list. ex: rob@techatnyu.com,jenn@techatnyu.com,david@techatnyu.com\n")
variables = raw_input(
    "Please enter all variable names as a comma-separated list. ex: NAME,COMPANY\n").split(",")

emails = raw_emails.split(",")
# strip all trailing whitespace from lists
map(str.strip, emails)
map(str.strip, variables)

json_dictionary = {}
json_dictionary["name"] = name
json_dictionary["username"] = username
json_dictionary["password"] = password
json_dictionary["to"] = "{{EMAIL}}"
json_dictionary["subject"] = subject
json_dictionary["message"] = message
json_variables = []

formatted_emails = []
for email in emails:
    formatted_emails.append({'val': email})
json_variables.append({'var': '{{EMAIL}}', 'vals': formatted_emails})

for var in variables:
    raw_variable_values = raw_input(
        "Please enter all values of variable " + var + "\n")
    variable_values = raw_variable_values.split(",")
    map(str.strip, variable_values)
    list_variables = []
    for val in variable_values:
        list_variables.append({'val': val})
    variable_entry = {'var': '{{' + var + '}}', 'vals': list_variables}
    json_variables.append(variable_entry)

json_dictionary["variables"] = json_variables

print("Saving to " + file + "...")
with open(file, 'w') as f:
    json.dump(json_dictionary, f, sort_keys=True, indent=4,
              separators=(',', ': '), ensure_ascii=False)
    # json.dump(json_dictionary, f, ensure_ascii=False)

print("Done!")
