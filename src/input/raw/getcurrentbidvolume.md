










 


GetCurrentBidVolume()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getcurrentbidvolume.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
GetCurrentBidVolume() | [Previous page](getcurrentbid.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns the current real-time bid volume.





|  |
| --- |
| Notes: 
1. When accessed during State.Historical, the [Volume](volume.htm) of the evaluated bar series is substituted.  To access historical Bid Volumes, please see [Developing for Tick Replay](developing_for__tick_replay.htm).
2. The GetCurrentBidVolume() method runs on the bar series currently updating determined by the [BarsInProgress](barsinprogress.htm) property.  For [multi-instrument](multi-time_frame__instruments.htm) scripts, an additional int "barsSeriesIndex" parameter can be supplied which forces the method to run on an supplementary bar series. |





Method Return Value
-------------------


A long value representing the current bid volume.


 


Syntax  

GetCurrentBidVolume()  

GetCurrentBidVolume(int barsSeriesIndex)


 


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
   long currentBidVolume = GetCurrentBidVolume();
   Print("The Current Bid volume is: " + currentBidVolume);
   //The Current Bid volume is: 158         
} |



 


 




| ns |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";   
   }
   if (State == State.Configure)
   {
     //Add MSFT as our additional data series
     AddDataSeries("MSFT", BarsPeriodType.Minute, 1);
   }
}   
 
protected override void OnBarUpdate()
{         
   if(BarsInProgress == 0)
   {
     long currentBidVolume = GetCurrentBidVolume(0);
     Print("The Current Bid volume is: " + currentBidVolume);
     //The Current Bid volume is: 346
   }
   
   if(BarsInProgress == 1)
   {
     long msftBidVolume = GetCurrentBidVolume(1);
     Print("MSFT's Current Bid volume is: " + msftBidVolume);
     //MSFT's Current Bid volume is: 1548
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
 
 
 



