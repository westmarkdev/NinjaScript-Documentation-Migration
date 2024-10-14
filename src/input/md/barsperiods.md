










 


BarsPeriods







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsperiods.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [AddDataSeries()](adddataseries.htm) &gt;
BarsPeriods | [Previous page](barsinprogress.htm)
[Return to chapter overview](adddataseries.htm)










Definition
----------


Holds an array of BarsPeriod objects synchronized to the number of unique Bars objects held within the parent NinjaScript object. If a  NinjaScript object holds two Bars series, then BarsPeriods will hold two BarsPeriod objects.


 


Property Value
--------------


An array of [BarsPeriod](barsperiod.htm) objects.


 




|  |
| --- |
| Warning: This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |



 


   

Syntax  

BarsPeriods[int barSeriesIndex]




Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the strategy and is automatically assigned 
         // a Bars object index of 1 since the original data the strategy is ran on,
         // set by the UI, takes the index of 0. 
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5); 
     }
} 
 
protected override void OnBarUpdate() 
{ 
     // Print out 5, the value of the secondary bars object 
     if (BarsInProgress == 1)
         Print(BarsPeriods[1].Value);
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
 
 
 



