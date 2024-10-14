










 


CreateTabPage()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?createtabpage.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [INTTabFactory Interface](inttabfactory_class.htm) &gt;
CreateTabPage() | [Previous page](createparentwindow.htm)
[Return to chapter overview](inttabfactory_class.htm)










This determines which [NTTabPage](nttabpage_class.htm) is created whenever a new tab is needed in our parent window for our Add On.


 



Examples
--------




| ns |
| --- |
| // INTTabFactory member. Creates new tab pages whenever the user presses the + button
public NTTabPage CreateTabPage(string typeName, bool isNewWindow = false)
{
   return new MyWindowTabPage();
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
 
 
 



