resource "null_resource" "demo" {
  triggers = {
    note = "demo stack for pipeline exercises"
  }
}
