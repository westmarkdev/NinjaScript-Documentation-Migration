










 


Submit()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?submit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Submit() | [Previous page](strategies_account.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Submits specified [Order](order.htm) object(s).


 


Syntax
------


Submit(IEnumerable<order> orders)


 


Parameters
----------




|  |  |
| --- | --- |
| orders | Order(s) to submit |



 


 



Examples
--------




| ns |
| --- |
| Order stopOrder = null;
stopOrder = myAccount.CreateOrder(myInstrument, OrderAction.Sell, OrderType.StopMarket, TimeInForce.Day, 1, 0, 1400, "myOCO", "stopOrder", null);
 
myAccount.Submit(new[] { stopOrder }); |






 
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
 
 
 



</order>