#!/usr/bin/perl -w

#use strict;

#Point these to a directory of RH and rebuilt (aka WB) RPMS
#$WB_RPMS = "/home/test/b8";
#$RH_RPMS = "/home/test/new";

my $WB_RPMS = "/centos-3/build8/i386/RedHat/RPMS";
my $RH_RPMS = "/centos-3/build6/i386/RedHat/RPMS";

# Size difference to trigger error, .1 = plus/minus 10%
my $SizeError=.10;

# Working directories
# Careful where these point, they get a "rm -rf" cleaning!
my $RHTMP="/tmp/RH-$$";
my $WBTMP="/tmp/WB-$$";
my $rpm;

opendir(DIR,$RH_RPMS);
my @allrpms= grep (/rpm$/, readdir(DIR) );
closedir(DIR);

foreach $rpm (sort @allrpms){
my  $rpmwb=$rpm;
my $rpmwbf=$rpm;

    if (! (-e "$WB_RPMS/$rpm") ) {
	print "\nNo equivalent original for $rpm \t trying glob\n";

        my $fname= $rpm;
	$fname =~ s/(.*)-.*-.*/$1-/;
#	print "fname is $fname\n";
	my $found = 0;

#print "trying $WB_RPMS/$fname*\n";

		 my @globmatch = glob("$WB_RPMS/$fname*");
		while ($rpmwb = shift @globmatch) {
	#while($rpmwb = glob("$WB_RPMS/$fname*")){
		my $try = $rpmwb;
#		print "\nglob got $try\n ";
		$try =~ s/.*\///;
		$try =~ s/(.*)-.*-.*/$1-/;
		
		if($try eq $fname)
			{
			#this is the one
			$rpmwbf = $rpmwb;		
			$rpmwbf =~ s/.*\///;
			$found = 1;

		        while($rpmwb = glob("$WB_RPMS/$fname*")){};

			last;
			}
		}
	
	if(!$found)
		{
		next;
		}
    }

    if($rpm =~ /^kernel/)
	{
	next;
	}	

    if($rpm eq $rpmwbf)
	{
	# only doing difficult ones
#	next;
	}
    else
	{
    	print "$rpm >> $rpmwbf\n";
	}

    # Initialize
    %allfiles=(); %RHhash=(); %WBhash=();
    $fileproblems=0; $libproblems=0;
    system("rm -rf $RHTMP;mkdir $RHTMP");
    system("rm -rf $WBTMP;mkdir $WBTMP");
    # Extract RPMS
    system("cd $RHTMP/; rpm2cpio $RH_RPMS/$rpm | cpio -id --no-absolute-filenames --quiet");
    system("cd $WBTMP/; rpm2cpio $WB_RPMS/$rpmwbf | cpio -id --no-absolute-filenames --quiet");

    # Parse name/size info
    @RHnamesize=`cd $RHTMP/; find ./ -printf "%p:_:%s:_:%U:_:%G:_:%04m:_:\n"`;
    @WBnamesize=`cd $WBTMP/; find ./ -printf "%p:_:%s:_:%U:_:%G:_:%04m:_:\n"`;
    for ($i=0;$i<@RHnamesize;$i++){
	($file,$size,$uid,$gid,$perms)=split(/:_:/,$RHnamesize[$i]);
	$RHhash{"$file"}=$size;
	$RHuid{"$file"}=$uid;
	$RHgid{"$file"}=$gid;
	$RHperms{"$file"}=$perms;
	$allfiles{"$file"}=1;
    }
    for ($i=0;$i<@WBnamesize;$i++){
	($file,$size,$uid,$gid,$perms)=split(/:_:/,$WBnamesize[$i]);
	$WBhash{"$file"}=$size;
        $WBuid{"$file"}=$uid;
        $WBgid{"$file"}=$gid;
        $WBperms{"$file"}=$perms;
	$allfiles{"$file"}=1;
    }

    
    # Print and tag file errors if appropraite
    printf ("%-50s\t", $rpm);
    foreach $file (keys %allfiles){
	if (!(exists $RHhash{"$file"})){
	    print "\n\tPackage contains extra file:  $file";
	    $fileproblems=1;
	}
	elsif (!(exists $WBhash{"$file"})){
	    print "\n\tPackage is missing file: $file";
	    $fileproblems=1;
	}
	else {
	    if ($RHhash{"$file"}>0){
		$ratio=($WBhash{"$file"})/($RHhash{"$file"})}
	    else{
		$ratio=1-$WBhash{"$file"};  # Negative ratios indicate filesize vs. zero in RedHat
	        }
	    if (($ratio-1)*($ratio-1)>($SizeError*$SizeError)) {
		printf("\n\tSize Ratio: %3.2f on file:%s",$ratio,$file);
		$fileproblems=1;
	        };

            if ($RHuid{"$file"} ne $WBuid{"$file"}) {
		printf("\n\tUid Diff $RHuid{\"$file\"} : $WBuid{\"$file\"} on $file");
		$fileproblems=1;
		}
            if ($RHgid{"$file"} ne $WBgid{"$file"}) {
                printf("\n\tGid Diff $RHgid{\"$file\"} : $WBgid{\"$file\"} on $file");
		$fileproblems=1;
                }
            if ($RHperms{"$file"} ne $WBperms{"$file"}) {
                printf("\n\tPerms Diff $RHperms{\"$file\"} : $WBperms{\"$file\"} on $file");
		$fileproblems=1;
                }
	   }
    }

    
    # Select executable files
    @RHexec=`cd $RHTMP/; find ./ -perm +111 -type f -print`; 

    # Check library dependencies
    foreach $executable (@RHexec) {
	chop $executable;

	#  Move on if no equivalent binary exists in rebuild
	if (! (-e "$WBTMP/$executable") ) {next;}

	# Get shared libs
	@RHlibs=`ldd $RHTMP/$executable`;
	@WBlibs=`ldd $WBTMP/$executable`;

        # Clean up ldd output
	$RHlibline=join('',(sort @RHlibs)); 
	$WBlibline=join('',(sort @WBlibs)); 
	$RHlibline=~ s/=>(.*)(\n)/\n/g; $RHlibline=~ s/(\s+)/ /g; 
	$WBlibline=~ s/=>(.*)(\n)/\n/g; $WBlibline=~ s/(\s+)/ /g;
	@RHlibs=split(/ /,$RHlibline);
	@WBlibs=split(/ /,$WBlibline);

        # Print and tag library errors
	foreach $lib (@RHlibs){
	    $searchpat=$lib;
	    $searchpat =~ s/\+/\\\+/g;
	    $searchpat =~ s/\./\\\./g;
	    unless ($WBlibline =~ (/$searchpat/)){
		print "\n\tMissing link in $executable:\t$lib";$libproblems=1;
	    }
	}
	    
	foreach $lib (@WBlibs){
	    $searchpat=$lib;
	    $searchpat =~ s/\+/\\\+/g;
	    $searchpat =~ s/\./\\\./g;
	    unless ($RHlibline =~ (/$searchpat/)){
		print "\n\tExtra link in $executable:\t$lib";$libproblems=1;
	    }
	}
    }

    # sort out provides and requires

   @RHrequires = `rpm -qp --requires $RH_RPMS/$rpm`;
   @WBrequires = `rpm -qp --requires $WB_RPMS/$rpmwbf`;

   while ($rhrequire = shift(@RHrequires))
	{
	if($wbrequire = shift(@WBrequires))
		{
		chomp($rhrequire);
		chomp($wbrequire);

#		print "$rhrequire : $wbrequire\n";

		if ($rhrequire gt $wbrequire)
			{
			# extra one in wbrequire
			print "\n\tExtra require $wbrequire";$fileproblems=1;
			unshift(@RHrequires,$rhrequire);
			}
		elsif($rhrequire lt $wbrequire)
			{
			# one missing in wbrequire
			print "\n\tMissing require $rhrequire";$fileproblems=1;
			unshift(@WBrequires,$wbrequire);
			}

		}
	else
		{
		# end of wb array
		print "\n\tMissing require $rhrequire";$fileproblems=1;
		}

	}

  if(shift(@WBrequires)){
	# extra in the wb array
	print "\n\tExtra require $wbrequire";$fileproblems=1;
	}


   @RHprovides = `rpm -qp --provides $RH_RPMS/$rpm`;
   @WBprovides = `rpm -qp --provides $WB_RPMS/$rpmwbf`;

   while ($rhprovide = shift(@RHprovides))
	{
	if($wbprovide = shift(@WBprovides))
		{
		chomp($rhprovide);
		chomp($wbprovide);

#		print "$rhprovide : $wbprovide\n";

		if ($rhprovide gt $wbprovide)
			{
			# extra one in wbprovide
			print "\n\tExtra provide $wbprovide";$fileproblems=1;
			unshift(@RHprovides,$rhprovide);
			}
		elsif($rhprovide lt $wbprovide)
			{
			# one missing in wbprovide
			print "\n\tMissing provide $rhprovide";$fileproblems=1;
			unshift(@WBprovides,$wbprovide);
			}

		}
	else
		{
		# end of wb array
		print "\n\tMissing provide $rhprovide";$fileproblems=1;
		}

	}

  if(shift(@WBprovides)){
	# extra in the wb array
	print "\n\tExtra provide $wbprovide";$fileproblems=1;
	}


    if ($fileproblems || $libproblems) { print "\n\n";} else {print "MATCH\n";} 
}



----------------------

<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
