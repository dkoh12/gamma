# Company Data Miner

## Overview

### Instructions
Implement a program that ingests the given JSON file, you may choose whatever language you want. If you decide to use a JavaScript framework to facilitate console based entry, please note this and explain how to use and all requirements to run your code locally.  

Once ingested, we want to be able to run queries against this data and return the count and the list of Human Readable names for this query.

This exercise should take around 1-2 hours

### Breakdown of supported instructions:

* `locate`.  This instruction will allow us to find the list of companies by Location (state only).
		`e.g. : locate CA`
* `find_before`. This instruction will allow us to find the list of companies before a specific year.  This is an inclusive operation.
	`e.g.: find_before 1999`
	
* `find_after`. This instruction will allow us to find the list of companies after a specific year.  This is an inclusive operation
	`e.g.: find_after 2000`

* `find_between`.  Find the list of companies based on the number of full time employees. `e.g. find_between 1,001-5,000`. 
	* Possible Options:
	```
	['1-10', '11-50', '51-200', '201-500', '501-1,000', '1,001-5,000', '5,001-10,000', '10,001+']
	```
	**Note, if the company has `N/A` or `NA` as a value for `full_time_employees`, ignore it**


* `find_type`.  Find all companies by Company Type. `e.g. find_type Data/Technology'`
	* Possible Types are:
```
[’N/A’,
 'Aerospace and Defense',
 'Business & Legal Services',
 'Data/Technology',
 'Education',
 'Energy',
 'Environment & Weather',
 'Finance & Investment',
 'Food & Agriculture',
 'Geospatial/Mapping',
 'Governance',
 'Healthcare',
 'Housing/Real Estate',
 'Insurance',
 'Lifestyle & Consumer',
 'Media',
 'Research & Consulting',
 'Scientific Research',
 'Transportation']```
 
 
## Example output
#### We are expecting all output to be returned via console

**Locate Example**

```
> python my_program.py data.json locate MD

```
would return a dataset like this:

```
Company Names:
Overture Technologies, Smartronix, ...

Number of Companies: 34
```

**Find before/after Example**

```
> python my_program.py data.json find_after 2002

```

```
Company Names:
Overture Technologies, Smartronix, ...

Number of Companies: 349
```

**Find Employees in Range Example**

```
> python my_program.py data.json find_employees_in_range 1,001-5,000

```

```
Company Names:
Overture Technologies, Smartronix, ...

Number of Companies: 99
```

**Find Companies by Type**

```
> python my_program.py data.json find_type 'Geospatial/Mapping'

```

```
Company Names:
Overture Technologies, ...

Number of Companies: 3
```

## Expected deliverables
* **Readme file** -- An explanation  of your design and how to use your program/solution.  Example details would be Why you chose the language you did, any design decisions  that were made due to the constraints provided, as well as any assumptions you made
* **Tests** -- Please include tests as well as examples how to run them in your `README`
* **Requirements** -- List of requirements to run your code locally.  If the code is OS dependent, please make note of this also.

**Once complete, please email your solution to `ronald.brown@bain.com`**


## Example Data 
 **For a larget example, please see data.json included with this README**
 
```
[
  {
    "company_name_id": "3-round-stones-inc",
    "company_name": "3 Round Stones, Inc.",
    "url": "http://3RoundStones.com",
    "year_founded": 2010,
    "city": "Washington",
    "state": "DC",
    "country": "us",
    "zip_code": 20004,
    "full_time_employees": "1-10",
    "company_type": "Private",
    "company_category": "Data/Technology",
    "revenue_source": "Data analysis for clients, Database licensing, Subscriptions",
    "business_model": "Business to Business, Business to Consumer",
    "social_impact": "",
    "description": "3 Round Stones produces a platform for publishing data on the Web. 3 Round Stones provides commercial support for the Callimachus Data Platform, used by the Fortune 2000 and US Government Agencies publishing and consuming data.  Headquartered in Arlington, Virginia, we're seasoned entrepreneurs who are passionate about solving real world problems through open data and open Web standards.",
    "description_short": "Our Open Source platform is used by the Fortune2000 and US Government Agencies to collect, publish and reuse data, both public and proprietary.",
    "source_count": "NA",
    "data_types": "",
    "example_uses": "",
    "data_impacts": "[]",
    "financial_info": "3 Round Stones is a profitable, self-funded, woman-owned start-up.  Our team has several successful serial entrepreneurs.  As entrepreneurs, we've benefited from the valuable guidance by seasoned advisers and mentors in the mid-Atlantic region who have guided our team through multiple start-ups, outside funding and an acquisition by a Fortune 100 company in 2005.",
    "last_updated": "2014-11-12 14:44:25.969871"
  }
 ]
```