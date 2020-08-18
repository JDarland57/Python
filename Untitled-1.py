import dns.resolver 
import csv
import os
from os.path import dirname, abspath


# Setting Variables
current_path = dirname(abspath(__file__))
domainFName = '{0}/domainstest.csv'.format(current_path)
outputFile = '{0}/output.csv'.format(current_path)
dnsList = '{0}/list2.csv'.format(current_path)
case_list = []
dns_list = []
fields = ['Domains', 'DNS Resolvers']
csv_output = zip(case_list, dns_list)

# THIS IS THE CODE FOR WRITING CSV FILES INTO LISTS - LABELED AS #1

# Read in all domains from csv into list
with open(domainFName, 'r') as file:
    for line in csv.reader(file):
        case_list.append(line)
        
file.close()

# THIS IS THE END OF THE CODE FOR WRITING CSV FILES INTO LISTS - LABELED AS #1

# THE CODE BELOW IS WORKING FOR FINDING THE DNS RESOLVERS - LABELED AS #2

def dnsResolver (domain):
    answers = dns.resolver.resolve(domain, 'NS')
    for server in answers:      
        return(server.target)
     

for firstdomain in case_list:
    for domain in firstdomain:
        dns_list.append(dnsResolver(domain))
        with open(dnsList,'w', newline="") as r:
            writers = csv.writer(r)
            writers.writerows(dns_list)
r.close()

# THIS IS THE END OF THE WORKING CODE - LABELED AS #2     
   
# Write the dns Resolver names into a new csv file

with open(outputFile,'w+', newline="") as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerow(fields)
    for row in csv_output:
        writer.writerow(row)

    #writer.writerow(case_list)
    #writer.writerow(dns_list)
f.close()

exit()