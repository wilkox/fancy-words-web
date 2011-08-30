#!/usr/bin/perl

use warnings;
use CGI;

#define languages
%lang = (
	'OE' => 'old english',
	'F' => 'french',
	'L' => 'latin',
	'LL' => 'late latin',
	'AS' => 'anglo-saxon',
);

#read in words
die unless open(DICT, "<../../fancy-words/dict/ety.csv");
while (my $line = <DICT>) {
	next if $. == 1;
	chomp $line;
	$line =~ /^([^,]+),([^,]+),(.+$)/;
	$langOf{$1} = $2;
	$fancyOf{$1} = $3;
}
close DICT;

#fancy-count input
$query = new CGI;
my $content = $query->param('content');
my @content = split(/\s+/, $content);
my $total;
foreach my $word (@content) {
	$word = lc($word);
	if (exists $langOf{$word}) {
		++$count{$lang{$langOf{$word}}};
		++$fancyCount{$fancyOf{$word}};
		++$total;
	} else {
		++$count{'unknown'};
		++$total;
	}

}

#produce output
print "Content-type: text/html\n\n";
print <<EOF;
<HTML>
<HEAD>
<TITLE>Fancy-o-meter</TITLE>
</HEAD>

<BODY>

<H1>Fancy-o-meter</H1>
EOF

my $fancyPer = 100 * $fancyCount{'fancy'} / $total;
print <<EOF;
<h2>Your text is $fancyPer% fancy!</h2>
<table>
  <tr>
EOF
foreach my $lang (keys(%count)) {
	print "\n<tc>$lang</tc>";
}
print "</tr>\n<tr>";
foreach my $lang (keys(%count)) {
	print "\n<tc>$count{$lang}</tc>";
}
print <<EOF;
</tr>
</table>


Your text:

$content
</BODY>
</HTML>
EOF
