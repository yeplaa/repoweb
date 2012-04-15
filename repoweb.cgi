#!/usr/bin/perl -w 
#
# Repoweb.cgi
# Loic - GPLv3
# Version 1.0
#------------------------------------------------------------------------------

use CGI qw(:standard);

# Globals variables
my $v;
my $w;
my $des;
my $file;
my @fichiers;
my @tab2;
my @lesinfos;
my $i;
my $nom;
my $code;
my $ca;
my $clee;
my $racine="/tmp/"; # definir larborescence racine
my @repo = (<folder>); # liste des repertoires a checker dans le repertoire racine

#------------------------------------------------------------------------------
# Main program
#------------------------------------------------------------------------------
print header;    # text/html
print start_html("Repo Web");
br;
h1;
print " <h2>Repo Web</h2>";
print "<table>";
print "<tr>";
print "<th>File</th>";
print "<th>Description</th>";
print "<th>Size</th>";
print "<th>Date</th>";
print "</tr>";

# scan de chaque folder
foreach (@repo) 
{ 
	my $folder=$_;
	my $chemin="$racine/$folder";
	opendir (REPS,$chemin) or die "impossible d'ouvrir le repertoire";
	@fichiers = readdir (REPS); 
	closedir REPS;

	my %tableau;
	foreach (@fichiers) 
	{ 
		$file=$_;
		next if ($file =~ m/.txt$/);
		$desc =$_;
		chomp ($desc);
		$desc =~ s/.([a-zA-Z]+)$/.txt/i;
		warn "Impossible douvrir le fichier $desc \n" unless 
			open (DESC1,"$chemin/$desc");
		while (<DESC1>)
		{
			chomp $_;
			$tableau{$file}=$_;
			my $toto = $_;
			($nom,$code,$ca) = split(/;/, $toto);
		}

		close (DESC1);
	}

# nom des fichiers mis dans le tableau tab2
	@tab2 = keys(%tableau);
	print "   <tr>";
	print "   <tr>";
	print "   <tr>";
	print "<td>$folder</td>";
	print "   </tr>";


	foreach (@tab2)
	{

# lecture du fichier description
		($Description,$taille,$date) = split(/;/, $tableau{$_});

		print "     <tr>";
		print "      <td><a href=\"$chemin/$_\"> $_</a></td>";
		print "      <td>$Description</td>";
		print "      <td>$taille</td>";
		print "       <td>$date</td>";
		print "      </tr>  " ;

		br;

	}
}
print "</table>";
print "</tr>";
print end_html;