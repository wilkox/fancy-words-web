#!/usr/bin/perl

use warnings;
use CGI;
$query = new CGI;

my $content = $query->param('content')

print "Content-type: text/html\n\n";
print <<"EOF";
<HTML>
<HEAD>
<TITLE>Fancy-o-meter</TITLE>
</HEAD>

<BODY>

<H1>Fancy-o-meter</H1>

Your text:

$content
</BODY>
</HTML>
EOF
