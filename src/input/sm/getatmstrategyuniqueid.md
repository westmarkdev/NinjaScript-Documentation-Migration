










 


GetAtmStrategyUniqueId()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategyuniqueid.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyUniqueId() | [Previous page](getatmstrategyunrealizedprofit.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Generates a unique ATM Strategy ID value. 


 


Method Return Value
-------------------


A string value representing a unique id value.



Syntax
------


GetAtmStrategyUniqueId()


 


Parameters
----------


This method does use take any parameters.


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     string orderId = GetAtmStrategyUniqueId();
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
 
 
 



