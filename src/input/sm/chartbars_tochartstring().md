










 


ToChartString()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_tochartstring().htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
ToChartString() | [Previous page](chartbars_properties.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


Returns a formatted string representing the [ChartBars.Properties.Label](chartbars_properties.htm) property, [BarsPeriod](barsperiod.htm) Value, and BarsPeriodType name.


 




|  |
| --- |
| Note:  The property returned is dependent on a user configured [Data Series](working_with_price_data.htm) property, and results may return differently than expected.  See also [Bars.ToChartString()](tochartstring.htm) for a return value which is not subject to user-defined variables. |



 


 


Syntax
------


ChartBars.ToChartString()


 


Return Value
------------


A string value that represents the ChartBars label and configured bars period


 


Parameters
----------


This method does not accept any parameters



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if (ChartBars != null)
     Print(ChartBars.ToChartString()); // My Favorite Instrument (1 Minute)
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
 
 
 



