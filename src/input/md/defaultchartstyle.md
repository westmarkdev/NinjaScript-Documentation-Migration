










 


DefaultChartStyle







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?defaultchartstyle.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
DefaultChartStyle | [Previous page](builtfrom.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Allows to set a default ChartStyle for usage with a NinjaTrader bars type


 


Property Value
--------------


A ChartStyleTypeÂenum value representing the [ChartStyle](chartstyletype.htm) to be set as default. System defaults include:


 


•ChartStyleType.Box,

•ChartStyleType.CandleStick,

•ChartStyleType.LineOnClose,

•ChartStyleType.OHLC,

•ChartStyleType.PointAndFigure,

•ChartStyleType.KagiLine,

•ChartStyleType.OpenClose,

•ChartStyleType.Mountain

 


Syntax
------


DefaultChartStyle


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
        if (State == State.SetDefaults)
       {
           Name                       = "SampleBarsType";
           BarsPeriod                 = new BarsPeriod { BarsPeriodType = (BarsPeriodType) 15, BarsPeriodTypeName = "SampleBarsType(15)", Value = 1 };
           BuiltFrom                 = BarsPeriodType.Minute;
           DaysToLoad                 = 5;
           DefaultChartStyle         = Gui.Chart.ChartStyleType.CandleStick;
           IsIntraday                 = true;
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
 
 
 



