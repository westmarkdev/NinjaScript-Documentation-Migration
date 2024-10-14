










 


GetValueAt()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getvalueat.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
GetValueAt() | [Previous page](iseries_count.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Returns the underlying input value at a specified bar index value.


 


Method Return Value
-------------------


A double value representing the value at a specified bar.


 


Syntax
------


GetValueAt(int barIndex)


ISeries<t>.GetValueAt(int barIndex)


 




|  |
| --- |
| Tip:  If called directly from the instance of the NinjaScript object, the value which is returned corresponds to the input series the object is running. (e.g., Close, High, Low, SMA, etc.).  If you're attempting to obtain another indicator value, you will need to pull this from the calculated indicator Value or Plot:
 
SMA(20).GetValueAt(123); // bar value
SMA(20).Values[0].GetValueAt(123); // indicator value
(Input as Indicator).Values[0].GetValueAt(123) // passed in indicator value
  |



 
Parameters
------------




|  |  |
| --- | --- |
| barIndex | An int representing an absolute bar index value |




 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // make sure there are bars displayed on the chart and the chart control is ready before running
   if (Bars == null || chartControl == null)
     return;      
 
   // loop through all the visable bars on the chart
   for (int i = ChartBars.FromIndex - 1; i &gt;= BarsRequiredToPlot; i--)
   {
     double value = GetValueAt(i);
     Print(string.Format("The value at bar {0} is {1}", i, value));      
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
 
 
 



</t></t></t>