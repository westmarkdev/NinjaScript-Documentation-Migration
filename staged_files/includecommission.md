










 


IncludeCommission







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?includecommission.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IncludeCommission | [Previous page](exitonsessioncloseseconds.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if the strategy performance results will include commission on a historical backtest. When true, the [Commission Template](understanding_commissions.htm) applied to the account on which the strategy is running will be used.


 


Property Value
--------------


A bool value which returns true if the strategy includes commission on a historical backtest; otherwise, false.  Default value is set to false.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IncludeCommission



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         IncludeCommission = true;
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
 
 
 



