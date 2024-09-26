










 


GetYByValueWpf()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getybyvaluewpf.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
GetYByValueWpf() | [Previous page](getybyvalue.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Returns a WPF coordinate on the chart determined by a series value represented on the chart scale.


 


Method Return Value
-------------------


An double value representing a WPF coordinate on the chart scale



Syntax
<chartscale>.GetYByValueWpf(double val)
----------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| val | A double value which usually represents a price or indicator value |





Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // gets the wpf coordinate of the price value passed to the method
   int     valueByYWpf = chartScale.GetYByValueWpf(Bars.GetClose(Bars.Count - 1));
 
   Print("valueByYWpf: " + valueByYWpf); // 207
} |



 


 


 In the image below, we pass the last bar close as the value (example logic avoids using a bars ago index, see also [OnRender()](onrender.htm) note #5), which in return tells us the last price displayed on the chart is at a WPF location of 207.30998 pixels.


 


![GetYByValueWpf](getybyvaluewpf.png)





 
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
 
 
 



</chartscale>