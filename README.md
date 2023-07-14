# terraform-aws-route53-firwall-domainlists

## Introduction
Terraform module to provide named lookups of AWS Route53 Resolver DNS Firewall Managed Domain List IDs.

ID is stored statically in all_lists.json and will be updated with new module versions

```
  + all_domain_lists = {
      + ap-northeast-1 = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-103b4302c274455e"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-3ba9acb851c04c45"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-1a63d8549cca46e6"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-dc19e97bef3c454a"
        }
      + ap-northeast-2 = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-1997a3cdd61a4f2a"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-19615996f5c5490f"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-e8d1e969ad484741"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-6301b5257e0c4210"
        }
      + ap-northeast-3 = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-2e57899062984ed1"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-4bf13df37a441bc"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-c708707d5d6e4359"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-7fc34ef9e9ea468b"
        }
      + ap-south-1     = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-d1159fcdd6b942cf"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-3d348983c03d44a1"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-c6afb679f51946cd"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-cb11fc50eaef4bad"
        }
      + ap-southeast-1 = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-49099fd7fc3d4853"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-b1c1d04c32194010"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-2ff056c2bf334345"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-cc92cf0f3482427c"
        }
      + ap-southeast-2 = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-9be336ef32844e5"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-266fd908c38f42d5"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-eac509f599e640b6"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-73ed798ec0d14b61"
        }
      + ca-central-1   = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-46d873be30464a06"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-181528f01d8f4134"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-2ce5306fddeb4dfd"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-a81620624a514ced"
        }
      + eu-central-1   = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-54a2c1ef5b014042"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-f5447e97782f4746"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-1e3b46ad48844225"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-d81c6f509bef4d49"
        }
      + eu-north-1     = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-17764a248c141e9"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-9cfbbf8059454500"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-bd383ec1cede45cc"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-19c22a22cc624ad7"
        }
      + eu-west-1      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-a88f2f26cc6a4296"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-2f416a2435da4ee6"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-fad18de921a64bfa"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-7aba603e4cc343fd"
        }
      + eu-west-2      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-4e96d4ce77f466b"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-876a86d96f294739"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-3268f74d91fe418f"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-4fc4edfc63854751"
        }
      + eu-west-3      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-6002172db5fc4cab"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-66d3dfe2b4234c4e"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-2d71f72512345cb"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-31cbb811909748dc"
        }
      + sa-east-1      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-5d3faeb3ed7a4492"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-154a50443f004ad4"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-946e512cb7624fd5"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-83ca12c0855d49ab"
        }
      + us-east-1      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-15f4860b1ad54ead"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-984dae9d8bac4e2b"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-aa970e9eb1ca4777"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-2c46f2ecbfec4dcc"
        }
      + us-east-2      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-bbc798062d594728"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-996a2e1ce1314abb"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-3c30dcb4c50b4401"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-19f9b4c730a14748"
        }
      + us-west-1      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-d2a6edeaa3b04a8a"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-1e9ab4960ee4f9a"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-1f6c57357d4d47c9"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-9d577f4576e54ab7"
        }
      + us-west-2      = {
          + AWSManagedDomainsAggregateThreatList       = "rslvr-fdl-d252ee1944404e15"
          + AWSManagedDomainsAmazonGuardDutyThreatList = "rslvr-fdl-23584f0fb4c24ebb"
          + AWSManagedDomainsBotnetCommandandControl   = "rslvr-fdl-c80983a1f0284c99"
          + AWSManagedDomainsMalwareDomainList         = "rslvr-fdl-fe17696f22a445f6"
        }
    }
```

## Usage

```hcl
provider "aws" {
  region = "ap-southeast-2"
}

module "route53resolver-firewall-domainlists" {
  source  = "elduds/route53resolver-firewall-domainlists/aws"
  version = "0.1.2"
}

data "aws_region" "current" {}

resource "aws_route53_resolver_firewall_rule_group" "managed_domain_lists" {
  name = "managed-domain-lists"
}

resource "aws_route53_resolver_firewall_rule" "block_malware_domains" {
  action                  = "BLOCK"
  block_response          = "NODATA"
  firewall_domain_list_id = module.route53resolver-firewall-domainlists.all_domain_lists[data.aws_region.current.name].AWSManagedDomainsMalwareDomainList
  firewall_rule_group_id  = aws_route53_resolver_firewall_rule_group.managed_domain_lists.id
  name                    = "block-AWSManagedDomainsMalwareDomainList"
  priority                = 300
}
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
# Maintainers:

- Luke Dudney
