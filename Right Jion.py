# Select all products, and the user(s) who have them as their favorite:
sql="SELECT \"
   users.name As user,\
   products.name As favorite\
   FROM users \
   RIGHT JION products ON users.fav=products.id"