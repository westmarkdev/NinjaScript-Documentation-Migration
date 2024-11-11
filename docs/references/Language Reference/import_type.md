---
title: Import Type
pathName: import_type
parent: language_reference
order: 7
status: imported
section: references
---

## Import Type

Custom data Import Types can be developed to allow for the importing of historical data from any format. Two important event handler methods are documented in this section:

### Methods and Properties

{% table %}

* Name

* Description

---

* [OnNextInstrument()](onnextinstrument)

* Called at the beginning of the import process

---

* [OnNextDataPoint()](onnextdatapoint)

* Called for each line of data contained in the file being imported

---

{% /table %}
