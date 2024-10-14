










 


Get()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?get.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Get() | [Previous page](flatten.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Returns the value of an AccountItem, such as BuyingPower, CashValue, etc.  

 


Method Return Value
-------------------


A double representing the value of the requested AccountItem


 


Syntax
------


Get(AccountItem itemType, Cbi.Currency currency)


 


Parameters
----------




|  |  |
| --- | --- |
| itemType | The desired AccountItem to return |
| Currency | The account currency the value should be denoted (required parameter, but has no effect on returned value) |



 



Examples
--------




| ns |
| --- |
| // Evaluates to see if the account has more than $25000
if (Account.Get(AccountItem.CashValue, Currency.UsDollar) &gt; 25000)
{
   // Do something;
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
 
 
 



