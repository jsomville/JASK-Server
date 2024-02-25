


def getUser(db, email, hashedPassword):
    if email in db:
        user = db[email]
        if user.hashedPassword == hashedPassword:
            return user