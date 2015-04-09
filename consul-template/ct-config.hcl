template {
 source = "./haproxy-cfg.ctmpl"
 destination = "/tmp/haproxy-consul.cfg"
 command = "/usr/sbin/haproxy -D -f /tmp/haproxy-consul.cfg -p /var/run/haproxy.pid -sf $(cat /var/run/haproxy.pid)"
}
retry = "10s"
max_stale = "10s"
wait = "5s:10s"
log_level = "info"
