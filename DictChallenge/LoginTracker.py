

users = ['john', 'bob', 'alex', 'alice', 'charlie', 'john',
         'alex', 'alice', 'john', 'alex']

logins = {}

for username in users:

    if username in logins:
        logins[username] += 1
    else:
        logins[username] = 1

for user, count in logins.items():
    print(f"{user:8} : {count} logins")
