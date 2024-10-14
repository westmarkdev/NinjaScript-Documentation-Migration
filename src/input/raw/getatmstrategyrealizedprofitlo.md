﻿










 


GetAtmStrategyRealizedProfitLoss()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategyrealizedprofitlo.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyRealizedProfitLoss() | [Previous page](getatmstrategypositionquantity.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the realized profit and loss value of the specified ATM Strategy.


 


Method Return Value
-------------------


A double value representing the realized profit and loss.



Syntax
------


GetAtmStrategyRealizedProfitLoss(string atmStrategyId)


 



Parameters
----------




|  |  |
| --- | --- |
| atmStrategyId | The unique identifier for the ATM strategy |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     Print("PnL is " + GetAtmStrategyRealizedProfitLoss("id").ToString());
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
 
 
 


