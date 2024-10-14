










 


IsAutoScale







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isautoscale.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
IsAutoScale | [Previous page](formatpricemarker.htm)
[Return to chapter overview](chart.htm)










Definition
----------


If true, the object will call [CalculateMinMax()](oncalculateminmax.htm) in order to determine the object's [MinValue](minvalue.htm) and [MaxValue](maxvalue.htm) value used to scale the Y-axis of the chart.



Property Value
--------------


This property returns true if the object's are included in the y-scale; otherwise, false. Default set to false for [DrawingTools](drawing_tools.htm), but set to true for [Indicators](indicator.htm).


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |




Syntax
------


IsAutoScale



Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {         
     Name                 = "Example Indicator";         
     // set this to true to call CalculateMinMix() to ensure drawing tool is fully rendered in chart scale
     IsAutoScale = true;  
   }
   else if (State == State.Configure)
   {
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
 
 
 



