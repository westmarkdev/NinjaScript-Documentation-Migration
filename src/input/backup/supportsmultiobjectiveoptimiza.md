










 


SupportsMultiObjectiveOptimization







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?supportsmultiobjectiveoptimiza.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimizer](optimizer.htm) &gt;
SupportsMultiObjectiveOptimization | [Previous page](runiteration.htm)
[Return to chapter overview](optimizer.htm)










Definition
----------


Informs the Strategy Analyzer if this Optimizer can do multi-objective optimizations.


 


Property Value
--------------


A bool value.


 


Syntax
------


SupportsMultiObjectiveOptimization


 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          Name = "MyOptimizer";
          SupportsMultiObjectiveOptimization = true;
     }
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
 
 
 



