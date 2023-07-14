#!/usr/bin/env python3

import json
import boto3

botosession = boto3.Session()
ec2 = botosession.client(service_name='ec2')
all_regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

all_lists = {}

for region in all_regions:
    all_lists[region] = {}
    route53resolver = botosession.client(service_name='route53resolver',
                                         region_name=region)

    regional_lists = route53resolver.list_firewall_domain_lists()['FirewallDomainLists']

    for domain_list in regional_lists:
        if domain_list['ManagedOwnerName'] == 'Route 53 Resolver DNS Firewall':
            all_lists[region][domain_list['Name']] = domain_list['Id']

with open('new_all_lists.json', 'w', encoding='utf-8') as outfile:
    json.dump(all_lists, outfile, indent=4)
