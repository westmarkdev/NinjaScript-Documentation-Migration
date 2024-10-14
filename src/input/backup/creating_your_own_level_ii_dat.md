










 


Creating your own Level II data book (Accessing market depth)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?creating_your_own_level_ii_dat.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Creating your own Level II data book (Accessing market depth) | [Previous page](creating_a_user-defined_parame.htm)
[Return to chapter overview](indicator2.htm)










Level II data is important for the momentum trader. It allows them to determine which way the market makers are trading and can be useful in helping the trader decide which way the momentum is going.


 


Key concepts in this example
----------------------------


•Storing Level II data in a custom object list

•Printing Level II books for discretionary trading

 


Important related documentation
-------------------------------


•[List&lt;&gt;](https://msdn.microsoft.com/en-us/library/6sh2ey19(v=vs.110).aspx)

•[MarketDepthEventArgs](marketdeptheventargs.htm)

•[Operation](operations.htm)

•[Position](position.htm)

•[Price](price.htm)

•[Volume](volume.htm)

•[Time](time.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleLevel2Book\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleLevel2Book_NT8.zip)





 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



