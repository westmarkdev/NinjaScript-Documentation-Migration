










 


IsInStrategyAnalyzer







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isinstrategyanalyer.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IsInStrategyAnalyzer | [Previous page](isinstantiatedoneachoptimizationiteration.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if the current NinjaScript Strategy is run from a Strategy Analyzer chart.


 


Property Value
--------------


A bool value when true the strategy is being run from the Strategy Analyzer chart; otherwise will return false.


 


Syntax
------


IsInStrategyAnalyzer


 


Examples
--------


 




| ns |
| --- |
|  | protected override void OnBarUpdate()
{
    // Only draw the ArrowUp on our condition if we're not in the Strategy Analyzer chart
   if (Close[0] &gt; SMA(High, 14)[0] &amp;&amp; !IsInStrategyAnalyzer)
       Draw.ArrowUp(this, CurrentBar.ToString(), true, 0, High[0] + TickSize, Brushes.Blue);
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
 
 
 



