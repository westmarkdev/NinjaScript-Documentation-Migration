










 


BarsPeriod







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsperiod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
BarsPeriod | [Previous page](onbarupdate.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


The primary Bars object time frame (period type and interval).  

 




|  |
| --- |
| Warning:  This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |





Property Value
--------------


A [Bars](bars.htm) series object representing the time frame of the Bars. 


 


Syntax




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BarsPeriod.BarsPeriodType | The type of bars used for the period, as well as the enumeration value under which the any of the 14 default NinjaTrader types are registered. Possible values include:
 


|  |  |
| --- | --- |
| BarsPeriodType.Tick | 0 |
| BarsPeriodType.Volume | 1 |
| BarsPeriodType.Range | 2 |
| BarsPeriodType.Second | 3 |
| BarsPeriodType.Minute | 4 |
| BarsPeriodType.Day | 5 |
| BarsPeriodType.Week | 6 |
| BarsPeriodType.Month | 7 |
| BarsPeriodType.Year | 8 |
| BarsPeriodType.HeikenAshi | 9 |
| BarsPeriodType.Kagi | 10 |
| BarsPeriodType.Renko | 11 |
| BarsPeriodType.PointAndFigure | 12 |
| BarsPeriodType.LineBreak | 13 |
| BarsPeriodType.Volumetric | 14 |



 
 


|  |
| --- |
| Tip: When creating custom [BarsTypes](bars_type.htm), it is recommended to pick high, unique enumeration value to avoid conflict from other BarsTypes that may be used by a single installation.  
 
BarsPeriod = new BarsPeriod { BarsPeriodType = (BarsPeriodType)123456, BarsPeriodTypeName = "MyCustomBars", Value = 1 }; |



  |
| BarsPeriod.BaseBarsPeriodType | Only relevant for [HeikenAshi](addheikenashi.htm), [Kagi](addkagi.htm), [LineBreak](addlinebreak.htm), [PointAndFigure](addpointandfigure.htm) and [Volumetric](addvolumetric.htm) Bars objects. Same possible values as BarsPeriod.BarsPeriodType |
| BarsPeriod.BaseBarsPeriodValue | Only relevant for [HeikenAshi](addheikenashi.htm), [Kagi](addkagi.htm), [LineBreak](addlinebreak.htm), [PointAndFigure](addpointandfigure.htm) and [Volumetric](addvolumetric.htm) Bars objects. Determines an integer value representing the basePeriodTypeValue parameter |
| BarsPeriod.MarketDataType | The data type used to build the bars.  Possible values:
MarketDataType.Ask
MarketDataType.Bid
MarketDataType.Last |
| BarsPeriod.PointAndFigurePriceType | Only relevant for PointAndFigure Bars objects. Possible values:
PointAndFigurePriceType.Close
PointAndFigurePriceType.HighsAndLows |
| BarsPeriod.ReversalType | Only relevant for Kagi Bars objects. Possible values:
ReversalType.Percent
ReversalType.Tick |
| BarsPeriod.Value | Determines an integer value representing the period parameter.
•When using Kagi Bars objects this represents the "reversal" parameter•When using LineBreak Bars objects this represents the "lineBreakCount" parameter•When using PointAndFigure Bars objects this represents the "boxSize" parameter•When using Renko Bars objects this represents the "brickSize" parameter |
| BarsPeriod.Value2 | Only relevant for PointAndFigure Bars objects. Determines an integer value representing the "reversal" parameter. |



 



Examples
--------




| ns Checking BarsPeriod values |
| --- |
| // Calculate only if there is a 100 tick chart or greater
protected override void OnBarUpdate() 
{ 
     if (BarsPeriod.BarsPeriodType == BarsPeriodType.Tick &amp;&amp; BarsPeriod.Value &gt;= 100)
     {
         // Indicator calculation logic here
     }
} |



 


 




| ns Creating a new BarsPeriod object |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {      
           // add a 1440 minute apple bars object using the RTH session template
           AddDataSeries("AAPL", new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1440 }, "US Equities RTH");               
     }
 
     else if (State == State.DataLoaded)
     {
           // Print out the loaded bars period 
           Print(Instrument.FullName + " " + BarsPeriod); // MSFT 1 Minute
           Print(BarsArray[1].Instrument.FullName + " " + BarsArray[1].BarsPeriod); // AAPL 1440 Minute
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
 
 
 



