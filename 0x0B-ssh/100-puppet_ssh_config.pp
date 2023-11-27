# client configuration.
file { '~/.ssh':
  ensure  => directory,
}

file_line { '~/.ssh/config':
  ensure   => 'present',
  content  =>  "PasswordAuthentication no",
}

file_line { '~/.ssh/config':
  ensure   => 'present',
  content  =>  "IdentityFile ~/.ssh/school",
}
