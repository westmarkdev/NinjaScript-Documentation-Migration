










 


ChartBars







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
ChartBars | [Previous page](chart.htm)
[Return to chapter overview](chart.htm)










The ChartBars class provides GUI access related methods and properties to the primary bars series configured on the Chart through the [Data Series](working_with_price_data.htm) menu.   For data access information related to the NinjaScript input's bars series, please use the [Bars Series](bars.htm) object (or the [BarsArray](barsarray.htm) for multi-series input)


 




|  |
| --- |
| Note:  A ChartBars object will ONLY exist should the hosting NinjaScript type be loaded through a [Chart](chart.htm).  For example, a Strategy would have access to a ChartBars property when running on a Chart, but would NOT when loaded through the [Strategies Grid](strategies_tab2.htm) or [Strategy analyzer](strategy_analyzer.htm).   |



 


 


![ChartBars](chartbars.png)


 


 




|  |
| --- |
| Warning:  It is crucial to check for object references before accessing the ChartBars otherwise possible null reference errors can be expected depending on where the NinjaScript object was started.  See example below |



 


 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Bars](chartbars_bars.htm) | Data returned from the historical data repository. |
| [Count](chartbars_count.htm) | The total number of ChartBars that exist on the chart |
| [FromIndex](chartbars_fromindex.htm) | An index value representing the first bar painted on the chart.   |
| [GetBarIdxByTime()](chartbars_getbaridxbytime.htm) | An ChartBar index value calculated from a time value on the chart. |
| [GetBarIdxByX()](chartbars_getbaridxbyx.htm) | Returns the ChartBar index value at a specified x-coordinate relative to the ChartControl. |
| [GetTimeByBarIdx()](chartbars_gettimebybaridx.htm) | The ChartBars time value calculated from a bar index value on the chart. |
| [Panel](chartbars_panel.htm) | The Panel index value that the ChartBars eside. |
| [Properties](chartbars_properties.htm) | Various ChartBar properties that have been configured from the Chart's [Data Series](working_with_price_data.htm) menu.  |
| [ToChartString()](chartbars_tochartstring().htm) | A string formatted for the Chart's Data Series Label as well as the period. |
| [ToIndex](chartbars_toindex.htm) | An index value representing the last bar painted on the chart.   |



 


 


Example




| ns |
| --- |
| protected override void OnStateChange()
{         
   if (State == State.DataLoaded)
   {
     if(ChartBars != null)
     {
         Print("The starting number of bars on the chart is " + ChartBars.Bars.Count);
     }
     else 
     {
         Print("Strategy was not loaded from a chart, exiting strategy...");
         return;
     }
   }
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
 
 
 



