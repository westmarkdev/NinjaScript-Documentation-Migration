﻿










 


BuySell Pressure







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?buysellpressure.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
BuySell Pressure | [Previous page](bollinger_bands.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The BuySellPressure indicator displays both the current bar's buying and selling pressure as percentage values based on the categorization of trades as buy or sell trades. Trades are categorized in real-time as a buy (at the ask or above) or as a sell (at the bid or below).... Trades in between the market are ignored. 


 




|  |
| --- |
| Note:  For historical calculations, [Tick Replay](tick_replay.htm) must be enabled |



 


 


Syntax
------


BuySellPressure()  

BuySellPressure(ISeries<double> input)


 


Returns buy pressure value  

BuySellPressure().BuyPressure[int barsAgo]  

BuySellPressure(ISeries<double> input).BuyPressure[int barsAgo]


 


Returns sell pressure value  

BuySellPressure().SellPressure[int barsAgo]  

BuySellPressure(ISeries<double> input).SellPressure[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |



 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Indicators will inherit the Calculate mode from the hosting script.
       // Since BuySellPressure requires the use of Calculate.OnEachTick, we must ensure the hosting script has this Calculate mode set
       Calculate = Calculate.OnEachTick;
   }
}
 
protected override void OnBarUpdate()
{
   // This checks that 70% or more of the volume hit the ask or higher
   if (State == State.Historical || BuySellPressure().BuyPressure[0] &gt; 70)
   {
       EnterLong();
   }
} |



 




|  |
| --- |
| Tip: Since this indicator operates in a real-time environment, remember to check for State.Realtime, or enable Tick Replay on the associated Data Series. In the above example we check that 50% or more of the volume hit the ask or higher. Our statement checks if the data is being calculated on historical data first, if true, we enter long, if not true (live), the the statement then checks for the Buy Volume condition. |



 


Source Code
-----------


You can view this indicator method source code by selecting the menu New &gt; NinjaScript Editor &gt; Indicators within the NinjaTrader Control Center window.





 
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
 
 
 



</double></double></double>