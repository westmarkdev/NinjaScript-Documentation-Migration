










 


CrosshairType







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?crosshairtype.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
CrosshairType | [Previous page](chartpanels.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the [Cross Hair](cross_hair.htm) type currently enabled on the chart.



Property Value
--------------


An enum specifying the type of Cross Hair currently enabled on the chart. Possible values are listed below:


 




|  |  |
| --- | --- |
| Local | The local (single-chart) Cross Hair is enabled |
| Global | Global Cross Hair |
| GlobalNoTimeScroll | Global Cross Hair (No Time Scroll) is enabled |




Syntax
------


<chartcontrol>.CrosshairType



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print a message if the user enables the Global Cross Hair without time scrolling
   if (chartControl.CrosshairType == CrosshairType.GlobalNoTimeScroll)
       Print("It is recommended to enable Global Cross Hair time scrolling with this indicator");
} |



 


 


In the image below, CrosshairType reveals that Global Cross Hair (No Time Scroll) is enabled on the chart.


 


![ChartControl_CrosshairType](chartcontrol_crosshairtype.png)





 
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