










 


Strategies







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategies_account.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Strategies | [Previous page](simulationaccountreset.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


A collection of StrategyBase objects generated for the specified account


 


Property Value
--------------


An [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of StrategyBase objects


 


Syntax
------


<account>.Strategies



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
 
private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
   foreach (StrategyBase strategy in myAccount.Strategies)
   {
       Print(String.Format("Account status updated. {0} strategy applied with position {1}", strategy.Name, strategy.Position));
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