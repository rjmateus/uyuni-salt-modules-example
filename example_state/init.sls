test:
  uyuni_org.present:
    - name: "new org"
    - first_username: new_test
    - first_password: new_test
    - user_email: new@test.com

test2:
  uyuni_org.present:
    - name: "ric_org"
    - first_username: ric_test
    - first_password: ric_test
    - user_email: new@test.com

simple_user:
  uyuni_user.present:
    - name: user_new
    - password: user_new2
    - org: ric_org
    - org_admin_username: ric_test
    - org_admin_password: ric_test
    - first_name: user_new_first2
    - last_name: user_new_last2
    - email: user_new2@test.com
    - org_admin: False

admin_user_ric_org:
  uyuni_user.present:
    - name: user_new_admin
    - password: user_new_admin
    - org: ric_org
    - org_admin_username: ric_test
    - org_admin_password: ric_test
    - first_name: user_new_admin_first
    - last_name: user_new_admin_last
    - email: user_new_admin@test.com
    - org_admin: True
