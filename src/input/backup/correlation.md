










 


Correlation







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?correlation.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Correlation | [Previous page](commodity_channel_index_cci.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The correlation indicator will plot the correlation of the data series to a desired instrument. Values close to 1 indicate movement in the same direction. Values close to -1 indicate movement in opposite directions. Values near 0 indicate no correlation.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 


 


Syntax
------


Correlation(int period, string correlationSeries)  

string correlationSeies(ISeries<double> input, int period, string correlationSeies)


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |
| correlationSeries | The data series to compare to |



 


 


Examples
--------




| ns |
| --- |
| // The correlation data series must be added to OnStateChange() as this indicator runs off the correlation data series data
else if (State == State.Configure)
{
   AddDataSeries("SPY");
}
 
// Checks the bars in progress and prints the current correlation to the SPY
if (BarsInProgress == 0)
{
   double value = Correlation(20, "SPY")[0];
   Print("The current correlation to the SPY is " + value.ToString());
} |



 


 




|  |
| --- |
| Note: If the correlation series does not plot during a time the input series plots, a value of zero would plot in the above example. You may consider ignroing zero values. |




 


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
 
 
 



</double>