










 


ToChartString()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tochartstring.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
ToChartString() | [Previous page](tickcount.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the bars series as a formatted string, including the [Instrument.FullName](instrument_fullname.htm), [BarsPeriod](barsperiod.htm) Value, and BarsPeriodType name. 


 




|  |
| --- |
| Note:  To obtain a return value which matches the user configured [ChartBars Label property](chartbars_properties.htm), please see the [ChartBars.ToChartString()](chartbars_tochartstring().htm) method |



 


 


Syntax
------


Bars.ToChartString()


 


Return Value
------------


A string value that represents the bars series


 


Parameters
----------


This method does not accept any parameters



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // print the chart string on start up
   if(CurrentBar == 0)
     Print(Bars.ToChartString()); // ES 09-15 (60 Minute)      
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
 
 
 



