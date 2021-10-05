import re
import sys
import os
import javaos

clustername = 'OAS'
cell = AdminControl.getCell()
list_node =[]

for cm in AdminConfig.list("ClusterMember",
	AdminConfig.getid("/ServerCluster:"
		+clutername+"/")).split('\n'):
  nodename = AdminConfig.showAttribute(cm,"nodeName")
  membername = AdminConfig.showAttribute(cm,"memberName")
  serverId = AdminConfig.getid("/Cell:"+cell+"/Node:"+nodename+"/Server:"+membername)

  print "Server ID:" +serverId
  poolid = AdminConfig.list("ThreadPool", serverId).split('\n')
  print AdminConfig.show(poolid[3])
  print ('\n')
  print AdminConfig.show(poolid[10])

  list_node.append(nodename)