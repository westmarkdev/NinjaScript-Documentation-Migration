










 


GetCurrentBid()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getcurrentbid.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
GetCurrentBid() | [Previous page](getcurrentaskvolume.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns the current real-time bid price.





|  |
| --- |
| Notes: 
1. When accessed during State.Historical, the [Close](close.htm) price of the evaluated bar is substituted.  To access historical bid prices, please see [Developing for Tick Replay](developing_for__tick_replay.htm).
2. The GetCurrentBid() method runs on the bar series currently updating determined by the [BarsInProgress](barsinprogress.htm) property.  For [multi-instrument](multi-time_frame__instruments.htm) scripts, an additional int "barsSeriesIndex" parameter can be supplied which forces the method to run on an supplementary bar series. |





Method Return Value
-------------------


A double value representing the current bid price.


 


Syntax  

GetCurrentBid()  

GetCurrentBid(int barsSeriesIndex)


 


Parameters
----------




|  |  |
| --- | --- |
| barsSeriesIndex | An int value determining the bar series the method runs. Note:  This optional parameter is reserved for multi-instrument scripts |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Ensure we do not call GetCurrentBid() on historical data
   if (State == State.Historical)
     return;
 
   double currentBid = GetCurrentBid();
   Print("The Current Bid price is: " + currentBid);
   // The Current Bid price is: 1924.75
} |



 


 




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Example's Indicator";
   }
   if (State == State.Configure)
   {
     //Add MSFT as our additional data series
     AddDataSeries("MSFT", BarsPeriodType.Minute, 1);
   }
}
 
protected override void OnBarUpdate()
{
   // Ensure we do not call GetCurrentBid() on historical data
   if (State == State.Historical)
     return;
 
   if (BarsInProgress == 0)
   {
     double primaryBid = GetCurrentBid(0);
     Print("The Primary Bid price is: " + primaryBid);
     // The Primary Bid price is: 1924.75
   }
 
   if (BarsInProgress == 1)
   {
     double msftBid = GetCurrentBid(1);
     Print("MSFT's Current Bid price is: " + msftBid);
     // MSFT's Current Bid is: 43.63
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
 
 
 



