










 


Orders







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?orders_account.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Orders | [Previous page](name_account.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


A collection of Order objects generated for the specified account


 


Property Value
--------------


An [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of Order objects


 




|  |
| --- |
| Note: Please keep in mind that orders placed when in State.Historical are not submitted live to an account.  |



 


Syntax
------


<account>.Orders



Examples
--------




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
 
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
   // Print the name and order action of each order processed on the account
   foreach (Order order in myAccount.Orders)
   {
       Print(String.Format("Order placed: {0} - {1}", order.Name, order.OrderAction));
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