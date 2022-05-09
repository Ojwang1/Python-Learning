# LEFT JION
# Select all users and their favorite product:

sql=["SELECT \"
    users.name As user, \
    products.name As favorite \
    FROM users \
    LEFT JION products ON users.fav=products.id"]