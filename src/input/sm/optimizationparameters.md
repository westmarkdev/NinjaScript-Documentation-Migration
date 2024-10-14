










 


OptimizationParameters







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?optimizationparameters.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimizer](optimizer.htm) &gt;
OptimizationParameters | [Previous page](onoptimize.htm)
[Return to chapter overview](optimizer.htm)










Definition
----------


The optimization parameters selected for the optimization run. (e.g. user parameters or Data Series)


 


Property Value
--------------


A bool value.


 


Syntax
------


Strategies[0].OptimizationParameters


 


 


Examples
--------




| ns |
| --- |
| protected override void OnOptimize()
{
     // If there are no optimization parameters to optimize, return
     if (Strategies[0].OptimizationParameters.Count == 0)
         return;
 
     // Do something with the optimization parameter
     Parameter parameter = Strategies[0].OptimizationParameters[0];
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
 
 
 



