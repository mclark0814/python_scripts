#!/usr/bin/env python3.7

print("Hello and thank you for reaching out to see a copy of my list containing a some of AWS' Services.\n")

aws_svcs_list = [] # Establishing the name of the list

print("\nThe AWS Services list is empty", aws_svcs_list) # Status of listing

aws_svcs_list.append('EC2')                             # elements in listing
aws_svcs_list.append('Elasticache')
aws_svcs_list.append('Elastic Beanstalk')
aws_svcs_list.append('Machine Learning')
aws_svcs_list.append('Systems Manager')
aws_svcs_list.append('VPC')                                # elements in listing
aws_svcs_list.append('Route53')
aws_svcs_list.append('CloudFront')
aws_svcs_list.append('API Gateway')
aws_svcs_list.append('Cognito')
aws_svcs_list.append('CloudHSM')
aws_svcs_list.append('IAM')
aws_svcs_list.append('Key Management Service')
aws_svcs_list.append('Amazon Macie')
aws_svcs_list.append('WAF & Shield')
aws_svcs_list.append('CloudFormation')                      # elements in listing
aws_svcs_list.append('AWS Cost Explorer')
aws_svcs_list.append('Secrets Manager')
aws_svcs_list.append('Certificate Manager')
aws_svcs_list.append('Artifact')
aws_svcs_list.append('Lambda')
aws_svcs_list.append('s3')
aws_svcs_list.append('X-Ray')
aws_svcs_list.append('EFS')                                 # elements in listing

#New services have been added to the listing

print('\nAfter adding services, the length of the listing is now:', len(aws_svcs_list))

print("\nThe AWS Services list now contains:", aws_svcs_list)


strs = aws_svcs_list                               # Assigning list table to variable for sorting
strs.sort()                                        # sort the content of the variable
print("\nListing in Alphabetical order")           # Print the listin out in alphabetical order


print("Deleting two services:", 'Route53' " & " 'EFS') # Announce the deletion of two services

del aws_svcs_list[23]                                  # Delete two services
del aws_svcs_list[6]

#Print an updated status
print('\nAfter deleting two services: Route53 and EFS, the length of the listing is now:', len(aws_svcs_list))

print("\nThe AWS Services list now contains:", strs)
