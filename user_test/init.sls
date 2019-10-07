mycommand:
  cmd.run:
    - name: ls -l /

register_master:
  cmd.script:
    - name: salt://user_test/list.py
    - args: "{{ grains.get('fqdn') }}" 
