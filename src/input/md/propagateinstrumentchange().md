










 


PropagateInstrumentChange()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?propagateinstrumentchange().htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
PropagateInstrumentChange() | [Previous page](strategybase.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


In an [NTWindow](ntwindow.htm), PropagateInstrumentChange() sends an Instrument to other windows with the same Instrument Linking color configured. 


 




|  |
| --- |
| Notes: 
•A public Instrument property must be defined in order to use PropagateInstrumentChange(), as in the example below•For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |




Example
-------




| ns |
| --- |
| // IInstrumentProvider member. Required if you want to use the instrument link mechanism on an NTWindow.
public Cbi.Instrument Instrument
{
   get { return instrument; }
   set
   {
       // Process logic related to switching instruments, such as:
       // Unsubscribe to subscriptions to old instruments...
       // Subscribe for the new instrument...
       // Change the value displayed in an Instrument Selector in the NTWindow...
       // Update the tab header name on AddOnFramework to be the same name as the new instrument...
       // etc...
 
       // Send instrument to other windows linked to the same color
       PropagateInstrumentChange(value);
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
 
 
 



