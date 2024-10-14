










 


All







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?all.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
All | [Previous page](accountstatusupdate.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


A collection of Account objects


 


Property Value
--------------


A [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of Account objects


 


Syntax
------


Accounts.All



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.DataLoaded)
   {
       foreach (Account sampleAccount in Account.All)
    Print(String.Format("The account {0} has a {1} unit FX lotsize set", sampleAccount.Name, sampleAccount.ForexLotSize));
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
 
 
 



