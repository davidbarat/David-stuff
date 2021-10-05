dsList = AdminConfig.list('DataSource').splitlines()
for ds in dsList:
    try:
	      propSet = AdminConfig.showAttribute(ds,'properySet')
    except AdminException, why:
	      print(Error getting propertySet:)
	      print(why)
    else:
