










 


INTTabFactory Interface







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?inttabfactory_class.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
INTTabFactory Interface | [Previous page](iintervalprovider_barsperiod.htm)
[Return to chapter overview](add_on.htm)










If you wish to have tab page functionality like adding, removing, moving, duplicating tabs you must create a class which implements the INTTabFactory interface. 


 


 


 


This interface contains two methods which must be hidden:


 


NTWindow CreateParentWindow();
------------------------------


NTTabPage CreateTabPage(string typeName, bool isNewWindow = false);
-------------------------------------------------------------------



Examples
--------




| ns |
| --- |
| public class MyWindowFactory : INTTabFactory
{
     // INTTabFactory member. Creates the parent window that contains tabs
     public NTWindow CreateParentWindow()
     {
         return new MyWindow();
     }
 
     // INTTabFactory member. Creates new tab pages whenever the user presses the + button
     public NTTabPage CreateTabPage(string typeName)
     {
         return new MyWindowTabPage();
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
 
 
 



