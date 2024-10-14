










 


GetHeaderPart()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getheaderpart.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NTTabPage Class](nttabpage_class.htm) &gt;
GetHeaderPart() | [Previous page](nttabpage_cleanup.htm)
[Return to chapter overview](nttabpage_class.htm)










Definition
----------


Indicates the tab header name.


 



Examples
--------




| ns |
| --- |
| // NTTabPage member. Required for determining the tab header name
protected override string GetHeaderPart(string variable)
{
     // Determine the text for the tab header name
     switch (variable)
     {
         case "@INSTRUMENT": return Instrument == null ? Resource.GuiNewTab : Instrument.MasterInstrument.Name;
         case "@INSTRUMENT\_FULL": return Instrument == null ? Resource.GuiNewTab : Instrument.FullName;
     }
     return variable;
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
 
 
 



