include stdlib

file_line { 'Set SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]*[\s]*(?i)IdentityFile[\s]+.*',
  replace            => true,
  append_on_no_match => true,
  notify             => Service['ssh'],
}

file_line { 'Deny Password Authentication':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]*[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true,
  notify             => Service['ssh'],
}

service { 'ssh':
  ensure => 'running',
  enable => true,
}
