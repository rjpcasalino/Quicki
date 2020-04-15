#! /usr/bin/perl -w
# Copyright 1994-2000, Cunningham & Cunningham, Inc.
# Open Source for personal use only.
# ... and then only
# with the understanding that the owner(s) cannot be
# responsible for any behavior of the program or
# any damages that it may cause. See LICENSE.TXT

# use strict;
$|++;
print "Content-type: text/html\n\n";

my $link = "[A-Z][a-z0-9]+([A-Z][a-z0-9]+)+";
my $mark = "\263";

my $page = $ENV{QUERY_STRING} =~ /^$link$/
	? $&
	: "WelcomeVisitors";

my $text = "";

if ( -e "pages/$page" ) {
	open(F, "pages/$page") or die "$page: $!";
	undef $/;
	$_ = <F>;
	close(F);
	s/&/&amp;/g;
	s/</&lt;/g;
	s/>/&gt;/g;
	$text = $_;
	$/ = "\n";
}


my %par;
$par{page} = $page;
$par{body} = << "";
	<form method=post action="save.cgi?$page">
	<textarea name=Text rows=16 cols=60 wrap=virtual>$text</textarea>
	<p><input type="submit" value=" Save ">
	</form>

open(T, 'template.html') or die "template.html: $!";
undef $/;
$_ = <T>;
close(T);
s/\$(\w+)/defined($par{$1}) ? $par{$1} : ''/geo;
print;
$/ = "\n";

