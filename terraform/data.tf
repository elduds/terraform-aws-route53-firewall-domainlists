locals {
    all_domain_lists = tomap(jsondecode(file("${path.module}/all_lists.json")))
}