










 


Cancel()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?cancel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Cancel() | [Previous page](all.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Cancels specified [Order](order.htm) object(s).


 


Syntax
------


Cancel(IEnumerable<order> orders)


 


Parameters
----------




|  |  |
| --- | --- |
| orders | Order(s) to cancel |



 



Examples
--------




| ns |
| --- |
| private Account myAccount;
Order stopOrder = null;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Initialize myAccount
   }
}
 
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   // Cancel the stop order if an execution results in a long position
   if(e.MarketPosition == MarketPosition.Long)
       myAccount.Cancel(new[] { stopOrder });
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