










 


Instrument







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?position_instrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Position](position.htm) &gt;
Instrument | [Previous page](position_getunrealizedprofitloss.htm)
[Return to chapter overview](position.htm)










Definition
----------


Gets the instrument of a strategy position.


 


Property Value
--------------


An [Instrument](instrument.htm) representing the position's instrument.



Syntax
------


Position.Instrument


 



Examples
--------




| ns |
| --- |
| protected override void OnPositionUpdate(Position position, double averagePrice, int quantity, MarketPosition marketPosition)
{
     // If the position is an AAPL position
     if (position.Instrument.MasterInstrument.Name == "AAPL")
   {
         //do something    
   }
}    |






 
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
 
 
 



