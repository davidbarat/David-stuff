import re
import sys
import time
import os
import javaos
import calendar


def month_string_to_number(string):
	m = {
	    'jan':1,
	    'fev':2,
	    'feb':2,
	    'mar':3,
	    'avr':4,
	    'apr':4,
	    'mai':5,
	    'may':5,
	    'jun':6,
	    'jui':6,
	    'jul':7,
	    'aou':8,
	    'aug':8,
	    'sep':9,
	    'oct':10,
	    'nov':11,
	    'dec':12
	    }

  try:
  	out = m[s]
  	return out
  except:
  	raise ValueError('Not a month')

 def dateDiff(keystoreName, issuedTo, expString, scopeName):
 	print '\t## CERTIFICATE DATE -> ' +expString + '##'
 	string_spec = "'"
 	month_exp = string_spec +expString[0:3]+ string_spec
 	#print month_exp
  new_month_exp = month_string_to_number(month_exp)
  #print (new_month_exp)

  if expString[4] == ',':
  	new_date_exp = '0' + expString[3] +str(new_month_exp)+ expString[5:10]
  	struc_time_exp = (expString[5:10], str(new_month_exp), '0'+expString[3],0,0,0,0,0,0,0)
  else:
  	new_date_exp = '0' + expString[3:5] +str(new_month_exp)+ expString[6:10]
  	struc_time_exp = (expString[6:10], str(new_month_exp), '0'+expString[3:5],0,0,0,0,0,0,0)
  exp_time = time.mktime(struc_time_exp)
  #print ("expi time:", exp_time)
  today_time = time.time()
  date_to_compare = float(exp_time) - 5184000

  if today_time > date_to_compare:
  	if(re.search("blueworks", issuedTo)):
  		print "\tIgnoring BlueworksLive cert"
  	else:
  		print "\n\tALERT - this certificate will expire in 2 months \n"
  		print ('\t-> Expiry Date '+expString)
  		print ('\t-> '+str(issuedTo))
  		print ('\t-> Keystore name' +str(keystoreName))
  		print ('\t-> Keystore scope' +str(scopeName)+'\n')

# Main

print 'Obtaining keystore information'

for ks in AdminTask.listKeyStores('[-all true -keyStoreUsage SSLKeys ]').splitlines():
	keystoreName = AdminConfig.showAttribute(ks, 'name')
	ms = AdminConfig.showAttribute(ks, 'managementScope')
	scopeName = AdminConfig.showAttribute(ms, 'scopeName')

	print '\n## START '+keystoreName +' in scope '+scopeName+'##'

	print '\n## START personal certificate ##'
	personalCertsFound=0
	for cert in AdminTask.listPersonalCertificates('[-keyStoreName '+keystoreName+' -keyStoreScope '+scopeName+']').splitlines():
		personalCertsFound=1
		issuedTo=""
		for property in re.split("\] \[", cert):
			if(re.search("[\[", propery)):
				tmp = property
				property = re.split("\[\[",tmp)[1]
			if(re.search("] ]", propery)):
				tmp = property
				property = re.split("] ]",tmp)[0]
			if(re.search("alias", propery)):
				alias = re.split("\s+", property)[1]
				print "\t" + property
			if(re.search("issuedTo", propery)):
				issuedTo = property
				print "\t" + property
			if(re.search("validity", propery)):
				expString = property.split()[7].split('.]')[0]+property.split()[8].split(']')[0]+property.split()[9].split('.]')[0]

				dateDiff(keystoreName, issuedTo, expString, scopeName)

	if(personalCertsFound==0):
		print '\tNo personal certificates found in '+keystoreName+' in scope '+scopeName
	print '\n\t## END personal certificates ##'

	print '\t## START signer certificates ##'
	signerCertsFound=0
  for cert in AdminTask.listSignerCertificates('[-keyStoreName '+keystoreName+' -keyStoreScope '+scopeName+']').splitlines():
		personalCertsFound=1
		issuedTo=""
    for property in re.split("\] \[", cert):
			if(re.search("[\[", propery)):
				tmp = property
				property = re.split("\[\[",tmp)[1]
			if(re.search("] ]", propery)):
				tmp = property
				property = re.split("] ]",tmp)[0]
			if(re.search("alias", propery)):
				alias = re.split("\s+", property)[1]
				print "\t" + property
			if(re.search("issuedTo", propery)):
				issuedTo = property
				print "\t" + property
			if(re.search("validity", propery)):
				expString = property.split()[5].split('.]')[0]

		if(signerCertsFound==0):
			print '\tNo signer certificates found in '+keystoreName+' in scope '+scopeName
	  print '\n\t## END signer certificates ##'

	  print '\t## END ' +keystoreName +' in scope '+scopeName+ '##'






