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
  AdminTask.setJVMProperties('[-serverName '+membername+' \
                               -nodeName '+nodeName+' \
                               -initialHeapSize 2048 \
                               -maximumHeapSize 2048]')

  list_node.append(nodename)

AdminConfig.save()

##### SyncNodes

for node in list_node:
  print node
  # Sync1 = AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=myNodeName,*')
  # AdminControl.invoke(Sync1, 'sync')