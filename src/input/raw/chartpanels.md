










 


ChartPanels







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartpanels.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
ChartPanels | [Previous page](canvaszoomstate.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Holds a collection of [ChartPanel](chartpanel.htm) objects containing information about the panels active on the chart.



Property Value
--------------


An [ObservableCollection](https://msdn.microsoft.com/en-us/library/ms668604(v=vs.110).aspx) of ChartPanel objects



Syntax
------


<chartcontrol>.ChartPanels



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the number of panels currently displayed on the chart
   Print(String.Format("There are {0} panels on the chart", chartControl.ChartPanels.Count));  
} |



 


 


Based on the image below, there are three ChartPanel objects in the ChartPanels collection, as seen by ChartPanels.Count in the code above.


 


![ChartControl_ChartPanels](chartcontrol_chartpanels.png)





 
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