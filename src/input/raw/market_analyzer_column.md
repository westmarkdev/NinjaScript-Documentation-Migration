










 


Market Analyzer Column







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?market_analyzer_column.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Market Analyzer Column | [Previous page](showtransparentplotsindatabox.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Market Analyzer columns can be used to further enhance your Market Analyzer experience by providing custom columns displaying values of your choosing. The methods and properties covered in this section are unique to custom Market Analyzer Column development.


 


In this section
---------------




|  |  |
| --- | --- |
| [CurrentText](currenttext.htm) | Sets text to be displayed in the Market Analyzer column. |
| [CurrentValue](currentvalue.htm) | The value to be displayed in the Market Analyzer Column. |
| [DataType](datatype.htm) | Determines the data type displayed in a Market Analyzer Column. |
| [FormatDecimals](formatdecimals.htm) | Rounds the value contained in [CurrentValue](currentvalue.htm) to a specified number of decimal places before displaying it in the Market Analyzer column. |
| [IsEditable](iseditable.htm) | Determines if a Market Analyzer Column is editable. |
| [PriorValue](priorvalue.htm) | Contains the last value of [CurrentValue](currentvalue.htm). PriorValue is assigned the value of CurrentValue immediately before CurrentValue is updated. |






 
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
 
 
 



