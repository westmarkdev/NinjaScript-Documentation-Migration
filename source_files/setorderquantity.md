










 


SetOrderQuantity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?setorderquantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
SetOrderQuantity | [Previous page](restartswithinminutes.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines how order sizes are calculated for a given strategy.


 


Property Value
--------------


An enum determining how order quantities are set.  Default value is set to SetOrderQuantity.Strategy. 


 


Possible values are:




|  |  |
| --- | --- |
| SetOrderQuantity.DefaultQuantity | User defined order size based on the [DefaultQuantity](defaultquantity.htm) property |
| SetOrderQuantity.Strategy | Takes the order size specified programmatically within the strategy  |






|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |




 


Syntax
------


SetOrderQuantity


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         SetOrderQuantity = SetOrderQuantity.DefaultQuantity; // calculate orders based off default size
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
 
 
 



