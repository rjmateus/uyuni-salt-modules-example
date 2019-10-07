#!/usr/bin/python3.6
from xmlrpc.client import ServerProxy
import ssl
MANAGER_URL = "https://server-4-0.tf.local/rpc/api"
MANAGER_LOGIN = "admin"
MANAGER_PASSWORD = "admin"
# You might need to set to set other options depending on your
# server SSL configuartion and your local SSL configuration
context = ssl._create_unverified_context()
client = ServerProxy(MANAGER_URL, context=context)
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)
print(client.user.list_users(key))
print(client.org.listOrgs(key))

print(client.org.create(
    key,
    "test", "admin_test", "admin",
    "Dr.", "admin_test", "admin_test", "admin_test@tes.com", False))

client.auth.logout(key)

ORG_MANAGER_LOGIN = "admin_test"
ORG_MANAGER_PASSWORD = "admin"

key = client.auth.login(ORG_MANAGER_LOGIN, ORG_MANAGER_PASSWORD)
print(client.user.create(key, "user1", "user1", "name", "name", "user1@test.com", 0))
print(client.user.create(key, "user2", "user2", "name", "name", "user2@test.com", 0))

print(client.user.list_users(key))

client.auth.logout(key)
