










 


OnPropertyChanged()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onpropertychanged.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
OnPropertyChanged() | [Previous page](superdomcolumn_onpositionupdate.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


This method should be used any time you wish to repaint the column instead of calling [OnRender()](superdomcolumn_onrender.htm) directly.



Method Return Value
-------------------


This method does not return a value


 


Syntax
------


OnPropertyChanged()



Parameters
----------


This method does not require any parameters



Examples
--------




| ns |
| --- |
| // Repaint the SuperDOM column
OnPropertyChanged(); |






 
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
 
 
 



