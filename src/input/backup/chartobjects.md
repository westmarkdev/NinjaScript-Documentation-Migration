










 


ChartObjects







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartobjects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
ChartObjects | [Previous page](chartpanel.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


A collection of objects configured on the chart panel



Property Value
--------------


An [IList](https://msdn.microsoft.com/en-us/library/system.collections.ilist(v=vs.110).aspx) of Gui.NinjaScript.IChartObject instances containing references to the objects configured on the panel


 


Syntax
------


ChartPanel.ChartObjects



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
 
   IList<gui.ninjascript.ichartobject> myObjects = ChartPanel.ChartObjects;
 
   foreach (Gui.NinjaScript.IChartObject thisObject in myObjects)
   {
       Print(String.Format("{0} is of type {1}", thisObject.Name, thisObject.GetType()));
   }
} |



 


 


The image below shows the output of the code example above, while applied in a chart panel with three objects.


 


![ChartPanel_ChartObjects](chartpanel_chartobjects.png)





 
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
 
 
 



</gui.ninjascript.ichartobject>