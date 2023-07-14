# terraform_aws_route53resolver_firewall_domainlists

## Introduction
Terraform module to provide named lookups of AWS Route53 Resolver DNS Firewall Managed Domain List IDs

## Usage

```hcl
provider "aws" {
  region = "ap-southeast-2"
}

module "terraform_aws_route53_firewall_domainlists" {
  version = ">= 0.1.0"
  source  = "elduds/route53-firewall-domainlists/aws"
}

data "aws_region" "current" {}

resource "aws_route53_resolver_firewall_rule_group" "managed_domain_lists" {
  name = "managed-domain-lists"
}

resource "aws_route53_resolver_firewall_rule" "block_malware_domains" {
  action                  = "BLOCK"
  block_response          = "NODATA"
  firewall_domain_list_id = module.terraform_aws_route53_firewall_domainlists.all_domain_lists[data.aws_region.current.name].AWSManagedDomainsMalwareDomainList
  firewall_rule_group_id  = aws_route53_resolver_firewall_rule_group.managed_domain_lists.id
  name                    = "block-AWSManagedDomainsMalwareDomainList"
  priority                = 300
}

```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
# Maintainers:

- Luke Dudney
