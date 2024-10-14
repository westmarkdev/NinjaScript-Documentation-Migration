










 


ShowTransparentPlotsInDataBox







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?showtransparentplotsindatabox.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
ShowTransparentPlotsInDataBox | [Previous page](paintpricemarkers.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


Determines if plot(s) values which are set to a Transparent brush display in the chart data box.  The default behavior is to hide any plots which have been configured as a Transparent brush, however this behavior can be changed by setting ShowTransparentPlotsInDataBox to true on the indicator.


 


Property Value
--------------


This property returns true if transparent indicator plot(s) values display in the chart data box; otherwise, false. Default set to false.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


ShowTransparentPlotsInDataBox



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         ShowTransparentPlotsInDataBox = true;   
         AddPlot(Brushes.Transparent, "MyPlot");
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
 
 
 



