










 


Slippage







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?slippage.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Slippage | [Previous page](setorderquantity.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Sets the amount of slippage in ticks per execution used in performance calculations during backtests.


 


Property Value
--------------


An int value representing the number ticks.  Default value is set to 0.


 


Syntax
------


Slippage


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         Slippage = 2; 
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
 
 
 



