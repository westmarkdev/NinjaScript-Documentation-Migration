










 


CancelAllOrders()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?accounts_cancelallorders.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
CancelAllOrders() | [Previous page](cancel.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Cancels all [Order](order.htm)s of an instrument.


 


Syntax
------


CancelAllOrders(Instrument instrument)


 


Parameters
----------




|  |  |
| --- | --- |
| instrument | Instrument of the orders to be cancelled |



 


 


Example
-------




| ns |
| --- |
| private Account myAccount;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Initialize myAccount
   }
}
 
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   // Cancel all orders if an execution is triggered after 9pm
   if (e.Time &gt; new DateTime(now.Year, now.Month, now.Day, 21, 0, 0))
       myAccount.CancelAllOrders(e.Execution.Instrument);
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
 
 
 



