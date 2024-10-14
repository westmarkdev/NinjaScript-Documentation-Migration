










 


IIntervalProvider Interface







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iintervalprovider_interface.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
IIntervalProvider Interface | [Previous page](iinstrumentprovider_instrument.htm)
[Return to chapter overview](add_on.htm)










When creating your [NTTabPage](nttabpage_class.htm), if you wish to use the [interval link](linking_windows.htm), be sure to implement the IIntervalProvider interface.


 



Examples
--------




| ns |
| --- |
| public class MyWindowTabPage : NTTabPage, IIntervalProvider
{
     public MyWindowTabPage()
     {
         /* Define the content for our NTTabPage. We can load loose XAML to define controls and layouts
         if we so choose here as well.
 
          Note: XAML with event handlers defined inside WILL FAIL when attempted to load.
          Note: XAML with "inline code" WILL FAIL when attempted to load */
     }
 
     // IIntervalProvider member
     public BarsPeriod BarsPeriod { get; set; }
 
     // Be sure to include all the required NTTabPage members as well
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
 
 
 



