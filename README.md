# SUMA salt modules and states for orgs and user

This project has a set of salt modules and states to easily manage suse
manager server organizations and suse_manager_server

# Modules
## 'uyuni_org'

Module can only be applied in minions with the role 'suse_manager_server'.

### check_present (org_name, first_username, first_password)
Verify if organization is set up on the server with the correct admin user.


example:
```
salt '*' uyuni_org.check_present SUSE admin admin
```

### present (org_name, first_username, first_password, user_email, prefix='Sr.', firstName = None,lastName = None)
Creates a new organization with a user as administer of the organization

example 1:
```
salt '*' uyuni_org.check_present Org org_admin org_admin org_admin@test.com
```

example 2:
```
salt '*' uyuni_org.check_present Org org_admin org_admin org_admin@test.com "Mr." foo bar
```

## 'uyuni_user'

Module can only be applied in minions with the role 'suse_manager_server'.

### check_present (name, password, org, first_name = None, last_name = None, email = ' ',org_admin=False)
Verify is user existis in the server with the correct organization and detail information

example:
```
salt '*' uyuni_user.check_present user password SUSE firstName lastName email@email.com False
```

### present (name, password, org, org_admin_username, org_admin_password, first_name = None, last_name = None, email=' ', org_admin=False)
Creates a new user in the server for the given organization.

example:
```
salt '*' uyuni_user.present user password SUSE admin admin firstName lastName email@email.com True
```

# states
## 'uyuni_org.present'

Delegates all execution on the uyuni_org module.

**Available fields for the salt stated:**
* name
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
    - name: new_org
    - first_username: new_user
    - first_password: new_password
    - user_email: new@test.com
    - prefix: "Sr."
    - firstName: "New"
    - lastName: "User"
```

## 'uyuni_user.present'

Delegates all execution on the uyuni_user module.

**Available fields for the salt stated:**
* name
* password
* org
* org_admin_username: user that belongs to the organization and have 'org_admin' role
* org_admin_password: password for the user specified on 'org_admin_username'
* firstName: default value is the value passed in the 'name' field
* lastName: default value is the value passed in the 'name' field
* email
* org_admin: specifies if the user should be an organization administrator

Example:
```
simple_user:
  uyuni_user.present:
    - name: org_user_example
    - password: org_user_example
    - org: new_org
    - org_admin_username: new_user
    - org_admin_password: new_password
    - first_name: first_name
    - last_name: last_name
    - email: test@test.com
    - org_admin: False
```
