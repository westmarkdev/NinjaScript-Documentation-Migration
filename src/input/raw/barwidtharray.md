










 


BarWidthArray







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barwidtharray.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarWidthArray | [Previous page](chartcontrol_barwidth.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


An array containing the values of the [BarWidth](chartcontrol_barwidth.htm) properties of all Bars objects applied to the chart.



Property Value
--------------


An array of double variables containing the values of the BarWidth properties of Bars objects on the chart.



Syntax
------


<chartcontrol>.BarWidthArray[]



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Assign BarWidthArray to a new array
   double[] barWidths = chartControl.BarWidthArray;
 
   double referenceWidth = barWidths[0];
 
   // Trigger an alert if bar widths on the chart differ
   foreach (double width in barWidths)
   {
       if (width != referenceWidth)
           Alert("mismatchWidths", Priority.Low, "Bar widths on the chart do not match!", " ", 20, Brushes.White, Brushes.Black);
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
 
 
 



</chartcontrol>