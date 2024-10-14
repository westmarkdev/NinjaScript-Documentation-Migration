










 


OnOptimize()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onoptimize.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimizer](optimizer.htm) &gt;
OnOptimize() | [Previous page](numberofiterations.htm)
[Return to chapter overview](optimizer.htm)










Definition
----------


This method must be overridden in order to optimize a strategy. This method is called once per optimization run (not once per iteration).


 


Method Return Value
-------------------


This method does not return a value.



Syntax
You must override the method in your Optimizer with the following syntax.
--------------------------------------------------------------------------------


 


protected override void OnOptimize()   

{


   

}


 


 



Examples
--------




| ns |
| --- |
| protected override void OnOptimize()
{
     // If there is no optimization objective, return
     if (Strategies[0].OptimizationParameters.Count == 0)
         return;
 
     // Optimizer logic
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
 
 
 



