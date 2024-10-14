










 


OnOrderUpdate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?superdomcolumn_onorderupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
OnOrderUpdate() | [Previous page](superdomcolumn_onmarketdata.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


Called every time an [order](order.htm) changes state. An order will change state when a change in order quantity, price or state (e.g. working to filled) occurs.


 




|  |
| --- |
| Note:  The OnOrderUpdate() method is called on ALL order updates (e.g., any account and instrument combination) and NOT just the specific items which are selected in the SuperDOM. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


protected override void OnOrderUpdate(OrderEventArgs orderUpdate)  

{  

   

}


 


Method Parameters
-----------------




|  |  |
| --- | --- |
| orderUpdate | An OrderEventArgs representing the change in order state |





Examples
--------




| ns |
| --- |
| protected override void OnOrderUpdate(OrderEventArgs orderUpdate)
{
   // Do not take action if the order update does not come from the selected SuperDOM instrument/account
   if (orderUpdate.Order.Instrument != SuperDom.Instrument || orderUpdate.Order.Account != SuperDom.Account)
     return;
 
   // Do something
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
 
 
 



