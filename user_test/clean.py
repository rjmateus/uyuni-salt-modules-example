from xmlrpc.client import ServerProxy
import ssl
MANAGER_URL = "https://server-4-0.tf.local/rpc/api"
MANAGER_LOGIN = "admin_test"
MANAGER_PASSWORD = "admin"
# You might need to set to set other options depending on your
# server SSL configuartion and your local SSL configuration
context = ssl._create_unverified_context()
client = ServerProxy(MANAGER_URL, context=context)
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)
print(client.user.list_users(key))

print(client.user.delete(key, "user1"))
print(client.user.delete(key, "user2"))

client.auth.logout(key)

ORG_MANAGER_LOGIN = "admin"
ORG_MANAGER_PASSWORD = "admin"

key = client.auth.login(ORG_MANAGER_LOGIN, ORG_MANAGER_PASSWORD)
print(client.org.delete(key, client.org.get_details(key, "test")["id"] ))
#print(client.user.delete(key, "admin_test"))

client.auth.logout(key)
