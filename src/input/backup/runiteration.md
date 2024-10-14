










 


RunIteration()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?runiteration.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimizer](optimizer.htm) &gt;
RunIteration() | [Previous page](optimizationparameters.htm)
[Return to chapter overview](optimizer.htm)










Definition
----------


Runs an iteration of backtesting for the optimizer


 


Method Return Value
-------------------


This method does not return a value.



Syntax
------


RunIteration()


 


 



Examples
--------




| ns |
| --- |
| protected override void OnOptimize()
{
     // Optimizer logic
     RunIteration();
} |






 
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
 
 
 



