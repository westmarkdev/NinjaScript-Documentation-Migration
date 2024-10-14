










 


Psychological Line







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?psychological_line.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Psychological Line | [Previous page](prior_day_ohlc.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Psychological Line is the ratio of the number of rising bars over the specified number of bars.


 


Syntax
------


PsychologicalLine(int period)


PsychologicalLine(ISeries<double> input, int period)


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of a 10 period Psychological Line
double value = PsychologicalLine(10)[0];
Print("The current Psychological Line value is " + value.ToString()); |






 
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