










 


CandleStickPattern







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?candlestickpattern.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
CandleStickPattern | [Previous page](camarilla_pivots.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Detects the specified candle stick pattern.


 


 


Syntax
------


CandleStickPattern(ChartPattern pattern, int trendStrength)  

CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)


 


Returns a value indicating if the specified pattern was detected  

CandleStickPattern(ChartPattern pattern, int trendStrength)[int barsAgo]  

CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)[int barsAgo]


 


 


Return Value
------------


A double value representing pattern found. Returns a value of 1 if the pattern is found; returns a value of 0 if no pattern was found.


Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| pattern | Possible values are:
 
ChartPattern.BearishBeltHold
ChartPattern.BearishEngulfing
ChartPattern.BearishHarami
ChartPattern.BearishHaramiCross
ChartPattern.BullishBeltHold
ChartPattern.BullishEngulfing
ChartPattern.BullishHarami
ChartPattern.BullishHaramiCross
ChartPattern.DarkCloudCover
ChartPattern.Doji
ChartPattern.DownsideTasukiGap
ChartPattern.EveningStar
ChartPattern.FallingThreeMethods
ChartPattern.Hammer
ChartPattern.HangingMan
ChartPattern.InvertedHammer
ChartPattern.MorningStart
ChartPattern.PiercingLine
ChartPattern.RisingThreeMethods
ChartPattern.ShootingStar
ChartPattern.StickSandwich
ChartPattern.ThreeBlackCrows
ChartPattern.ThreeWhiteSoldiers
ChartPattern.UpsideGapTwoCrows
ChartPattern.UpsideTasukiGap |
| trendStrength | The number of required bars to the left and right of the swing point used to determine trend. A value of zero will exclude the requirement of a trend and only detect based on the candles themselves. |



 



Example
-------




| ns |
| --- |
| // Go long if the current bar is a bullish engulfing pattern
if (CandlestickPattern(ChartPattern.BullishEngulfing, 4)[0] == 1)
   EnterLong(); |



 


 


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
 
 
 



</double></double>