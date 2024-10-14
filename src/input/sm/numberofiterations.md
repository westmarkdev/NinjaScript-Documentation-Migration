










 


NumberOfIterations







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?numberofiterations.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimizer](optimizer.htm) &gt;
NumberOfIterations | [Previous page](optimizer.htm)
[Return to chapter overview](optimizer.htm)










Definition
----------


Informs the Strategy Analyzer how many iterations of optimizing it needs to do.


 


Property Value
--------------


An int value.


 


Syntax
------


NumberOfIterations


 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
         Name = "MyOptimizer";
     else if (State == State.Configure &amp;&amp; Strategies.Count &gt; 0)
         NumberOfIterations = 1;
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
 
 
 



