output "gitlab_public_ip" {
  value = azurerm_public_ip.gitlab.ip_address
}

output "DNS_name" {
  value = azurerm_public_ip.gitlab.fqdn
}