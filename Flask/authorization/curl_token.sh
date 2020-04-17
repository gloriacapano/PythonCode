# Connect to /welcome with right credentials
curl --header "Authorization: Bearer ArthurConanDoyle"\
    127.0.0.1:5000/welcome
echo " "

# Connect to /welcome with wrong token
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
curl --header "Authorization: Bearer ArthurConanDoyle"\
    --header "Content-Type: application/json"\
     --request POST\
     --data '{"message": "The murder is the butler"}'\
     127.0.0.1:5000/encrypt
echo " "

echo "Encrypt message with wrong credentials"
curl --header "Authorization: Bearer EdgardAllanPoe"\
    --header "Content-Type: application/json"\
     --request POST\
     --data '{"message": "The murder is the butler"}'\
     127.0.0.1:5000/encrypt
echo " "