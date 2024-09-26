










 


PriceStatus







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connections_pricestatus.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Connection](connection_class.htm) &gt;
PriceStatus | [Previous page](connections_options.htm)
[Return to chapter overview](connection_class.htm)










Definition
----------


Indicates the current status of the price feed of the primary data connection


 


Syntax
------


<connection>.PriceStatus


 


 


Example
-------




| ns |
| --- |
| private int priceLost;
private int mainLost;
 
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
   // Count the number of times OnAccountItemUpdate() is called with a lost price connection
   if (myAccount.Connection.PriceStatus == ConnectionStatus.ConnectionLost)
       priceLost += 1;
 
   // Count the number of times OnAccountItemUpdate() is called with a lost primary connection
   if (myAccount.Connection.Status == ConnectionStatus.ConnectionLost)
       mainLost += 1;
 
   // Print the number of times each connection was lost during OnAccountItemUpdate()
   if (mainLost &gt; 0 || priceLost &gt; 0)
       Print(String.Format("Main connection lost {0} times. Price feed lost {1} times.", mainLost, priceLost));
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
 
 
 



</connection>