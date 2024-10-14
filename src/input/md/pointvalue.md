










 


PointValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?pointvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
PointValue | [Previous page](getnextexpiry.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the currency value of 1 full point of movement. For example, 1 point in the S&amp;P 500 Emini futures contract (ES) is $50 USD which is equal to $12.50 USD per tick.



Property Value
--------------


A double value representing the currency value of 1 point of movement.


 


Syntax
------


Instrument.MasterInstrument.PointValue


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
         {
                 // Displays the master instrument's point value at the bottom right of the chart
                 Draw.TextFixed(this, "Point value: ", Bars.Instrument.MasterInstrument.PointValue.ToString(), TextPosition.BottomRight);
         } |




 


Additional Access Information
This property can be accessed without a null reference check in the OnBarUpdate() event handler. When the OnBarUpdate() event is triggered, there will always be an Instrument object. Should you wish to access this property elsewhere, check for null reference first. e.g. if (Instrument != null)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





 
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
 
 
 



