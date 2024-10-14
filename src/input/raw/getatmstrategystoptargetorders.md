










 


GetAtmStrategyStopTargetOrderStatus()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategystoptargetorders.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyStopTargetOrderStatus() | [Previous page](getatmstrategyrealizedprofitlo.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the current order state(s) of the specified stop or target order of a still-active ATM strategy.


 




|  |
| --- |
| Notes:  
1.If the method can't find the specified order(s), an empty array is returned.2.A specified stop or target within an ATM strategy can actually hold multiple orders. For example, if your ATM strategy submits a stop and target and you receive multiple partial fills on entry with a delay of a few seconds or more between entry fills, the ATM strategy will submit stop and target orders for each partial fill all with the same price and order type. |



 


Method Return Value
-------------------


A string[,] multi-dimensional array holding three dimensions that represent average fill price, filled amount and [order state](order_state_definitions.htm). The length (number of elements) represents the number of orders that represent the specified name.



Syntax
------


GetAtmStrategyStopTargetOrderStatus(string orderName, string atmStrategyId)


 



Parameters
----------




|  |  |
| --- | --- |
| orderName | The order name such as "Stop1" or "Target2" |
| atmStrategyId | The unique identifier for the ATM strategy |



 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     string[,] orders = GetAtmStrategyStopTargetOrderStatus("Target1", "idValue");
 
     // Check length to ensure that returned array holds order information
     if (orders.Length &gt; 0)
     {
         for (int i = 0; i &lt; orders.GetLength(0); i++)
         {
               Print("Average fill price is " + orders[i, 0].ToString());
               Print("Filled amount is " + orders[i, 1].ToString());
               Print("Current state is " + orders[i, 2].ToString());
         }
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
 
 
 



