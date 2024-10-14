










 


GetAtmStrategyEntryOrderStatus()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategyentryorderstatus.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyEntryOrderStatus() | [Previous page](atmstrategycreate.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the current state of the specified entry order. 


 




|  |
| --- |
| Note:  If the method can't find the specified order, an empty array is returned. |



 


 


Method Return Value
-------------------


A string[] array holding three elements that represent average fill price, filled amount and order state.



Syntax
------


GetAtmStrategyEntryOrderStatus(string orderId)



Parameters
----------




|  |  |
| --- | --- |
| orderId | The unique identifier for the entry order |



 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     string[] entryOrder = GetAtmStrategyEntryOrderStatus("orderId");
 
     // Check length to ensure that returned array holds order information
     if (entryOrder.Length &gt; 0)
     {
         Print("Average fill price is " + entryOrder[0].ToString());
         Print("Filled amount is " + entryOrder[1].ToString());
         Print("Current state is " + entryOrder[2].ToString());
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
 
 
 



