










 


Fibonacci Pivots







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?fibonacci_pivots.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Fibonacci Pivots | [Previous page](ease_of_movement.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Fibonacci pivots are a price analysis tool that generates potential support and resistance levels by multiplying the prior range against Fibonacci values then adding or subtracting it from the average of the prior high, low, and close.


 


Syntax
------


FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width)  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width)


 


Returns pivot point value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).Pp[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).PP[int barsAgo]


 


Returns R1 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R1[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R1[int barsAgo]


 


Returns R2 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R2[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R2[int barsAgo]


 


Returns R3 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R3[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R3[int barsAgo]


 


Returns S1 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S1[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S1[int barsAgo]


 


Returns S2 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S2[int barsAgo]  

FibonacciPivots(ISeries<double> input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S2[int barsAgo]


 


Returns S3 value  

FibonacciPivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S3[int barsAgo]  

FibonacciPivots(ISeries<double>input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S3[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| pivotRangeType | Sets the range for the type of pivot calculated. Possible values are:
PivotRange.Daily
PivotRange.Weekly
PivotRange.Monthly |
| priorDayHLC | Sets how the prior range High, Low, Close values are calculated. Possible values are:
HLCCalculationMode.CalcFromIntradayData
HLCCalculationMode.DailyBars
HLCCalculationMode.UserDefinedValues |
| userDefinedClose | Sets the close for Pivots calculations when using HLCCalculationMode.UserDefinedValues. |
| userDefinedHigh | Sets the high for Pivots calculations when using HLCCalculationMode.UserDefinedValues. |
| userDefinedLow | Sets the low for Pivots calculations when using HLCCalculationMode.UserDefinedValues. |
| width | Sets how long the Pivots lines will be drawn |



 



Examples
--------




| ns |
| --- |
| // Prints the current pivot point value
double valuePp = FFibonacciPivots(PivotRange.Daily, HLCCalculationMode.CalcFromIntradayData, 0, 0, 0, 20).Pp[0];
Print("The current Fibonacci Pivots' pivot value is " + valuePp.ToString());
 
// Prints the current S2 pivot value
double valueS2 = FibonacciPivots(PivotRange.Daily, HLCCalculationMode.CalcFromIntradayData, 0, 0, 0, 20).S2[0];
Print("The current Fibonacci Pivots' S2 pivot value is " + valueS2.ToString()); |



 


 


Source Code
-----------


You can view this indicator method source code by selecting the menu New &gt; NinjaScript Editor &gt; Indicators within the NinjaTrader Control Center window.


 




|  |  |  |
| --- | --- | --- |
| Tip: When using HLCCalculationMode.DailyBars it can be expected that a value of 0 is returned when the daily bars have not been loaded yet. Due to the asynchronous nature of this indicator calling daily bars you should only access the pivot values when the indicator has loaded all required Bars objects. To ensure you are accessing accurate values you can use .[IsValidDataPoint()](isvaliddatapoint.htm) as a check:
 


| ns |
| --- |
| // Evaluates that this is a valid pivot point value
if (FibonacciPivots(PivotRange.Daily, HLCCalculationMode.DailyBars, 0, 0, 0, 20).Pp.IsValidDataPoint(0))
{
     // Prints the current pivot point value
     double valuePp = FibonacciPivots(PivotRange.Daily, HLCCalculationMode.DailyBars, 0, 0, 0, 20).Pp[0];
     Print("The current Pivots' pivot value is " + valuePp.ToString());
} |


 |






 
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
 
 
 



</double></double></double></double></double></double></double></double>