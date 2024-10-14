










 


GetValueByYWpf()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getvaluebyywpf.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
GetValueByYWpf() | [Previous page](getvaluebyy.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Returns the series value on the chart scale determined by a WPF coordinate on the chart.  


 


Method Return Value
-------------------


A double value representing a series value on the chart scale.  This is normally a price value, but can represent indicator plot values as well.


 


Syntax
<chartscale>.GetValueByYWpf(double y)
--------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| y | A double value representing a WPF coordinate on the chart scale |





Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // store the y location the user clicked
   double   wpfY = chartControl.MouseDownPoint.Y;
 
   // gets price value of the WPF coordinate passed to the method
   double   valueByYWpf = chartScale.GetValueByYWpf(wpfY);
 
   Print("valueByYWpf: " + valueByYWpf); //2105.49995215
} |



 


 


In the image below, we used the Chart Control property [MouseDownPoint](mousedownpoint.htm) as the "wpfy" variable, which in return tells us the user clicked on a Y value of 2105.499 on the chart scale.


 


![getvaluebyywpf](getvaluebyywpf.png)





 
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