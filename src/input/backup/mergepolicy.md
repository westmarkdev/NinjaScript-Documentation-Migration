










 


MergePolicy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?mergepolicy.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
MergePolicy | [Previous page](instrumenttype.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the Merge Policy configured for the [Master Instrument properties](editing_instruments.htm).



Property Value
--------------


Represents the MergePolicy that is configured for the current master instrument.


 


Possible values are:


 




|  |  |
| --- | --- |
| DoNotMerge | No merge policy is applied |
| MergeBackAdjusted | Merge policy is applied between contracts along with rollover offsets |
| MergeNonBackAdjusted | Merge policy is applied between contracts without offsets |
| UseGlobalSettings | Uses the value configured from Tools -&gt; Options -&gt; Market Data |



 


Syntax
------


Bars.Instrument.MasterInstrument.MergePolicy


 


Examples
--------




| ns |
| --- |
| //Prints a warning, indicating what merge policy is in use if not using global settings
if (Bars.Instrument.MasterInstrument.MergePolicy != MergePolicy.UseGlobalSettings)
{
 Print("Warning: Instrument has merge policy of " + Bars.Instrument.MasterInstrument.MergePolicy);
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
 
 
 



