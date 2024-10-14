










 


IsTickReplays







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?istickreplays.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
IsTickReplays | [Previous page](isresetonnewtradingdays.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


Indicates the specified bar series is using Tick Replay.   Please see the help guide topic on using [Tick Replay](tick_replay.htm) for general information on this mode.


 




|  |
| --- |
| Note:  For a primary series, the Tick Replay option must be configured from the UI before a NinjaScript object can take use of this property.  The setting on the Chart's Data Series menu will always take precedence for an object series which already exists on the user's chart.   |



 


 




|  |
| --- |
| Warning:  This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |




 


Property Value
--------------


A bool[] when true, indicates the specified [BarsArray](barsarray.htm) is setup to run Tick Replay; otherwise false.  Default value is false


 


Syntax
------


IsTickReplays[int idx]


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if(State == State.SetDefaults)
   {
       Name = "Examples Indicator";
   }
   
   else if (State == State.Configure)
   {
     AddDataSeries("AAPL", BarsPeriodType.Minute, 1);   
   }
   else if (State == Data.Loaded)
   {
      // IsTickReplays[0] = true; 
      // Programmatically setting this option here for Primary [0] does not have any effect      
     // Primary series must be configured from UI
            
     // It is not possible to combine Tick Replay series and non Tick Replay series in a single chart or script
     // The assignment below would not be necessary if the primary series were set to True via the UI
     // IsTickReplays[1] = true;
   }
}
 
protected override void OnBarUpdate()
{                 
   //Print out the current bars series name and tick replays setting on start up
   if (CurrentBar == 0)          
     Print(BarsArray[BarsInProgress].ToChartString() + " " + IsTickReplays[BarsInProgress]);
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
 
 
 



