﻿










 


NinjaScript Wizard







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ns_wizard.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Editor](editor.htm) &gt;
NinjaScript Wizard | [Previous page](ns_explorer.htm)
[Return to chapter overview](editor.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









The NinjaScript Wizard is used to generate the minimum code to get started programming any supported NinjaScript type.  This wizard will allow you to define any default properties, add custom input parameters, add additional data series, and add any relevant event methods.  There are a number of different properties and options available in the NinjaScript Wizard depending on the type of NinjaScript object you are creating.  


 


The information on this page is to be used as a standard overview of the various components of the NinjaScript Wizard.  For more information on NinjaScript methods and properties, please see the NinjaScript Language Reference section of our Help Guide.


![tog_minus](tog_minus.gif)        [Opening the NinjaScript Wizard](javascript:HMToggle('toggle','OpeningTheNinjaScriptWizard','OpeningTheNinjaScriptWizard_ICON'))




|  |
| --- |
| Creating a new NinjaScript file
The NinjaScript Wizard can be opened from the NinjaScript Editor by selecting the + symbol on the tab row, and then selecting the NinjaScript object type you wish to develop.
 
NS_Wizard_1
 
You can also right click on any of the NinjaScript categories listed in the [NinjaScript Explorer](ns_explorer.htm) and select "New..."
 
NS_Wizard_2 |



![tog_minus](tog_minus.gif)        [Understand the NinjaScript Wizard Display](javascript:HMToggle('toggle','UnderstandtheNinjaScriptWizardDisplay','UnderstandtheNinjaScriptWizardDisplay_ICON'))




|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Display Overview
NS_Wizard_3
 


|  |  |
| --- | --- |
| 2. Wizard Screen | Displays relevant information pertaining to the step of wizard you have navigated to and will provide instructions to help you define your script at various stages. |
| 3. Wizard Controls | Buttons used to perform various actions pertaining to the script that is being created.  Selecting Generate at any time will exit the wizard and open your script in the NinjaScript Code Editor (Note:  You cannot return back to the NinjaScript Wizard once the code is generated). |


 |



![tog_minus](tog_minus.gif)        [Understanding the Wizard Screens](javascript:HMToggle('toggle','UnderstandingTheWizardScreens','UnderstandingTheWizardScreens_ICON'))




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Optional Pages
The NinjaScript Wizard has a number of different pages available used to define various steps of your custom script.  Please note that the table below describes ALL of the pages available from the Wizard, but does not imply that these steps will be available for the script you are currently creating.
 


|  |  |
| --- | --- |
| Welcome | The first step of the Wizard, used to identify which type of object is being created  |
| General | Used to define a name and description to identify the NinjaScript file |
| Default Properties | Sets various properties and start behavior for the script being created |
| Additional Data | Used to optionally add additional data series such as minute, tick, etc or even custom series you may plan on calculating programmatically    |
| Additional Event Methods | Optionally add additional event methods to your custom script, such as [OnMarketData](onmarketdata.htm), [OnMarketDepth](onmarketdepth.htm), etc |
| Input Parameters | Used to define any public properties that may be used in your script |
| Plots and Lines | Optionally add visual plots or lines to your script for charting purposes |
| Finish | Last page of the Wizard, gives you a chance to go back and review each page if desired before finishing generating the script. |


 |






 
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
 
 
 


HMInitToggle('OpeningTheNinjaScriptWizard\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'OpeningTheNinjaScriptWizard\',\'OpeningTheNinjaScriptWizard\_ICON\')');
HMInitToggle('OpeningTheNinjaScriptWizard','hm.type','dropdown','hm.state','0');
HMInitToggle('UnderstandtheNinjaScriptWizardDisplay\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'UnderstandtheNinjaScriptWizardDisplay\',\'UnderstandtheNinjaScriptWizardDisplay\_ICON\')');
HMInitToggle('UnderstandtheNinjaScriptWizardDisplay','hm.type','dropdown','hm.state','0');
HMInitToggle('UnderstandingTheWizardScreens\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'UnderstandingTheWizardScreens\',\'UnderstandingTheWizardScreens\_ICON\')');
HMInitToggle('UnderstandingTheWizardScreens','hm.type','dropdown','hm.state','0');


