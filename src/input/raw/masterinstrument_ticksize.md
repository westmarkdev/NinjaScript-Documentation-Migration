










 


TickSize







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?masterinstrument_ticksize.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
TickSize | [Previous page](splits.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the tick size configured for the [Master Instrument properties](editing_instruments.htm).



Property Value
--------------


A double value representing the tick size configured for the current master instrument.


 


Syntax
------


Bars.Instrument.MasterInstrument.TickSize


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
         {
                 // Displays the master instrument's tick size at the bottom right of the chart
                 Draw.TextFixed(this, "tag1", Bars.Instrument.MasterInstrument.TickSize.ToString(), TextPosition.BottomRight);
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
 
 
 



