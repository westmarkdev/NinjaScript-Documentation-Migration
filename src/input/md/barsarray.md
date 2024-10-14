










 


BarsArray







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsarray.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [AddDataSeries()](adddataseries.htm) &gt;
BarsArray | [Previous page](addvolumetric.htm)
[Return to chapter overview](adddataseries.htm)










Definition
----------


An array holding Bars objects that are added via the [AddDataSeries()](adddataseries.htm) method. BarsArray can be used as input for [indicator methods](indicators.htm). This property is of primary value when working with [multi-time frame or multi-instrument scripts](multi-time_frame__instruments.htm).


 


Property Value
--------------


An array of [Bars](bars.htm) objects.


 




|  |
| --- |
| Warning:  This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |



 


 


Syntax
BarsArray[int index]
---------------------------



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
 
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";      
   }
   else if (State == State.Configure)
   {
     // Add a 5 minute Bars object which is added to the BarArray 
     // which will take index 1 since the primary Bars object of the strategy 
     // will be index 0 
     AddDataSeries(BarsPeriodType.Minute, 5); 
   }
} 
 
protected override void OnBarUpdate() 
{ 
   // Ignore bar update events for the supplementary Bars object added above 
   if (BarsInProgress == 1) 
     return; 
 
   // Pass in a Bars object as input for the simple moving average method 
   // Evaluates if the 20 SMA of the primary Bars is greater than 
   // the 20 SMA of the secondary Bars added above 
   if (SMA(20)[0] &gt; SMA(BarsArray[1], 20)[0]) 
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
 
 
 



