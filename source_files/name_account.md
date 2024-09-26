










 


Name







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?name_account.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Name | [Previous page](get.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Indicates the name of the specified account


 


Property Value
--------------


An string representing the name of the account


 


Syntax
------


<account>.Name



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
 
private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
   // Print the name of each account updated
   Print(String.Format("{0} account updated", myAccount.Name));
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