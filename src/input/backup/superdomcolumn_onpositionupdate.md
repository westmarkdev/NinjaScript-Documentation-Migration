










 


OnPositionUpdate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?superdomcolumn_onpositionupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
OnPositionUpdate() | [Previous page](superdomcolumn_onorderupdate.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


Called every time a [position](position.htm) changes state.


 




|  |
| --- |
| Note:  The OnPositionUpdate() method is called on ALL position updates (e.g., any account and instrument combination) and NOT just the specific items which are selected in the SuperDOM. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


protected override void OnPositionUpdate(PositionEventArgs positionUpdate)  

{


   

}


 


Method Parameters
-----------------




|  |  |
| --- | --- |
| positionUpdate | A PositionEventArgs representing the change in position |





Examples
--------




| ns |
| --- |
| protected override void OnPositionUpdate(PositionEventArgs positionUpdate)
{
   // Do not take action if the position update does not come from the selected SuperDOM instrument/account
   if (positionUpdate.Position.Instrument != SuperDom.Instrument 
     || positionUpdate.Position.Account != SuperDom.Account)
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
 
 
 



