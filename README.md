# SUMA salt modules and states for orgs and user

This project has a set of salt modules and states to easily manage suse
manager server organizations and suse_manager_server

# states
## 'uyuni_org.present'

**Available fields for the salt stated:**
* org_name
* first_username
* first_password
* user_email
* prefix = Must match one of the values available in the web UI. (i.e. Dr., Mr., Mrs., Sr., etc.). Default value is 'Sr.'
* firstName: default value is the value passed in first_username field
* lastName: default value is the value passed in first_username field

Example:
```
test:
  uyuni_org.present:
    - org_name: "new org"
    - first_username: new_test
    - first_password: new_test
    - user_email: new@test.com
    - prefix: "Sr."
    - firstName: "New"
    - lastName: "User"
```
# Modules
## 'uyuni_org'

### check_present ()
Verify is organization is set up on the server with the correct user names
example:

### present
Creates a new organization with a new user to administer the organization
