










 


Indicators







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_indicators.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
Indicators | [Previous page](getxbytime.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Contains a collection of indicators currently configured on the chart.



Property Value
--------------


A ChartObjectCollection of NinjaTrader.Gui.NinjaScript.IndicatorRenderBase objects representing the indicators on the chart


 


Syntax
------


<chartcontrol>.Indicators



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Instantiate a ChartObjectCollection to hold chartControl.Indicators
   ChartObjectCollection<ninjatrader.gui.ninjascript.indicatorrenderbase> indicatorCollection = chartControl.Indicators;
 
   // Print the Calculate setting for any configured indicators not using Calculate.OnBarClose
   foreach (NinjaTrader.Gui.NinjaScript.IndicatorRenderBase indicator in indicatorCollection)
   {
       if(indicator.Calculate != Calculate.OnBarClose)
           Print(String.Format("{0} is using Calculate.{1}", indicator.Name, indicator.Calculate.ToString()));
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
 
 
 



</ninjatrader.gui.ninjascript.indicatorrenderbase></chartcontrol>