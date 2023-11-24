# kills a process
exec { 'kill killmenow':
  command  => '/usr/bin/pkill -f killmenow',
}
