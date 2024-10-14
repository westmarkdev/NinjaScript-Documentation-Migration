










 


IsResetOnNewTradingDays







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isresetonnewtradingdays.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
IsResetOnNewTradingDays | [Previous page](isfirsttickofbar.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


Determines if the specified bar series is using Break at EOD


 




|  |
| --- |
| Note:  The property available on the UI will override any values set in code. Please see the help guide topic on using [Break at EOD](break_at_eod.htm) for more information |



 


Property Value
--------------


A bool[] when true, indicates the specified [BarsArray](barsarray.htm) is setup to run Break at EOD; otherwise false.  Default value is false


 


Syntax
------


IsResetOnNewTradingDays[int idx]


 


 




|  |
| --- |
| Warning:  This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |




Examples
--------




|  |
| --- |
| ns |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
   }
 
   else if (State == State.Configure)
   {
     //Add AAPL 1 minute with RTH trading hours, set to break EOD
     AddDataSeries("AAPL", new BarsPeriod() { BarsPeriodType = BarsPeriodType.Minute, Value = 1 }, 50, "US Equities RTH", true);
   }
 
}
protected override void OnBarUpdate()
{                 
 //Print out the current bars series name and break EOD setting on start up
 //   IsResetOnNewTradingDays[0]  Primary
 //   IsResetOnNewTradingDays[1]  AAPL
 
 if (CurrentBar == 0)          
   Print(BarsArray[BarsInProgress].ToChartString() + " " + IsResetOnNewTradingDays[BarsInProgress]);
 
 //Output:  
 //ES 03-15 (1 Minute) True
 //AAPL (1 Minute) False         
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
 
 
 



