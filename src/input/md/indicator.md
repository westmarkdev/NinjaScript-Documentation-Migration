










 


Indicator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?indicator.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Indicator | [Previous page](onnextdatapoint.htm)
[Return to chapter overview](language_reference_wip.htm)










The methods and properties covered in this section are unique to custom indicator development.  Indicator configuration properties globally define various behaviors of indicators. All properties have default values and can be overridden by setting them in the [OnStateChange()](onstatechange.htm) method of the indicator.


 




|  |
| --- |
| Tip:  See also the "[Common](common.htm)" section for more method and properties which are shared by NinjaScript types |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AddLine()](addline.htm) | Adds line objects on a chart. |
| [AddPlot()](addplot.htm) | Adds plot objects that define how an indicator or strategy data series render on a chart. |
| [BarsRequiredToPlot](barsrequiredtoplot.htm) | The number of bars on a chart required before the script plots. |
| [DisplayInDataBox](displayindatabox.htm) | Determines if plot(s) display in the chart data box. |
| [DrawHorizontalGridLines](drawhorizontalgridlines.htm) | Plots horizontal grid lines on the indicator panel. |
| [DrawOnPricePanel](drawonpricepanel.htm) | Determines the chart panel the draw objects renders. |
| [DrawVerticalGridLines](drawverticalgridlines.htm) | Plots vertical grid lines on the indicator panel. |
| [IndicatorBaseConverter](indicatorbaseconverter.htm) | A custom TypeConverter class handling the designed behavior of an indicator's property descriptor collection. |
| [IsChartOnly](ischartonly.htm) | If true, any indicator will be only available for charting usage - indicators with this property enabled would for example not be expected to show if called in a SuperDOM or MarketAnalyzer window. |
| [IsSuspendedWhileInactive](issuspendedwhileinactive.htm) | Prevents real-time market data events from being raised while the indicator's hosting feature is in a state that would be considered suspended and not in immediate use by a user. |
| [PaintPriceMarkers](paintpricemarkers.htm) | If true, any indicator plot values display price markers in the y-axis. |
| [ShowTransparentPlotsInDataBox](showtransparentplotsindatabox.htm) | Determines if plot(s) values which are set to a Transparent brush display in the chart data box. |






 
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
 
 
 



