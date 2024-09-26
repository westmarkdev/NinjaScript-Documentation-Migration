










 


TraceOrders







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?traceorders.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
TraceOrders | [Previous page](timeinforce.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if OnOrderTrace() would be called for a given strategy.  When enabled, traces are generated and displayed in the [NinjaScript Output](output.htm) window for each call of an [order method](order_methods.htm) providing confirmation that the method is entered and providing information if order methods are ignored and why. This is valuable for debugging if you are not seeing expected behavior when calling an order method. This property can be set programatically in the [OnStateChange()](onstatechange.htm) method.


   

The output will reference a method "PlaceOrder()" which is an internal method that all Enter() and Exit() methods use.



Property Value
--------------


This property returns true if the strategy will output trace information; otherwise, false.  Default value is false.


 


Syntax
------


TraceOrders


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         TraceOrders = true;
     }
} |



 




|  |
| --- |
| Tips
1.See [this](traceorders2.htm) article for more examples of how to utilize this property.2.You can override the default output by using OnOrderTrace() in your strategy. |






 
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
 
 
 



