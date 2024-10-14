










 


Change()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?change.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Change() | [Previous page](accounts_cancelallorders.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Changes specified [Order](order.htm) object(s).


 


Syntax
------


Change(IEnumerable<order> orders)


 


Parameters
----------




|  |  |
| --- | --- |
| orders | Order(s) to change |



 



Example
-------




| ns |
| --- |
| Order stopOrder;
stopOrder.StopPriceChanged = stopOrder.StopPrice - 4 * stopOrder.Instrument.MasterInstrument.TickSize;
 
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   // Change the stop order if an execution results in a long position
   if(e.MarketPosition == MarketPosition.Long)
       myAccount.Change(new[] { stopOrder });
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
 
 
 



</order>