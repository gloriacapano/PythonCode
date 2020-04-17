# Connect to /welcome with right credentials
curl -u sherlock:ArthurConanDoyle\
    127.0.0.1:5000/welcome
echo " "

# Connect to /welcome with wrong username
curl -u watson:ArthurConanDoyle\
    127.0.0.1:5000/welcome
echo " "


# Connect to /welcome with wrong password
curl -u sherlock:EdgardAllanPoe\
    127.0.0.1:5000/welcome
echo " "


# Connect to /crypto
echo "Encrypt message with no credentials"
curl --header "Content-Type: application/json"\
     --request POST\
     --data '{"message": "The murder is the butler"}'\
     127.0.0.1:5000/encrypt
echo " "

echo "Encrypt message with correct credentials"
curl -u sherlock:ArthurConanDoyle\
    --header "Content-Type: application/json"\
     --request POST\
     --data '{"message": "The murder is the butler"}'\
     127.0.0.1:5000/encrypt
echo " "