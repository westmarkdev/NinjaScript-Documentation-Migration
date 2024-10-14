










 


BuiltFrom







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?builtfrom.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
BuiltFrom | [Previous page](applydefaultvalue.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Determines the base dataset used to build the BarsType (i.e., Tick, Minute, Day).   The BuiltFrom property will control the frequency in which [OnDataPoint()](ondatapoint.htm) processes historical data.


 


Property Value
--------------


A [BarsPeriodType](barsperiod.htm) enum.  Values that will be recognized include:


 


•BarsPeriodType.Tick

•BarsPeriodType.Minute

•BarsPeriodType.Day

 




|  |
| --- |
| Warning:  Using other bars period types (e.g., Range, Volume, or other custom bars types) is NOT supported.  The BarsPeriodType values mentioned above represent all of the fundamental data points needed to build a bar. |



 


 


Syntax
------


BuiltFrom



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name     = "MyCustomBarsType";
     BarsPeriod   = new BarsPeriod { BarsPeriodType = (BarsPeriodType) 15, BarsPeriodTypeName = "MyCustomBarsType(15)", Value = 1 };
     BuiltFrom   = BarsPeriodType.Minute; // update OnDataPoint() every minute on historical data
     DaysToLoad   = 5;
   }
 
   else if (State == State.Configure)
   {
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
 
 
 



