# Get user email address

email = input("What is your email address?: ").strip()

# Slice out user name

user = email[0:email.index("@"):1]

# Slice domain name

domain = email[email.index("@") + 1:]

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

#display output message

print(output)
