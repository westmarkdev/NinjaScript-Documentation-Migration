










 


Connection







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connection.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Connection | [Previous page](change.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Indicates the data connection used for the specified account.


 


Property Value
--------------


An instance of the Connection class containing information about the connection used for a specified account


 


Syntax
------


<account>.Connection



Examples
--------




| ns |
| --- |
| private Account myAccount;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       myAccount = Account.All.FirstOrDefault(a =&gt; a.Name == "Sim101");
   }
}
 
private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
   Print(String.Format("{0} connection updated", myAccount.Connection.Options.Name));
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