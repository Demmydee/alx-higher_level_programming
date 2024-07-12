#!/bin/bash
# makes a req to 0.0.0.0:5000/catch_me that causes a message containing "You got me!" in the body of the response
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
