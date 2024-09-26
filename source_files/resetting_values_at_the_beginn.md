










 


Resetting values at the beginning of new trading sessions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?resetting_values_at_the_beginn.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Resetting values at the beginning of new trading sessions | [Previous page](removing_draw_objects_from_the.htm)
[Return to chapter overview](strategy2.htm)










Normally calculated values are carried over between trading sessions, but sometimes you may want to reset these values to begin a trading session fresh. The technique demonstrated in this reference sample can be useful to do things like resetting counters you may be running or clearing bool flags you may have set.


 


Key concepts in this example
----------------------------


•Resetting a variable at the beginning of a new trading session

•Limiting the number of trades a strategy can make per trading session

 


Important related documentation
-------------------------------


•[IsFirstBarOfSession](isfirstbarofsession.htm)

•[IsFirstTickOfBar](isfirsttickofbar.htm)

•[EnterLong()](enterlong.htm)

•[ExitLong()](exitlong.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


<https: helpguides="" ninjatrader.com="" nt8="" samples="" sampletradelimiter_nt8.zip="" support="">





 
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
 
 
 



</https:>