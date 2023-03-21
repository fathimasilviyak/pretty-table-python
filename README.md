# pretty-table-python

PrettyTable lets you print tables in an attractive ASCII form.

First we have to intall the prettytable package from PyPi into our code.
(files->settings->Project: project_name->project interpreter->add package->select and install package).

Then import the PrettyTable class from the prettytable pacakage.

Then create an object for the PrettyTable class. eg: table = PrettyTable().

Then we can access the attributes and methods assosciated with the created object of the PrettyTable class.

We can insert the data as column by column or row by row.
eg: table.add_column("column name", [list of items in that column])
  : table.add_row([list of items in a particular row])

We can change alignment of the table data by assigning different values to the align attribute of the PrettyTable class.
eg: table.align = "l" , to align data to left.

For a particular table object we can change the attribute values and can also perform various methods on it.

Link for documentation: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

This helps to understand how to import external python libraries from PyPi and utilise the classes defined in it.

It also helps to explore various attributes and methods of the imported class .

