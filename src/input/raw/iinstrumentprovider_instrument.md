










 


Instrument







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iinstrumentprovider_instrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [IInstrumentProvider Interface](iinstrumentprovider_interface.htm) &gt;
Instrument | [Previous page](iinstrumentprovider_interface.htm)
[Return to chapter overview](iinstrumentprovider_interface.htm)










In order for instrument linking to work properly in your Add On, Instrument must be created.


 



Examples
--------




| ns |
| --- |
| // IInstrumentProvider member
public Instrument Instrument
{
     get { return instrument; }
     set
     {
         if (instrument != null)
          {
               // Unsubscribe to subscriptions to previously selected instrument
          }
               
         if (value != null)
          {
               // Create subscriptions for the newly selected instrument
          }
 
          instrument = value;
 
         // Send instrument to other windows linked to the same color
          PropagateInstrumentChange(value);
 
         // Update the tab header name
          RefreshHeader();
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
 
 
 



