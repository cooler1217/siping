#! /usr/bin/perl -w   
#filename: add_ftp_user.pl   
use strict;   
#   
print "#example: user:passwd\n";   
while (<STDIN>) {   
    exit if ($_ =~/^\n/);   
    chomp;   
    (my $user, my $pass) = split /:/, $_, 2;   
    my $crypt = crypt $pass, '$1$' . gensalt(8);   
    print "$user:$crypt\n";   
}   
sub gensalt {   
    my $count = shift;   
    my @salt = ('.', '/', 0 .. 9, 'A' .. 'Z', 'a' .. 'z');   
    my $s;   
    $s .= $salt[rand @salt] for (1 .. $count);   
    return $s;   
} 