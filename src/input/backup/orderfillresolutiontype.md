










 


OrderFillResolutionType







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?orderfillresolutiontype.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OrderFillResolutionType | [Previous page](orderfillresolution.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the bars type which will be used for historical fill processing.





|  |
| --- |
| Note: This property will only be valid if the [OrderFillResolution](orderfillresolution.htm) is set to OrderFillResolution.High |





Property Value
--------------


A [BarsPeriodType](barsperiod.htm) representing the type of bars during historical order processing.  Default value is set to BarsPeriodType.Minute.


 


Syntax
OrderFillResolutionType
------------------------------





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
 
 
 



