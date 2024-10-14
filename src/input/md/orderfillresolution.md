










 


OrderFillResolution







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?orderfillresolution.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OrderFillResolution | [Previous page](submitorderunmanaged.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines how strategy orders are filled during historical states.  


 


Please see [Understanding Historical Fill Processing](understanding_historical_fill_.htm) for general information on historical fill processing.


 


Property Value
--------------


An enum value that determines how the strategy orders are filled.  Default value is set to OrderFillResolution.Standard.  Possible values are:




|  |  |
| --- | --- |
| OrderFillResolution.Standard  | Faster - Uses the existing bar type and interval that you are running the backtest on to fill your orders.   |
| OrderFillResolution.High | More granular - Allows you to set a secondary bar series to be used as the price data to fill your orders.   (See also [OrderFillResolutionType](orderfillresolutiontype.htm) and [OrderFillResolutionValue](orderfillresolutionvalue.htm)) |



 


Syntax
OrderFillResolution
--------------------------


 




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
     OrderFillResolution = OrderFillResolution.Standard;
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
 
 
 



