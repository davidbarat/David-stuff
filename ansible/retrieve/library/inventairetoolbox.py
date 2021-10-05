#!/bin/env python

from ansible.module_utils.basic import *
from elasticsearch import elasticsearch
import json
import sys


def main():
  es = Elasticsearch(
    ["http://123:9200"])
  fields = {
    "host": {"required": True, "type": "str"},
    "ansible_host": {"required": True, "type": "str"},
    "env": {"required": True, "type": "str"},
    "version": {"required": True, "type": "str"},
  }
  module = AnsibleModule(argument_spec=fields)
  try:
    tmp_json = {
      'host': module.params["ansible_host"],
      'alias': module.params["host"],
      'env': module.params["env"].replace,
      'version': module.params["version"],
    }
  except:
    a = 1
  module.exit_json(msg="")


  def get_version_tbx():
    with open('/apps/toolboxes/version') as f:
      version = f.read().split(|)
      return(version)

  if if __name__ == "__main__":
      main()