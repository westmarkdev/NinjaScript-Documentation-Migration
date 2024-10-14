










 


DefaultQuantity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?defaultquantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
DefaultQuantity | [Previous page](daystoload.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


An order size variable that can be set either programmatically or overriden via the Strategy that determines the quantity of an entry order.


 


Property Value
--------------


An int value represents the number of contracts or shares to enter a position with.  Default value is 1.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |





Syntax
------


DefaultQuantity


 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange() 
{
     if (State == State.SetDefaults)
     {
         DefaultQuantity = 1;
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
 
 
 



