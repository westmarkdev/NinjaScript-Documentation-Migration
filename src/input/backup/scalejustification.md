










 


ScaleJustification







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?scalejustification.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
ScaleJustification | [Previous page](isseparatezorder.htm)
[Return to chapter overview](chart.htm)










Definition
----------


Determines which scale an indicator will be plotted on.





|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Property Value
--------------


This property returns a ScaleJustification value of either:


 


NinjaTrader.Gui.Charts.ScaleJustification.Left;  

NinjaTrader.Gui.Charts.ScaleJustification.Overlay;  

NinjaTrader.Gui.Charts.ScaleJustification.Right;


 


 


Syntax
------


ScaleJustification


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";   
 
     // force "My Plot" to be plotted on the left scale
     ScaleJustification = ScaleJustification.Left;  
   }
   else if (State == State.Configure)
   {            
     AddPlot(Brushes.Orange, "My Plot");
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
 
 
 



