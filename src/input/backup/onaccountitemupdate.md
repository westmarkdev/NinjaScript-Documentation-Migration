










 


OnAccountItemUpdate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onaccountitemupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OnAccountItemUpdate() | [Previous page](numberrestartattempts.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


An event driven method used for strategies which is called for each AccountItem update for the account on which the strategy is running.





|  |
| --- |
| Note:  OnAccountItemUpdate() will be called continually in real-time if a position exists on the account on which the strategy is running. This is to provide updates on the current Unrealized Profit and Loss and associated risk values. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
You must override the method in your strategy with the following syntax:
-------------------------------------------------------------------------------


protected override void OnAccountItemUpdate(Account account, AccountItem accountItem, double value)
{ 
 
}
----------------------------------------------------------------------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| account | The [Account](account_class.htm) updated |
| accountItem | The [AccountItem](accountitem.htm) updated |
| value | The value of the AccountItem updated |



 



Examples
--------




| ns |
| --- |
| protected override void OnAccountItemUpdate(Account account, AccountItem accountItem, double value)
{ 
   Print(string.Format("{0} {1} {2}", account.Name, accountItem, value));
   
   // output:
   // Sim101 BuyingPower 103962.5
   // Sim101 CashValue 103962.5
   // Sim101 GrossRealizedProfitLoss 3962.5
   // Sim101 RealizedProfitLoss 3962.5
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
 
 
 



