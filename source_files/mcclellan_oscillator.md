










 


McClellan Oscillator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?mcclellan_oscillator.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
McClellan Oscillator | [Previous page](maximum_max.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


McClellan Oscillator is the difference between two exponential moving averages of the NYSE advance decline spread. This indicator require ADV and DECL index data.


 


Syntax
------


McClellanOscillator(int fastPeriod, int slowPeriod)
---------------------------------------------------


McClellanOsillator(ISeries<double> input, int fastPeriod, int slowPeriod)


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| fastPeriod | Number of bars used in the fast moving average calculation |
| slowPeriod | Number of bars used in the slow moving average calculation |



 



Examples
--------




| ns |
| --- |
| // An ADV and DECL data series must be added to OnStateChange()
else if (State == State.Configure)
{
 AddDataSeries("^ADV");
 AddDataSeries("^DECL");
}
 
// Prints the current value of the McClellan Oscillator with a 19 fast period moving average &amp; 39 slow period
double value = McClellanOscillator(19, 39)[0];
Print("The current McClellan Oscillator value is " + value.ToString()); |






 
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