










 


GetInstrument()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getinstrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt;
GetInstrument() | [Previous page](instrument_fullname.htm)
[Return to chapter overview](instrument.htm)










Definition
----------


Returns an [Instrument](instruments.htm) object by the master instrument name configured in the database.  


 




|  |
| --- |
| Note:  This method does NOT add additional data for real-time or historical processing.  For adding an additional data to your script, please see the  [AddDataSeries()](adddataseries.htm) method. |





Method Return Value
-------------------


An [Instrument](instrument.htm) object


 


Syntax
------


Instrument.GetInstrument(string instrumentName)


 


Parameters
----------




|  |  |
| --- | --- |
| instrumentName | A string value representing a name of an instrument |



 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.Historical)
   {
     Instrument myInstrument = Instrument.GetInstrument("AAPL");
 
     Print("AAPL's tick size is " + myInstrument.MasterInstrument.TickSize.ToString());
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
 
 
 



