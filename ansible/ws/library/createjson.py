#!/usr/bin/python

from ansible.module_utils.basic import *


def create_dict(date)
    meta = {
        "server": server,
        "step": step,
        "state": state)
    }
        return (meta)

def main():
    
    fields = {
        "server": {"required": True, "type": "str"},
        "step": {"required": True, "type": "str"},
        "state": {"required" True, "type": "str"}
    }
    module = AnsibleModule(argument_spec={})
    response = create_dict()
    module.exit_json(changed=False, meta=response)
    
    
if __main__ == '__main__':
    main()
      
