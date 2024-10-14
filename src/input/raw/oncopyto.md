










 


OnCopyTo()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?oncopyto.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Performance Metrics](performance_metrics.htm) &gt;
OnCopyTo() | [Previous page](onaddtrade.htm)
[Return to chapter overview](performance_metrics.htm)










Definition
----------


Called as the values of a trade metric are saved.


 


Syntax
------


protected override void OnCopyTo(PerformanceMetricBase target)  

{  

     

}



Examples
--------




| ns |
| --- |
| protected override void OnCopyTo(PerformanceMetricBase target)
{
   // You need to cast, in order to access the right type
   SampleCumProfit targetMetrics = (target as SampleCumProfit);
 
   if (targetMetrics != null)
     Array.Copy(Values, targetMetrics.Values, Values.Length);
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
 
 
 



