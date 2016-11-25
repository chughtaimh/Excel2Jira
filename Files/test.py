from excel2jira import format_row, excel_to_jira, split_table

def tests():

	## TESTS: split_table
	# One Row
	t = "Campaign ID	Campaign Name	Placement ID	Placement Name	Ad Type	Impressions"
	assert split_table(t) == (t, "")
	# Multiple Rows
	t = """Campaign ID	Campaign Name	Placement ID	Placement Name	Ad Type	Impressions
607295	2016 Q3 Liberty Mutual DR OLV	1300614	DESK_iPR_T1_15s_High CPM	interactive_preroll	93183
588435	2016 Q2 Liberty Mutual OLV 	1125091	DESK_iPR_X_Quintile 2 Sites_15s	interactive_preroll	291258
588435	2016 Q2 Liberty Mutual OLV 	1125851	DESK_iPR_RT1_Quintile 3 Sites_30s	interactive_preroll	1970703
607295	2016 Q3 Liberty Mutual DR OLV	1238479	DESK_iPR_T1_15s	interactive_preroll	5851411
"""
	assert split_table(t) == (t.split('\n')[0], t.split('\n')[1:])
	# Empty table
	t = ""
	assert split_table(t) == ""
	# Not a table
	t = "This is not a table."
	assert split_table(t) == (t, '')

	## TESTS: format_row
	# Single column row
	t = "607295"
	assert format_row(t) == "|{row}|\n".format(row=t)
	# Multiple column row
	t = "607295	2016 Q3 Liberty Mutual DR OLV	1300614"
	assert format_row(t, '||') == "||607295||2016 Q3 Liberty Mutual DR OLV||1300614||\n"
	# Empty row
	t = ""
	assert format_row(t) == ""
	# Not a row
	t = "This is not a row"
	assert format_row(t) == "|{row}|\n".format(row=t)

	## TESTS: excel_to_jira
	# Single column table
	t = "Campaign ID	Campaign Name	Placement ID	Placement Name	Ad Type	Impressions"
	assert excel_to_jira(t) == "||{table}||\n".format(table=t.replace('\t', '||'))
	# Multiple column table
	t = """Campaign ID	Campaign Name	Placement ID	Placement Name	Ad Type	Impressions
607295	2016 Q3 Liberty Mutual DR OLV	1300614	DESK_iPR_T1_15s_High CPM	interactive_preroll	93183
"""
	assert excel_to_jira(t) == "||{header}||\n|{col}|\n".format(
		header=t.splitlines()[0].replace('\t', '||'),
		col=t.splitlines()[1].replace('\t', '|'))
	# Empty table
	t = ""
	assert excel_to_jira(t) == ""
	# Not a table
	t = "This is not a table."
	assert excel_to_jira(t) == "||{table}||\n".format(table=t)

if __name__ == '__main__':
	tests()