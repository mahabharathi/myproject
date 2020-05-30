#https://www.twilio.com/console/sms/getting-started/build
from twilio.rest import Client 
 
account_sid = 'AC40a58aa5561edf9c6b5c18965ea81b5c' 
auth_token = '3586243afcae249da99b9121928631f9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+17867568645',  
                              body='hi i am maha',      
                              to='+918825963872' 
                          ) 
 
print(message.sid)