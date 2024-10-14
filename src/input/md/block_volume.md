










 


Block Volume







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?block_volume.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Block Volume | [Previous page](balance_of_power_bop.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Block volume detects block trades and display how many occurred per bar. This can be displayed either as trades or volume. Historical tick data is required to plot historically.


 


Syntax
------


BlockVolume(int blockSize, CountType countType)


BlockVolume(ISeries<double> input, int blockSize, CountType countType)


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| blockSize | The minimum volume a trade must be to be considered a block trade |
| countType | The format to count the block trades. By number of block trades that occurred or total block trade volume |



 



Examples
--------




| ns |
| --- |
| // A 1 tick data series must be added to OnStateChange() as this indicator runs off of tick data
else if (State == State.Configure)
{
   AddDataSeries(Data.BarsPeriodType.Tick, 1);
}
 
// Prints the current value of an 80 block trade size counted in volume for the Block Volume
if (BarsInProgress == 0)
{
double value = BlockVolume(80, CountType.Volume)[0];
Print("The current Block Volume value is " + value.ToString());
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
 
 
 



</double>