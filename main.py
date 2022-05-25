import smtplib

my_email = "mrwickjonathan62@gmail.com"
my_password = "abc123()"

# TODO making an object of SMTP Class (SMTP stands for Simple Message Transport Protocol)
connection = smtplib.SMTP("smtp.gmail.com", port=587)
# TODO TLS (TLS stands for Transport Layer Security) TLS is used for securing the message
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="mrwickjonathan62@yahoo.com", msg="Hello Jonathan")
connection.close()
