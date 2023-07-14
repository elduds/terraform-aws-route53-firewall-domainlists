output "all_domain_lists" {
    value = local.all_domain_lists
    description = "Map of all Route53 Resolver DNS Firewall Managed Domain lists by AWS Region"
}