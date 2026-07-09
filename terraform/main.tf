resource "null_resource" "demo" {
  triggers = {
    note = "demo stack v2"
  }
}
