










 


Input







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?input.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
Input | [Previous page](highs.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


The main historical data input. If implemented in the NinjaScript object, it allows for more flexibility as non bars based series such as plot series could be passed in and drive the calculation outcomes - an example would be a custom moving average that should have the ability to operate on another moving average (i.e. the SMA) as input series.


 


Property Value
--------------


An ISeries<double> type object that implements the Series<double> interface. Accessing this property via an index value [int barsAgo] returns a double value representing the price of the referenced bar.


 


Syntax
------


Input   

Input[int barsAgo]



 



Examples
--------




| ns |
| --- |
| // Prints the the current value of input
Print(Input[0].ToString()); |



 




| ns |
| --- |
| // Prints the the current type of input passed to the object, so we can detect if we're working on a price based series such as OHLCV or a derivative such as an SMA indicator
if (Input is PriceSeries)
Print("Price Series Input");
if (Input is Indicator)
Print("Indicator Input"); |



 




| ns |
| --- |
| // Prints the the current selected price type for the input series
else if (State == State.DataLoaded)
{
     PriceSeries priceSeries = Inputs[0] as PriceSeries;
            
     if (priceSeries != null)
         Print("PriceType selected: " + priceSeries.PriceType);
} |



 


 




|  |
| --- |
| Tip: When working with multi-series indicators, Input is not guaranteed to reference the primary [BarsInProgress](barsinprogress.htm). Please be mindful as to when you access Input[0] as you will only be able to do so after the contextual BarsInProgress has bars. To check to ensure BarsInProgress has some bars you can use [CurrentBars](currentbars.htm) to check. |






 
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
 
 
 



</double></double></double></t></double></t>