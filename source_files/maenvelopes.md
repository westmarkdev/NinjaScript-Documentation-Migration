










 


MA Envelopes







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maenvelopes.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
MA Envelopes | [Previous page](linear_regression_slope.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Moving Average Envelope consists of moving averages calculated from the underling price, shifted up and down by a fixed percentage.


 


 


Syntax
------


MAEnvelopes(double envelopePercentage, int mAType, int period)


MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period)


 


Returns upper band levels


MAEnvelopes(double envelopePercentage, int mAType, int period).Upper[int barsAgo]


MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Upper[int barsAgo]


 


Returns moving average value


MAEnvelopes(double envelopePercentage, int mAType, int period).Middle[int barsAgo]


MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Middle[int barsAgo]


 


Returns lower band levels


MAEnvelopes(double envelopePercentage, int mAType, int period).Lower[int barsAgo]


MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Lower[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| envelopePercentage | Percentage around MA that envelopes will be drawn |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| mAType | Moving average type:
1 = EMA
2 = HMA
3 = SMA
4 = TMA
5 = TEMA
6 = WMA |
| period | Number of bars used in the calculation |



 



Examples
--------




| ns |
| --- |
| // Prints the current upper band value of a 20 period SMA envelope using default price type
double upperValue = MAEnvelopes(0.2, 3, 20).Upper[0];
Print("The current SMA envelope upper value is " + upperValue.ToString());
 
// Prints the current lower band value of a 20 period SMA envelope using low price type
double lowerValue = MAEnvelopes(Low, 0.2, 3, 20).Lower[0];
Print("The current SMA envelope lower value is " + lowerValue.ToString()); |



 


 


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
 
 
 



</double></double></double></double>