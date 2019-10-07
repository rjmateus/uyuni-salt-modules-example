#!/usr/bin/python3.6
from xmlrpc.client import ServerProxy
import ssl
import sys

print("hello", sys.argv)

#MANAGER_URL = "https://{{ grains.get('fqdn') }}/rpc/api"
MANAGER_URL = "http://{}/rpc/api".format(sys.argv[1])

MANAGER_LOGIN = "admin"
MANAGER_PASSWORD = "admin"
# You might need to set to set other options depending on your
# server SSL configuartion and your local SSL configuration
context = ssl._create_unverified_context()
client = ServerProxy(MANAGER_URL, context=context)
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)

print(client.user.list_users(key))

print(client.org.list_orgs(key))

orgDetails = client.org.get_details(key, "test")
print("org id is: ", orgDetails["id"])

print(client.org.listUsers(key, orgDetails["id"]))

client.auth.logout(key)
