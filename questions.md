1. Discuss your strategy and decisions implementing the application. Please, considertime
complexity, effort cost, technologies used and any other variable that you understand
important on your development process.

In the topic of technologies used: I decided to use Django both because it was recommended,
and because I am very familiar with it. The 4.2 version was the one I picked because it is
the LTS version I am most familiar with. 
Due to the low complexity of the problem, I also opted to develop all of the solution within
the Django environment, making use of the Django Template feature and simple FBVs.
As for the csv parsing library, the standard csv Python Library proved to be more than enough
for the job.

In the topic of time complexity and effort cost:
My original idea was to create models that would represent the csv tables.
I would, after creating the models, create an empty migration which would
run a script that would read the files and populate the tables, using the
standard sqlite database. This would then be part of the setup of the project.
With the tables populated, I could then make use of the Django ORM to
query these tables to resolve the task.

I didnt do that because the test description made very clear that
a database wasnt necessary, so, instead, I treated the csv files as the database,
and developed a few functions in the utils.py module which are the main part of the solutions of this test.
I developed these functions with the idea that these CSVs could instead be way bigger than they
actually are, so I put a lot of effort in making sure that every iteration when reading or rearranging
the data would make the most out of it. 
This can be seen in functions like get_legislator_data and get_bill_data, where it is necessary to
iterate over all legislators and bills, but it is also necessary to retrieve unfiltered data from
other related tables. Instead of iterating on these related tables for every iteration in legislators
or bills, I filtered and reorganized these related tables in a way that only one unique iteration was
necessary, for after that the related data could be retrieved directly, without the need for filtering again.

I also developed these functions with the philosophy of making its purpose very concise and defined,
with the idea of allowing them to be reused in a project that would grow in scope.

In the end, I also decided to develop a few unit tests, to guarantee the solution integrity.

2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?

Assuming the column "Bill Voted on Date" would be a column in the votes csv, where a vote_id 
is related to a bill_id, and also that every legislator would cast their vote in the same date: I could
change the get_bill_data function, specifically the votes_dict declaration, which is a dict that
relates a bill_id to a vote_id, to not only relate the bill_id to a vote_id, but also to the date
when the vote happened. This would allow the date to be retrieved from this dictionary for every
bill iterated.

Assuming the "Co-Sponsors" would be a new column in the bills csv, since this is a information
available in every bill that is iterated in the get_bill_data, it could be easily retrieved much 
like the 'id' and 'title' columns are retrieved. 
In the case the Co-Sponsors is a new csv file, relating a legislator_id to a bill_id, a process
similar to the one made for the votes_dict dictionary would be necessary, where a dictionary is created
with the goal of relating a bill_id to a list of legislator ids.


3. How would you change your solution if instead of receiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?

Assuming this list would be given via a html form, I would create Django view that would use a form class
to validate this data. After that, I would generate these files in the server using the standard csv
python library and return them in the views's response.


4. How long did you spend working on the assignment?

Approximately 5 hours.


