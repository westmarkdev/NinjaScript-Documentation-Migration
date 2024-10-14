










 


CrossAbove()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?crossabove.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
CrossAbove() | [Previous page](countif.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Evaluates a cross above condition over the specified bar look-back period. 


 




|  |
| --- |
| Note: This method does not return true if both series being compared have equal values on the current or previous bar with a lookbackPeriod of 1.  |



 


Method Return Value
-------------------


This method returns true if a cross above condition occurred; otherwise, false.


 


Syntax
CrossAbove(ISeries<double> series1, ISeries<double> series2, int lookBackPeriod)
CrossAbove(ISeries<double> series1, double value, int lookBackPeriod)
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Parameters
----------




|  |  |
| --- | --- |
| lookBackPeriod | Number of bars back to check the cross above condition |
| series1 &amp; series2 | Any Series<double> type object such as an indicator, Close, High, Low, etc... |
| value | Any double value |




Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Go short if CCI crossed above 250 within the last bar
   if (CrossAbove(CCI(14), 250, 1))
       EnterShort();
 
   // Go long if 10 EMA crosses above 20 EMA within the last bar
   if (CrossAbove(EMA(10), EMA(20), 1))
       EnterLong();
 
   // Go long we have an up bar and the 10 EMA crosses above 20 EMA within the last 5 bars
   if (Close[0] &gt; Open[0] &amp;&amp; CrossAbove(EMA(10), EMA(20), 5))
       EnterLong();
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
 
 
 



</double></double></double></double>