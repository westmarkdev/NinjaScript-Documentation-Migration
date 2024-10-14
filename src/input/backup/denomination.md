










 


Denomination







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?denomination.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
Denomination | [Previous page](createorder.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Indicates the currency set on an account


 


Property Value
--------------


A Currency object containing information about the currency denomination specified in the referenced account


 


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
     // Initialize myAccount here
 
     // Print myAccount's currency denomination
     NinjaTrader.Code.Output.Process("myAccount currency is set to " + myAccount.Denomination, PrintTo.OutputTab1);
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