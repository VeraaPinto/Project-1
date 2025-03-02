!pip install "kagglehub[pandas-datasets]"

import os
os.environ['KAGGLE_USERNAME'] = 'veraapinto'
os.environ['KAGGLE_KEY'] = 'e47f4642064e3cd9feb2dbb913a63bce'

# Install the Kaggle package
!pip install kaggle

# Download the dataset
!kaggle datasets download -d iramshahzadi9/remote-work-and-mental-health
import zipfile
with zipfile.ZipFile('remote-work-and-mental-health.zip', 'r') as zip_ref:
    zip_ref.extractall('remote-work-and-mental-health')
file_path = "remote-work-and-mental-health/Impact_of_Remote_Work_on_Mental_Health.csv"
import pandas as pd
import numpy as np
df = pd.read_csv(file_path)
df.head()

# Download the dataset
!kaggle datasets download -d saumitgp/absenteeism-at-work
import zipfile
with zipfile.ZipFile('absenteeism-at-work.zip', 'r') as zip_ref:
    zip_ref.extractall('absenteeism-at-work')
file_path2 = "absenteeism-at-work/Absenteesim At Work.csv"
df2 = pd.read_csv(file_path2)
df2.head()

import seaborn as sns
import matplotlib.pyplot as plt

# cleanning df2 absenteeism-at-work
df2.columns = df2.columns.str.replace(' ', '_').str.replace('/', '_').str.lower().str.strip()

reason_for_absence_key_value = pd.DataFrame({
    "Roman_Numeral": ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 
                      'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 
                      'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII'],
    "Number": list(range(1, 29)),
    "reason_for_absence": [
        "Certain infectious and parasitic diseases",
        "Neoplasms",
        "Diseases of the blood and...",
        "Endocrine, nutritional and...",
        "Mental and behavioural disorders",
        "Diseases of the nervous system",
        "Diseases of the eye and adnexa",
        "Diseases of the ear and mastoid process",
        "Diseases of the circulatory system",
        "Diseases of the respiratory system",
        "Diseases of the digestive system",
        "Diseases of the skin and...",
        "Diseases of the musculoskeletal system...",
        "Diseases of the genitourinary system",
        "Pregnancy, childbirth and the puerperium",
        "Certain conditions originating in the...",
        "Congenital malformations, deformations...",
        "Symptoms, signs and abnormal clinical...",
        "Injury, poisoning and certain other...",
        "External causes of morbidity and mortality",
        "Factors influencing health status...",
        "Patient follow-up",
        "Medical consultation",
        "Blood donation",
        "Laboratory examination",
        "Unjustified absence",
        "Physiotherapy",
        "Dental consultation"
    ],
    "keyword_reason_for_absence": [
        "infectious_diseases", "neoplasms", "blood_disorders", "endocrine_disorders", 
        "mental_disorders", "nervous_system", "eye_diseases", "ear_diseases", 
        "circulatory_diseases", "respiratory_diseases", "digestive_diseases", 
        "skin_diseases", "musculoskeletal", "genitourinary", "pregnancy", 
        "perinatal_conditions", "congenital_disorders", "general_symptoms", 
        "injuries", "external_causes", "health_factors", "follow_up", 
        "consultation", "blood_donation", "lab_examination", 
        "unjustified_absence", "physiotherapy", "dental"
    ]
})

df2 = df2.merge(reason_for_absence_key_value, left_on='reason_for_absence', right_on='Number', how='left')

day_mapping = {
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday'
}

df2['day_of_the_week'] = df2['day_of_the_week'].replace(day_mapping)

education_mapping = {
    1: 'high school',
    2: 'graduate',
    3: 'postgraduate',
    4: 'master and doctor'
}

df2['education'] = df2['education'].replace(education_mapping)

yes_no_mapping = {1: 'yes', 0: 'no'}

df2['disciplinary_failure'] = df2['disciplinary_failure'].replace(yes_no_mapping)
df2['social_drinker'] = df2['social_drinker'].replace(yes_no_mapping)
df2['social_smoker'] = df2['social_smoker'].replace(yes_no_mapping)

df2 = df2.dropna(how='all')
df2 = df2.drop(columns=['Roman_Numeral','Number'])
duplicate_rows = df2[df2.duplicated(keep=False)]
df2 = df2.drop(index=duplicate_rows.index)
df2 = df2.fillna('Unknown')

#checked all columns .unique() - corrections done
#checked null values: df2.isnull().mean() * 100 AND df2.isnull().sum() AND sns.heatmap(df2.isnull(), cbar=False, cmap='viridis') -> plt.show() - very few in added columns
#checked duplicates: df2[df2.duplicated()] AND any_duplicates_left = df2_unique.duplicated().any()
#checked data types df2.dtypes

# cLEANING DF
df.columns = df.columns.str.lower()
df.isnull().mean()*100
df.isnull().sum()
def fill_null_value(row):
    if (row['stress_level'] == 'high' and row['Productivity_Change'] == 'decrease' and row['sleep_quality'] == 'poor'):
        return "Burnout"
    elif (row['stress_level'] == 'high' and row['Productivity_Change'] == 'decrease' and row['sleep_quality'] == 'average'):
        return "Anxiety"
    else:
        return "Unknown"

# Apply the function to the DataFrame
df['mental_health_condition'] = df.apply(lambda row: fill_null_value(row) if pd.isnull(row['mental_health_condition']) else row['mental_health_condition'], axis=1)

# Replace blank (None or NaN) cells with 'unknown':
df['physical_activity'] = df['physical_activity'].replace(np.nan, 'Unknown')

df.isnull().sum()

#Check Duplicates:
df.duplicated().sum()

#Check data types:
df.dtypes

# Convert the access_to_mental_health_resources column from object type to boolean:
df['access_to_mental_health_resources'] = df['access_to_mental_health_resources'].map({'Yes': True, 'No': False})

def categorize_working_level(hours):
    if hours < 36:
        return 'part-time'    
    elif 36 <= hours <= 40:
        return 'regular_hours'
    elif 40 < hours <= 50:
        return 'overtime'
    else:
        return 'high_overtime'

df['working_level'] = df['hours_worked_per_week'].apply(categorize_working_level)

def seniority(years):
    if years < 2:
        return 'junior'
    elif 2 <= years <= 5:
        return "Associate"
    elif 5 < years <= 10:
        return "mid-senior"
    else:
        return 'Senior'

df['seniority'] = df['years_of_experience'].apply(seniority)

# Hypothesis 1: Remote jobs result in fewer cases of burnout.
filtered_df_burnout = df[df['mental_health_condition'] == 'Burnout']
grouped_df = filtered_df_burnout.groupby("work_location").agg({
    "employee_id": "count",
    "stress_level": lambda x: x.mode()[0],
    "satisfaction_with_remote_work": lambda x: x.mode()[0]
})
grouped_df
# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the employee count
ax.bar(grouped_df.index, grouped_df['employee_id'], color='skyblue', label='Employee Count')

# Set title and labels
ax.set_title('Employee Count by Work Location')
ax.set_xlabel('Work Location')
ax.set_ylabel('Number of Employees')

# Add actual numbers on top of the bars and text annotations for stress level and satisfaction
for index, (location, row) in enumerate(grouped_df.iterrows()):
    employee_count = row['employee_id']
    stress = row['stress_level']
    satisfaction = row['satisfaction_with_remote_work']
    ax.text(index, employee_count + 50,  # Adjust the vertical position to be slightly above the bar
            f'{employee_count}', ha='center', va='bottom', fontsize=10, color='blue')
    ax.text(index, employee_count - 100, 
            f'Stress: {stress}\nSatisfaction: {satisfaction}',
            ha='center', va='center', fontsize=9, color='black', wrap=True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
grouped_df_1 = filtered_df_burnout.groupby(["work_location","stress_level"]).agg({
    "employee_id": "count"
})
grouped_df_1
df_pivot = grouped_df_1.unstack(level='stress_level')
ax = df_pivot.plot(kind='bar', figsize=(10, 8), colormap="tab20", width=0.7)

ax.set_title('Employee Count by Stress Level and Work Location')
ax.set_xlabel('Work Location')
ax.set_ylabel('Number of Employees')
ax.set_xticklabels(df_pivot.index, rotation=45, ha='right')
ax.legend(title='Stress Level', loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Adding data labels on top of bars
for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

# Hypothesis 2: Is seniority-level related to burnout?
# creating seniority levels based on years of experience
seniority_counts = df['seniority'].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(seniority_counts, labels=seniority_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen','#DA70D6'])
plt.title('Seniority Level')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

filtered_df_burnout = df[df['mental_health_condition'] == 'Burnout']
pivot_table_jr= filtered_df_burnout.reset_index().pivot_table(index='seniority',columns='job_role',values='employee_id',aggfunc='count')
pivot_table_jr['Total'] = pivot_table_jr.sum(axis=1)
pivot_table_jr = pivot_table_jr.sort_values(by='Total', ascending=False)
pivot_table_jr = np.ceil(pivot_table_jr).astype(int)
pivot_table_jr

pivot_table_jr1 = df.reset_index().pivot_table(index='seniority',columns='job_role',values='employee_id',aggfunc='count')
pivot_table_jr1['Total'] = pivot_table_jr1.sum(axis=1)
pivot_table_jr1 = pivot_table_jr1.sort_values(by='Total', ascending=False)
pivot_table_jr1 = np.ceil(pivot_table_jr1).astype(int)
pivot_table_jr1

pivot_table_jr['Employee-to-Burnout Ratio'] = pivot_table_jr['Total']/pivot_table_jr1['Total'] * 100
pivot_table_jr

#Burnout Relationship with Job Role and Work Location
filtered_df_burnout = df[df['mental_health_condition'] == 'Burnout']
pivot_table = filtered_df_burnout.reset_index().pivot_table(index='job_role',columns='work_location',values='employee_id',aggfunc='count')
pivot_table['Total'] = pivot_table.sum(axis=1)
np.ceil(pivot_table).astype(int)

# Plotting the pie chart using the 'Total' column
plt.figure(figsize=(8, 8))
plt.pie(pivot_table['Total'], labels=pivot_table.index, autopct='%1.1f%%', startangle=140)
plt.title('% in each role with Burnout')
plt.axis('equal')  # Ensures the pie is a circle
plt.show()

#Relationship Between Industry and Burnout
# Calculate the proportion of burnout (Yes) in each industry
industry_burnout = df.groupby('industry')['mental_health_condition'].value_counts(normalize=True).unstack()
# Get only the proportion of 'Yes' for burnout
industry_burnout = industry_burnout['Burnout'].reset_index()
# Rename the column for clarity
industry_burnout.rename(columns={'Burnout': 'proportion_burnout'}, inplace=True)
# Sort the values for better visualization
industry_burnout.sort_values(by='proportion_burnout', ascending=False, inplace=True)

# Plot the results
plt.figure(figsize=(8, 5))
plt.bar(industry_burnout['industry'], industry_burnout['proportion_burnout'], color='skyblue')
plt.xlabel('Industry')
plt.ylabel('Proportion of Burnout (Mental Health Condition)')
plt.title('Proportion of Burnout by Industry')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Print the results
print(industry_burnout)

# Calculate the proportion of burnout (Yes) in each region
region_burnout = df.groupby('region')['mental_health_condition'].value_counts(normalize=True).unstack()
# Get only the proportion of 'Yes' for burnout
region_burnout = region_burnout['Burnout'].reset_index()
# Rename the column for clarity
region_burnout.rename(columns={'Burnout': 'proportion_burnout'}, inplace=True)
# Sort the values for better visualization
region_burnout.sort_values(by='proportion_burnout', ascending=False, inplace=True)
# Plot the results
plt.figure(figsize=(8, 5))
plt.bar(region_burnout['region'], region_burnout['proportion_burnout'], color='skyblue')
plt.xlabel('Region')
plt.ylabel('Proportion of Burnout (Mental Health Condition)')
plt.title('Proportion of Burnout by Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
# Print the results
print(region_burnout)

#Hypothesis 3: Individuals who work long hours more likely to experience burnout.

# Define a function to categorize hours_worked_per_week
def categorize_hours_worked(hours):
    if hours <= 40:
        return '<=40 hours'
    else:
        return '>40 hours'

# Create a new column using the categorize_hours_worked function
df['hours_worked_category'] = df['hours_worked_per_week'].apply(categorize_hours_worked)
# Group by hours_worked_category and calculate the proportion of burnout
burnout_proportion = df.groupby('hours_worked_category')['mental_health_condition'].value_counts(normalize=True).unstack().fillna(0)
# Get only the proportion of 'Yes' for burnout
burnout_proportion = burnout_proportion['Burnout'].reset_index()
# Rename the column for clarity
burnout_proportion.rename(columns={'Burnout': 'proportion_burnout'}, inplace=True)
# Print the results
print(burnout_proportion)
# Plot the results in a pie chart
fig, ax = plt.subplots()
ax.pie(burnout_proportion['proportion_burnout'], labels=burnout_proportion['hours_worked_category'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  
plt.title('Proportion of Burnout by Hours Worked Category')
plt.show()

# Hypothesis 4: Individuals who smoke are at a higher risk of experiencing burnout
# we do not relieable data to test it, but we can test the level of absentism for smokers vs non smokers
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df2, x='absenteeism_time_in_hours', hue='social_smoker', bins=15, kde=True)
plt.title('Absenteeism Distribution by Social Smoker Status')
plt.show()

result = df2.groupby('social_smoker').agg({
    'absenteeism_time_in_hours': 'sum',
    'id': 'count'
})
result['sum_versus_count'] = (result['id'] / result['absenteeism_time_in_hours']) * 100
# Display the result
print(result)
# Group by social_drinker and calculate the average absenteeism hours
result = df2.groupby('social_drinker').agg({
    'absenteeism_time_in_hours': 'sum',
    'id': 'count'
})

result['sum_versus_count'] = (result['id'] / result['absenteeism_time_in_hours']) * 100

# Display the result
print(result)
#Hypothesis 5: Can absenteeism predict burnout?
# WE DO NOT HAVE SUITABLE DATA FOR THIS
result2 = df2.groupby("keyword_reason_for_absence")["absenteeism_time_in_hours"].sum().sort_values(ascending=False)
result2
print(result2['mental_disorders']/result2.sum() *100)
print(result2['musculoskeletal']/result2.sum() * 100)

sorted_result = result2.sort_values(ascending=True)
sorted_result.plot(kind='barh', figsize=(12, 10), color='skyblue')
plt.xlabel('keyword_reason_for_absence')  # Label for the x-axis
plt.title('Total Absenteeism Time by Reason for Absence')  # Title of the plot
# Adding grid for better readability
plt.grid(axis='x')
plt.show()

!pip install requests beautifulsoup4
!pip install selenium
!pip install webdriver-manager

import requests
from bs4 import BeautifulSoup
import re

def scrape_and_extract(url1, keywords):
    # Fetch the webpage content
    response = requests.get(url1)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script, style, header, footer, and navigation elements
    for script in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
        script.extract()
    
    text = ' '.join(soup.stripped_strings)  # Extract text and remove excessive spaces
    
    # Remove references and unwanted sections
    text = re.sub(r'80 Burnout Statistics: Remote Work and Workplace Stress.*?Book a demo Contents ', '', text, flags=re.DOTALL)
    text = re.sub(r'Book a demo today Sources .*', '', text, flags=re.DOTALL)
    text = re.sub(r'\bMoving into the next section.*?[.!?]', '', text, flags=re.IGNORECASE)  # Remove sentences containing this phrase
    
    # Find all <a> tags (links) in the content and extract their text
    links = [a.get_text() for a in soup.find_all('a', href=True)]

    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Extract sentences containing any of the keywords or a link with a keyword
    matching_sentences = []
    for sentence in sentences:
        # Remove the specific phrase 'Manager Burnout Rates by Generation' from the sentence
        sentence = re.sub(r'\bManager Burnout Rates by Generation\b', '', sentence, flags=re.IGNORECASE)
        
        # Skip sentences containing the word 'statistics' (case insensitive)
        if 'statistics' in sentence.lower():
            continue
        
        # Skip sentences containing the word 'flair' (case insensitive)
        if 'flair' in sentence.lower():
               continue
        
        # Check if the sentence contains any keyword
        contains_keyword = any(keyword in sentence.lower() for keyword in keywords)
        
        # If it contains a keyword or has a link and a keyword, include it
        if contains_keyword or (any(link in sentence for link in links) and contains_keyword):
            sentence = re.sub(r'^\d+\s*(?!%)', '', sentence)  # Remove leading numbers not followed by %
            matching_sentences.append(sentence.strip())
    
    return matching_sentences

# URL of the blog post
url1 = "https://flair.hr/en/blog/burnout-statistics/"

# Keywords to search for
keywords = ["remote", "absence", "absences", "absenteeism", "hours"]

# Scrape and extract sentences
results = scrape_and_extract(url1, keywords)

# Print the extracted sentences
print("Sentences containing the words 'remote', 'absence', 'absences', 'absenteeism', 'hours', or links:")
for i, sentence in enumerate(results, 1):
    print(f"{i}. {sentence.strip()}")
print("Data source:", url1)


# Send a GET request to the webpage
url2 = "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/burnout/art-20046642"
response = requests.get(url2)

# Parse the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant section of the page containing the causes of burnout
# This may require checking multiple sections or tags
sections = soup.find_all(["h2", "h3"])

# Initialize an empty list to store the causes
causes = []

# Extract causes from the section
found_section = False
for section in sections:
    if "Handling job burnout" in section.get_text():
        found_section = True
        # Get the next sibling until another h2 or h3 is found
        sibling = section.find_next_sibling()
        while sibling and sibling.name not in ["h2", "h3"]:
            if sibling.name == "ul":
                for li in sibling.find_all("li"):
                    causes.append(li.get_text())
            sibling = sibling.find_next_sibling()

# Check if any causes were found and print the extracted causes
if found_section and causes:
    print("Handling job burnout:")
    for idx, cause in enumerate(causes, start=1):
        print(f"{idx}. {cause}")
    print("Data source:", url2)
else:
    print("The specified section was not found on the page or no causes were listed.")