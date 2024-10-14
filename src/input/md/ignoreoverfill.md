










 


IgnoreOverfill







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ignoreoverfill.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Unmanaged Approach](unmanaged_approach.htm) &gt;
IgnoreOverfill | [Previous page](unmanaged_changeorder.htm)
[Return to chapter overview](unmanaged_approach.htm)










Definition
----------


An [unmanaged order property](unmanaged_approach.htm) which defines the behavior of a strategy when an overfill is detected. An overfill is categorized as when an order returns a "Filled" or "PartFilled" state after the order was already marked for cancellation. The cancel request could have been induced by an explicit CancelOrder() call, from more implicit cancellations like those that occur when another order sharing the same OCO ID is filled, or from things like order expiration.


 




|  |
| --- |
| Critical:
•Setting this property value to true can have serious adverse affects on a running strategy unless you have programmed your own overfill handling •User defined overfill handling is advanced and should ONLY be addressed by experienced programmers. Additional information can be found on overfills in the [Unmanaged approach](unmanaged_approach.htm) section |



 


 


Property Value
--------------


This property returns true if the strategy will ignore overfills; otherwise, false. Default is set to false. 


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IgnoreOverfill


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Allows for custom overfill handling
       IgnoreOverfill = true;
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
 
 
 



