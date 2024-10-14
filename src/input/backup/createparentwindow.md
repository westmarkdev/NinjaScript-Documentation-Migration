










 


CreateParentWindow()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?createparentwindow.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [INTTabFactory Interface](inttabfactory_class.htm) &gt;
CreateParentWindow() | [Previous page](inttabfactory_class.htm)
[Return to chapter overview](inttabfactory_class.htm)










This determines which [NTWindow](ntwindow.htm) is created as the parent window for our Add On.


 



Examples
--------




| ns |
| --- |
| // INTTabFactory member. Creates the parent window that contains tabs
public NTWindow CreateParentWindow()
{
     return new MyWindow();
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
 
 
 



