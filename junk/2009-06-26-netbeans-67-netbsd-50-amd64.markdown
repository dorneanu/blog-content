Title: Netbeans 6.7 on NetBSD 5.0 (Amd64)
Author: Victor
Date: 2009-06-26
Tags: coding, misc, netbsd
Category: blog

Netbeans simply rocks! Download it from [here][1]! Since I&#8217;m using NetBSD I&#8217;ve downloaded the OS independent ZIP file, extracted it and found out my Java isn&#8217;t working well. I tried to install it from the pkgsrc. I tried **sun-jdk15/sun-jre15** from the Amd64 ports. I got a segmentation fault. So if you got the same architecture, don&#8217;t install JDK/JRE from the package tree. If you&#8217;re able to emulate Linux code (throught Kernel configuration &#8212; check this article[ here][2]), just download following files:

1) <a onclick="s_linkType='d';s_linkName='cds:jdk-1_5_0_16-linux-i586.bin';s_linkTrackVars='events,products,eVar3,eVar8';s_linkTrackEvents='event7';s_events='event7';s_products='Download Products;Java SE Development Kit 5.0u16  ';s_eVar3='cds';s_eVar8='jdk-1_5_0_16-linux-i586.bin';s_lnk=s_co(this);s_gs(s_account);" href="http://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/VerifyItem-Start/jdk-1_5_0_16-linux-i586.bin?BundledLineItemUUID=QqVIBe.pjF4AAAEiVpUHkxz5&OrderID=FRVIBe.pnigAAAEiRJUHkxz5&ProductID=08hIBe.nqCUAAAEaC7xVHpdD&FileName=/jdk-1_5_0_16-linux-i586.bin">jdk-1_5_0_16-linux-i586.bin</a>

2) <a onclick="s_linkType='d';s_linkName='cds:jre-1_5_0_16-linux-i586.bin';s_linkTrackVars='events,products,eVar3,eVar8';s_linkTrackEvents='event7';s_events='event7';s_products='Download Products;Java SE Runtime Environment 5.0u16  ';s_eVar3='cds';s_eVar8='jre-1_5_0_16-linux-i586.bin';s_lnk=s_co(this);s_gs(s_account);" href="http://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/VerifyItem-Start/jre-1_5_0_16-linux-i586.bin?BundledLineItemUUID=ERNIBe.ph0oAAAEiTQcHkxz6&OrderID=T0xIBe.p2TMAAAEiOgcHkxz6&ProductID=MlNIBe.ptoUAAAEaKPwkfJxw&FileName=/jre-1_5_0_16-linux-i586.bin"> jre-1_5_0_16-linux-i586.bin</a>

Then make sure you extract the content in &#8220;/usr/pkg/java/sun-1.5/&#8221;. Then you should be able to run Netbeans without any errors.

&nbsp;

<!--break-->

&nbsp;

 [1]: http://www.netbeans.org/community/releases/67/index.html
 [2]: http://wiki.netbsd.se/How_to_run_NetBeans_IDE_on_NetBSD
