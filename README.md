
# Company Strategies to Prevent Employee Burnout in the Workplace


## Introduction
Employee burnout is an escalating issue that significantly impacts productivity, employee satisfaction, and overall organizational performance. 
Recognizing this critical challenge, we embarked on a project that aims to analyze and predict burnout among employees. 

The primary objective of this project is to identify key factors contributing to employee burnout and predict burnout risks. 
By leveraging a comprehensive dataset and advanced analytical techniques, we aim to uncover critical insights into the causes of burnout and create effective strategies for early intervention. 
This project seeks to provide suggestions to enhance employee well-being, improve productivity, and foster a supportive work environment.


## Data
The data used in this project is collected from two datasets and web scraping from two credible websites.

- [df1 - Remote Work & Mental Health](https://www.kaggle.com/datasets/iramshahzadi9/remote-work-and-mental-health)
- [df2 - Absenteeism At Work ](https://www.kaggle.com/datasets/saumitgp/absenteeism-at-work?select=Absenteesim+At+Work.csv)

- [url1 - Burnout Statistics](https://flair.hr/en/blog/burnout-statistics/)
- [url2 - Job burnout](https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/burnout/art-20046642)


**Main Challenges**:
- Incomplete data for testing specific hypotheses, for example hypothesis 4 and 5
- Web scraping due to different websites structures
- Cleaning data related to web scraping, especially standardizing formats and making data usable for the project


**Strengths**:
- Diverse sources: Data is collected from multiple credible sources
- Good usability of datasets =7.06
- Recent datasets (2 years ago, 8 months ago) and articles (November 2023 and January 2024)


**Weaknesses**:
- Limited data resources: we were not able to find a lot of datasets related to burnout in Kaggle and websites
- Limited time to work in the project 


## Hypothesis
### Hypothesis 1: Remote jobs result in fewer cases of burnout.
Contrary to our belief, our analysis reveals that remote work is associated with a higher incidence of burnout cases, with elevated stress levels being a significant contributing factor (438 cases).
Onsite work exhibits the highest number of low-stress cases (158), whereas remote work is associated with the highest levels of stress (152).
A significant 86% of remote workers experience some degree of burnout compared to 70% amongst on-site workers (data source: https://flair.hr/en/blog/burnout-statistics/).
Around 40% of remote workers struggle to disconnect from work, leading to a higher burnout rate than office employees, with 86% of full-time remote workers reporting burnout (data source: https://flair.hr/en/blog/burnout-statistics/).


### Hypothesis 2: Is seniority level related to burnout? If not, what are the primary contributors to burnout?
When examining burnout cases across different job roles and levels of seniority, the data shows no clear indication that higher seniority levels are associated with increased burnout.
The data reflects the following insights:
Seniors exhibit the highest ratio of employees to burnout cases, but this does not necessarily imply high cases of burnout.
Junior and associate roles have slightly lower ratios, yet it's essential to consider other influencing factors such as workload, work-life balance, and support systems.

#### Burnout Relationship with Job Role and Work Location
The data suggests that burnout rates vary by job role and work location:
Remote work tends to be associated with higher burnout rates for Data Scientists and Project Managers.
Onsite work shows higher burnout rates for Data Scientists, Project Managers and Sales roles.
HR roles experience higher burnout rates among hybrid workers.
Overall, there is no clear pattern indicating that a specific work location consistently leads to higher burnout across all job roles.

#### Relationship Between Industry and Burnout
The finance industry exhibits the highest proportion of burnout (0.27),followed by Healthcare with a burnout proportion of 0.26.
The data indicates that burnout proportions vary across industries, with finance, healthcare, and IT showing higher levels compared to others.

#### Relationship Between Region and Burnout
The data indicates that burnout proportions vary across regions, with Asia showing the highest levels (0.27) and South America the lowest (0.23). This variation suggests that regional factors, including cultural, economic, and work environment differences,can influence employee burnout rates.


### Hypothesis 3: Individuals who work long hours more likely to experience burnout.
The data indicates a clear relationship between the number of hours worked and burnout levels. 
Employees working more than 40 hours per week exhibit higher burnout rates (51.6%) compared to those working 40 hours or less (48.4%).
45% noted an increase in work hours since the pandemic began (data source: https://flair.hr/en/blog/burnout-statistics/).


### Hypothesis 4: Individuals who smoke or drink are at a higher risk of experiencing burnout
The data indicates that social smokers have a higher average absenteeism time compared to non-social smokers. While non-social smokers average around 13.52 hours of absenteeism, social smokers average about 15.38 hours. 
It doesn't necessarily indicate a direct link to a higher risk of experiencing burnout.

#### Social drinker analysis
The data indicates that there are more social drinkers than social smokers in this dataset.
Non-social drinkers have a higher average absenteeism time compared to social drinkers. While non-social drinkers average around 16.03 hours of absenteeism, social drinkers average about 12.24 hours.
The number of non-social drinkers are higher than social drinkers, so there is not a clear link between social drinking and a lower risk of absenteeism and burnout.


### Hypothesis 5: Can absenteeism predict burnout?
The relationship between absenteeism and burnout is complex and multifaceted. While absenteeism can be an indicator of potential issues such as burnout, it alone isn't sufficient to make a conclusive prediction.

#### Reasons for absence
- Musculoskeletal Issues is the leading cause of absenteeism, with 842 cases. This highlights the importance of ergonomic workspaces and physical health programs. 
- The second most common reason is injuries with 729 cases. Safety protocols and preventive measures are crucial to reduce workplace injuries.
It is estimated that each year employee absence, decreased productivity and occupational injuries contribute to $190 billion in healthcare-related expenses (data source: https://flair.hr/en/blog/burnout-statistics/).
- Mental disorders is less frequent with only 19 cases reported.
- Absenteeism isn't sufficient to make a conclusive prediction of burnout. 
60% of work absences are due to psychological stress, but we cannot assume this is related to burnout (data source: https://flair.hr/en/blog/burnout-statistics/).



## Methodology
### Data Collection
- Web scraping using Python (libraries: 'requests', 'BeautifulSoup').
- Datasets imported from Kaggle


### Data Cleaning and Transformation
- Removing duplicates and irrelevant information
- Handling null and missing values by using "unknown" statement
- Adding new fields with new categories
- Using merge, replace and apply functions to formulate the data
- Formatting column names, numerical and categorical values for consistency


### Data Analysis
- Use aggregation and filtering techniques, such as groupby, agg, filters and pivot tables
- Visualizations using 'matplotlib' and 'seaborn' to identify trends and patterns


## Conclusions
Burnout is a multifaceted issue influenced by various factors such as work location, industry, region, job role, and individual behaviors. While some patterns emerge, such as the higher burnout rates among remote workers and certain industries, it is crucial to consider the broader context and multiple contributing factors. Effective interventions and support strategies should be tailored to address these diverse influences, promoting a healthier and more productive work environment for all employees.

Strategies to prevent burnout among employees:
- Encourage Social Interactions: promote on-site work to encourage employees to interact with their colleagues. Team-building activities, social events, or even casual meetings can help build closer relationships. Remote workers higher level of burnout.
- Offer Employee Benefits: wellness programs, gym memberships, Financial Education programs (with aim to develop knowledge and skills to manage finances effectively), especially for remote workers who reports higher levels of stress.
- Analyzing the stress levels in our dataset highlights the importance of prioritizing stress management. Drawing conclusions from the Mayo Clinic article, we recommend implementing counseling, workshops, stress-management training, online and on-site relaxing activities, such as yoga, meditation, or tai chi.
- Finance, Healthcare, and IT sectors experience higher levels of employee burnout. Therefore, we recommend investing in tailored support programs aimed at alleviating workplace stress and promoting employee well-being.
- Our findings reveal a connection between long working hours and burnout cases. This highlights the critical need to create an open and supportive environment where employees feel comfortable seeking help as suggested in Mayo clinic article.
- Musculoskeletal issues and injuries are the leading causes of absenteeism with 842 and 729 cases respectively. This highlights the importance of ergonomic workspaces and physical health programs (data source, Mayo Clinic article).



## Further Improvements
- To deepen our understanding, we should expand our research by further exploring the link between absenteeism patterns and burnout. This will involve incorporating additional data sources.
- Additional data sources to be incorporated in order to improve our understanding between seniority level and burnout.
- Conduct further investigation into the specific types of stress-management programs and interventions that organizations can implement
to prevent burnout



## Links to Data Sources and Trello
### Datasets
- [df1 - Remote Work & Mental Health](https://www.kaggle.com/datasets/iramshahzadi9/remote-work-and-mental-health)
- [df2 - Absenteeism At Work ](https://www.kaggle.com/datasets/saumitgp/absenteeism-at-work?select=Absenteesim+At+Work.csv)

### Articles Scrapped
- [url1 - Burnout Statistics](https://flair.hr/en/blog/burnout-statistics/)
- [url2 - Job burnout](https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/burnout/art-20046642)

### Trello
- [Trello Board](https://trello.com/b/CSiIcxRK/project-1-vera-yorgos)

### Presentation
- [Presentation](https://docs.google.com/presentation/d/1YnfzzLF3teajYI97MKeCV_HaoSKXAIURQxlcrVoKZPo/edit?usp=sharing)
