










 


GetInitialLookBackDays()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getinitiallookbackdays.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
GetInitialLookBackDays() | [Previous page](defaultchartstyle.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Determines how many days of data load when a user makes a "bars back" data request.


 


Method Return Value
-------------------


This method returns an int value.



Method Parameters
-----------------




|  |  |
| --- | --- |
| barsPeriod | The [bars period](barsperiod.htm) chosen by the user when utilizing this Bars type |
| tradingHours | The [trading hours](tradinghours.htm) chosen by the user when utilizing this Bars type |
| barsBack | The bars back chosen by the user when utilizing this Bars type |



 


Syntax
You must override the method in your Bars Type with the following syntax.
--------------------------------------------------------------------------------


   

public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)   

{  

   

}


 



Examples
--------




| ns |
| --- |
| public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)
{
     // Returns the minimum number of days needed to successfully load the number
     // of bars back requested for a monthly Bars type
     return (int) barsPeriod.Value * barsBack * 31;
} |



 


 




|  |
| --- |
| Tip:  Try to request an amount of data that is just right for what is needed. Requesting too large a data set will result in unnecessary data being loaded. Requesting too small a data set will result in multiple requests being done. |






 
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
 
 
 



