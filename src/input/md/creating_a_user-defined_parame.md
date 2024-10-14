










 


Creating a user-defined parameter type (enum)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?creating_a_user-defined_parame.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Creating a user-defined parameter type (enum) | [Previous page](coloring_a_region.htm)
[Return to chapter overview](indicator2.htm)










Creating user-defined parameters allows you to present the user with hard coded options they can choose. These options provide flexibility in your indicators and can be of value to the user if they like to switch settings often.


 


Key concepts in this example
----------------------------


•Hard code various Moving Average types the user can select

•Use a switch to determine which code logic is executed based on the Moving Average type selected

 


Important related documentation
-------------------------------


•[enum](http://csharp-station.com/Tutorial/CSharp/Lesson17)

•[branching statements](http://csharp-station.com/Tutorial/CSharp/Lesson03)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleUniversalMovingAverage\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleUniversalMovingAverage_NT8.zip)





 
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
 
 
 



