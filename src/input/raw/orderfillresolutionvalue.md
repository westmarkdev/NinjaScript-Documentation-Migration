










 


OrderFillResolutionValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?orderfillresolutionvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OrderFillResolutionValue | [Previous page](orderfillresolutiontype.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the bars period interval value which will be used for historical fill processing.





|  |
| --- |
| Note: This property will only be valid if the [OrderFillResolution](orderfillresolution.htm) is set to OrderFillResolution.High |




Property Value
--------------


A int representing the interval used for the bars period during historical order processing.  Default value is set to 1.


 


Syntax
OrderFillResolutionValue
-------------------------------


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {            
     Name = "ExampleStrategy";
 
     // use one second bars for filling orders
     OrderFillResolution       = OrderFillResolution.High;               
     OrderFillResolutionType   = BarsPeriodType.Second;
     OrderFillResolutionValue   = 1; 
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
 
 
 



