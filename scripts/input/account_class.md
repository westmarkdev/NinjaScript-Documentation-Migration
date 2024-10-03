










 


Account







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?account_class.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
Account | [Previous page](quantityupdown.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


The Account class can be used to subscribe to account related events as well as accessing account related information.


 


Static Account Class Properties
-------------------------------




|  |  |
| --- | --- |
| [All](all.htm) | A collection of Account objects |
| [AccountStatusUpdate](accountstatusupdate.htm) | Event handler for account status updates |
| [SimulationAccountReset](simulationaccountreset.htm) | Event handler for resets on sim accounts
 
NOTE: Also happens when rewinding/fast forwarding Playback connections) |



 


Methods and Properties From Account instances
---------------------------------------------




|  |  |
| --- | --- |
| [AccountItem](accountitem.htm) | Represents various account variables used to reflect values the status of the account |
| [AccountItemUpdate](accountitemupdate.htm) | Event handler for changes to account values |
| [Cancel()](cancel.htm) | Cancels specified order(s) on the account |
| [CancelAllOrders()](accounts_cancelallorders.htm) | Cancels all orders of an instrument on the account |
| [Change()](change.htm) | Changes specified order(s) on the account |
| [Connection](connection.htm) | A Connection representing the connection this account is associated with |
| [CreateOrder()](createorder.htm) | Creates orders for the account that need to be submitted via Submit() |
| [Denomination](denomination.htm) | A Currency representing the denomination currency of this connection |
| [Executions](executions.htm) | A collection of executions on this account |
| [ExecutionUpdate](executionupdate.htm) | Event handler for when new executions come in, an existing execution is amended, or an execution is removed |
| [Flatten()](flatten.htm) | Flattens the account on specified instrument(s) |
| [Get()](get.htm) | Returns the value of an [AccountItem](accountitem.htm) |
| [Name](name_account.htm) | A string representing the name of this account |
| [Orders](orders_account.htm) | A collection of orders on this account |
| [OrderUpdate](orderupdate.htm) | Event handler for changes to orders |
| [Positions](positions_account.htm) | A collection of positions on this account |
| [PositionUpdate](positionupdate.htm) | Event handler for changes to positions |
| [Strategies](strategies_account.htm) | A collection of strategies on this account |
| [Submit()](submit.htm) | Submits specified order(s) |



 


 


Example
-------




| ns |
| --- |
| private Account myAccount;
 
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Find our Sim101 account
         lock (Account.All)
               myAccount = Account.All.FirstOrDefault(a =&gt; a.Name == "Sim101");
 
         // Subscribe to static events. Remember to unsubscribe with -= when you are done
         Account.AccountStatusUpdate += OnAccountStatusUpdate;
 
         if (myAccount != null)
         {
               // Print some information about our account using the AccountItem indexer
               Print(string.Format("Account Name: {0} Connection Name: {1} Cash Value {2}",
                   myAccount.Name,
                   myAccount.Connection.Options.Name,
                   myAccount.Get(AccountItem.CashValue, Currency.UsDollar)
                   ));
 
               // Print the prices of the executions on our account
               lock (myAccount.Executions)
                   foreach (Execution execution in myAccount.Executions)
                         Print("Price: " + execution.Price);
 
               // Subscribe to events. Remember to unsubscribe with -= when you are done
               myAccount.AccountItemUpdate += OnAccountItemUpdate;
               myAccount.ExecutionUpdate += OnExecutionUpdate;
         }
     }
     else if (State == State.Terminated)
     {
         // Unsubscribe to events
         myAccount.AccountItemUpdate -= OnAccountItemUpdate;
         myAccount.ExecutionUpdate -= OnExecutionUpdate;
          Account.AccountStatusUpdate -= OnAccountStatusUpdate;
     }
}
 
private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
     // Do something with the account status update
}
 
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
     // Do something with the account item update
}
 
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
     // Do something with the execution update
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
 
 
 



