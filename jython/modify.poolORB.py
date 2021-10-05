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

  AdminConfig.modify(poolid[3], '[[maximumSize "50"] [name "ORB.thread.pool"] \
                                 [[minimumSize "10"] [inactivityTimeout "3500"] \
                                 [[isGrowable "false"]]')

  list_node.append(nodename)

AdminConfig.save()

##### SyncNodes

for node in list_node:
  print node
  # Sync1 = AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=myNodeName,*')
  # AdminControl.invoke(Sync1, 'sync')