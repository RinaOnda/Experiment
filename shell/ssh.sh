#!/bin/sh

address='address'
user_name='user'
password='password'

expect -c "
   set timeout 5
   spawn ssh ${user_name}@${address} ls 
   expect \"password:\"
   send \"${password}\n\"
   interact
"

