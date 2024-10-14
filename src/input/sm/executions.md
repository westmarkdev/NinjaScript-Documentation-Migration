










 


Executions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?executions.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Executions | [Previous page](denomination.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


A collection of Execution objects generated for the specified account. These are the current sessions executions and should match executions reported in the Executions tab of the NinjaTrader Account Data window. 


 


Property Value
--------------


An [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of Execution objects


 


Syntax
------


<account>.Executions


 




|  |
| --- |
| Note: At this time there is not a supported method to retrieve historical executions from the local database.  |




Examples
--------




| ns |
| --- |
|  
private Account myAccount;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Initialize myAccount
   }
}
 
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   foreach (Execution execution in myAccount.Executions)
   {
       Print(String.Format("Execution triggered for Order {0}", execution.Order));
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
 
 
 



</account>