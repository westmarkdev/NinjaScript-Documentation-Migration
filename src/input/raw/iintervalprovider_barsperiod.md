










 


BarsPeriod







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iintervalprovider_barsperiod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [IIntervalProvider Interface](iintervalprovider_interface.htm) &gt;
BarsPeriod | [Previous page](iintervalprovider_interface.htm)
[Return to chapter overview](iintervalprovider_interface.htm)










In order for interval linking to work properly in your Add On, BarsPeriod must be created.



Examples
--------




| ns |
| --- |
| // IIntervalProvider member
public BarsPeriod BarsPeriod { get; set; } |






 
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
 
 
 



